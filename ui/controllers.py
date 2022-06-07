
from subprocess import call
from qgis.PyQt.QtCore import QSettings, QTranslator, QCoreApplication
from qgis.PyQt.QtGui import QIcon
from qgis.PyQt.QtWidgets import QAction, QLabel, QLineEdit, QMessageBox
from ui.client import client
from qgis.core import Qgis
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

    def display_message(self, msg: str='') -> None:
        msg = QMessageBox()
        msg.setText(msg)
        print(dir(msg))
        msg.exec()


class AssetCreationController(Controller):

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

    def new_asset_creation(self):
        # TODO: create an error dialog to display details
        success = False
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
        asset_id = 0  # 2634
        if all(result):
            parent, assettype, description = result
            parent_id = parent.object_key.int32_value
            type_id = assettype.object_key.int32_value
            wkt = str(geog.asWkt())
            asset_id = client.create_asset(description=description, parent_id=parent_id,
                                      type_id=type_id, wkt_geometry=wkt)
        print(asset_id)

        # TODO: Update feature (add asset id to qgis record)

        # Open asset in app for further editing
        if success or asset_id:
            self.display_message(f'Asset {asset_id} created')
            webbrowser.open(
                f'https://link.conquest.live/?objectType=Asset&objectId={asset_id}', )

        # TODO: Clean up?

        return
