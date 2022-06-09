
from operator import truediv
from subprocess import call
from xmlrpc.client import boolean
from qgis.PyQt.QtCore import QSettings, QTranslator, QCoreApplication
from qgis.PyQt.QtGui import QIcon
from qgis.PyQt.QtWidgets import QAction, QLabel, QLineEdit, QMessageBox
from ui.client import client
from qgis.core import Qgis
from qgis.core import edit
from qgis.utils import iface
from qgis.core import (
    QgsCoordinateReferenceSystem,
    QgsCoordinateTransform,
    QgsProject,
    QgsPointXY,
)
# Initialize Qt resources from file resources.py
from  ui.resources import *
# Import the code for the dialog
from  ui.conquest_geo_dialog import ConquestGeoDialog
from  ui.conquest_geo_dialog_asset import ConquestGeoDialogAsset
import os.path
from swagger_client.models.conquest_api_object_type import ConquestApiObjectType

import webbrowser
import traceback

class Controller:
    connection_dlg = ConquestGeoDialog()

    def __init__(self) -> None:
        # TODO: create an error dialog to display details
        if not client.is_valid:
            self.connection_dlg.show()
            client.raise_invalid_credentials()

    def configure_connection(self):
        self.connection_dlg.show()


    def get_selected_features(self):
        canvas = iface.mapCanvas()
        layer = canvas.currentLayer()
        selected = []
        if layer:
            selected = layer.selectedFeatures()
        return selected

    def get_selected_geometries(self, as_epsg_4326=True):
        selected = self.get_selected_features()
        geoms = [f.geometry() for f in selected]
        if as_epsg_4326:
            crsSrc = self.get_srs()
            crsDst = QgsCoordinateReferenceSystem("EPSG:4326")
            context = QgsProject.instance()
            xform = QgsCoordinateTransform(crsSrc, crsDst, context)
            results = [g.transform(xform) == 0 for g in geoms]
            if not all(results):
                raise Exception(
                    'Unable to convert selected features to EPSG 4326 projection')
        return geoms

    def get_srs(self):
        canvas = iface.mapCanvas()
        layer = canvas.currentLayer()
        if layer:
            srs = layer.crs()  # .srsid()
            return srs
        return 0

    def count_selected(self):
        features = self.get_selected_features()
        if features is None: return 0
        return len(features)

    #def display_message(self, msg: str='') -> None:
    def display_message(self,msg):      
        qmsg = QMessageBox()        
        qmsg.setText(msg)        
        qmsg.exec()


class AssetCreationController(Controller):

    selected_feature = None
    index = 0
    # A feature has attributes
    # A feature is a row in a layer
    # Create a controller with the selected feature
    # Check that the feature can have an asset id
    # if it has an asset id, assign if the asset id is valid (not None or less or equal to 0)
    def __init__(self):
        print('Inside constructor')
        selected_features = self.get_selected_features()
       
        if len(selected_features) == 1:
            self.selected_feature = selected_features[0]           

    def asset_id(self):
        
        if self.selected_feature == None:
            return None  
        else: 
            #access the database of qgis and check for the data. 
            if self.selected_feature.attributes()[self.index] == None:
                return 0
            else:
                return self.selected_feature.attributes()[self.index]
             
        # if selected_feature.asset_id is None, return 0
        # otherwise return selected_feature.asset_id
        

    def should_create_new_asset(self):
        return self.selected_feature != None and self.asset_id() == 0

    def should_open_asset(self):
        return self.selected_feature != None and self.asset_id() != None and self.asset_id() > 0

    def supports_asset_id_column(self):
        # check that the self.selected_feature supports the asset_id column
        return self.layer_has_id_column()
        
    def layer_has_id_column(self):      
        layer = iface.activeLayer()
        field_names = [field.name() for field in layer.fields()]    
        for i in range(len(field_names)):
            if field_names[i] == 'AssetID':
                self.index = i
                return True             
        # not found
        return False

    # on selected what we delegate to when we click the conquest button
    # it assumes objects have been selected
    def on_selected(self):
        if self.supports_asset_id_column() == False:
            self.display_message('The layer for the selected feature needs to have an asset_id column')
            return

        if self.should_create_new_asset():
            self.create_new_asset()
            return

        if self.should_open_asset():
            self.open_asset()
            return

    def open_asset(self):
        webbrowser.open(f'https://link.conquest.live/?objectType=Asset&objectId={self.asset_id}', )

    def create_new_asset(self):
        self.asset_dlg = ConquestGeoDialogAsset()

        self.asset_dlg.reset_form()

        # get geometry
        number = self.count_selected()        
        if number != 1:
            msg = "Too many features selected. Please select only 1 geometry" if number else "No selected feature. Please select a geometry first"
            raise Exception(msg)
        geom = self.get_selected_geometries(as_epsg_4326=False)[0]
        geog = self.get_selected_geometries(as_epsg_4326=True)[0]

        # get projection
        srs = self.get_srs()
        if not srs: raise Exception('No projection identified')
        authority, srs_id, *unexpected = str(srs.authid()).split(':') # "authid() returns 'authority:srs_id' "
        srs_id = int(srs_id)
        if (srs_id not in client.supported_srs.keys()) or (authority == "QGIS"):
            raise Exception(f'Unsupported projection: {str(srs.authid())}.')
        if (unexpected):
            raise Exception(
                f'Unable to identify projection: {str(srs.authid())}.')

        # display coordinates on form
        self.asset_dlg.insert_row('Geometry', str(geom.asWkt()), False)
        self.asset_dlg.insert_row('Geography', str(geog.asWkt()), False)

        # select parent asset and asset type for new asset:
        client.reset_settings()
        result = self.select_asset_parameters()
        print(f'selected things are: {result}')

        # Create asset
        new_asset_id = 0
        if all(result):
            parent, assettype, description = result
            parent_id = parent.object_key.int32_value
            type_id = assettype.object_key.int32_value
            wkt = str(geog.asWkt())
            new_asset_id = client.create_asset(description=description, parent_id=parent_id,
                                      type_id=type_id, wkt_geometry=wkt)

        # Save the new asset id to the selected feature
        if new_asset_id != None and new_asset_id > 0:
            # An asset was created :)
            #self.selected_feature = 
            # TODO save the new_asset_id somehow
            # TODO check that self.asset_id() > 0
            self.display_message(f'Asset {self.asset_id()} created successfully')  
            self.open_asset() 


    def select_asset_parameters(self):
        dlg = self.asset_dlg
        # show the dialog
        dlg.show()
        # Run the dialog event loop
        result = dlg.exec()
        if result:
            selection = dlg.selection
            print(selection)
            return selection[ConquestApiObjectType.ASSET], selection[ConquestApiObjectType.ASSETTYPE], selection[dlg.ASSET_DESCRIPTION]
        return None, None, None