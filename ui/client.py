# from black import out
from qgis.PyQt.QtCore import QSettings
import swagger_client
from urllib.parse import urlparse
# from .conquest_geo_dialog import ConquestGeoDialog
from qgis.gui import QgsMessageBar
from qgis.core import Qgis
from qgis.utils import iface
from swagger_client.models.conquest_api_object_key import ConquestApiObjectKey
from swagger_client.models.conquest_api_geography_data import ConquestApiGeographyData

class Settings:
    _prefix = 'ConquestGeo'

    def get_setting(self, key, default=''):
        s = QSettings()
        p = self._prefix
        k = p+str(key) if not p in str(key) else str(key)
        return s.value(k, default)

    def set_setting(self, key, value):
        s = QSettings()
        p = self._prefix
        k = p+str(key) if not p in str(key) else str(key)
        print(f'saving {value} on {k}')
        s.setValue(k, value)
    
    def del_setting(self, key):
        s = QSettings()
        p = self._prefix
        k = p+str(key) if not p in str(key) else str(key)
        s.remove(k)
    
    def list_settings(self):
        s = QSettings()
        p = self._prefix
        return [k for k in s.allKeys() if p in k]

        

class Client(Settings):
    _url_key = 'api_url'
    _token_key = 'api_token'
    supported_srs = {
            3857: "WGS 84 / Pseudo-Mercator -- Spherical Mercator",
            4326: "WGS 84 / World Geodetic System 1984, used in GPS",
            4327: "WGS 84 / DEPRECATED (geographic 3D)",
            3395: "WGS 84 / World Mercator",
            28349: "GDA94 / MGA zone 49",
            28350: "GDA94 / MGA zone 50",
            28351: "GDA94 / MGA zone 51",
            28352: "GDA94 / MGA zone 52",
            28353: "GDA94 / MGA zone 53",
            28354: "GDA94 / MGA zone 54",
            28355: "GDA94 / MGA zone 55",
            28356: "GDA94 / MGA zone 56",
            32749: "WGS 84 / UTM zone 49S",
            32750: "WGS 84 / UTM zone 50S",
            32751: "WGS 84 / UTM zone 51S",
            32752: "WGS 84 / UTM zone 52S",
            32753: "WGS 84 / UTM zone 53S",
            32754: "WGS 84 / UTM zone 54S",
            32755: "WGS 84 / UTM zone 55S",
            32756: "WGS 84 / UTM zone 56S",
            7843: "GDA2020",
            7844: "GDA2020",
        }

    def __init__(self) -> None:
        super().__init__()
        self.reset_settings()
    
    @property
    def url(self):
        return self.get_setting(self._url_key)
    
    @url.setter
    def url(self, value):
        if value: # fix format, since the api client does not check formatting
            p = 'https://'
            value = value if '//' in value else p + value # urlparse needs to check for '//'
            value = p + urlparse(value).netloc
        self.set_setting(self._url_key, value)

    @url.deleter
    def url(self):
        self.set_setting(self._url_key, '')

    @property
    def token(self):
        return self.get_setting(self._token_key)

    @token.setter
    def token(self, value):
        self.set_setting(self._token_key, value)

    @token.deleter
    def token(self):
        self.set_setting(self._token_key, '')

    @property
    def not_expired(self):
        return self._test_token()

    @property
    def is_valid(self):
        if self.token and self.url and self._test_host():
            if self.not_expired: return True
        self.warn_invalid_credentials(iface)
        return False

    @property
    def api_client(self):
        config = swagger_client.Configuration()
        config.host = self.url
        config.api_key['Authorization'] = self.token
        config.api_key_prefix['Authorization'] = 'Bearer'
        config.verify_ssl = True # for testing locally
        config.debug = False # for testing and demonstration purposes, we can set debug to be verbose
        return swagger_client.ApiClient(configuration=config)

    def reset_settings(self):
        for k in self.list_settings():
            if not (self._url_key in k or self._token_key in k):
                print(f'removing setting on {k}')
                self.del_setting(k)

    
    def _test_host(self):
        """returns if host url is working"""
        print('testing host')
        try:
            output = swagger_client.SystemServiceApi(self.api_client).system_service_application_version_with_http_info()
            # print((output))
            print('ok')
            return True
        except Exception as e:
            print(f'invalid host: {e}')
            return False

    def _test_token(self):
        """returns if token is working"""
        print('testing token')
        try:
            output = self.list_children(0, conquest.ConquestApiObjectType.ASSET)
            # print((output))
            print('ok')
            return True
        except Exception as e:
            print(f'token failed: {e}')
            return False

    def warn_invalid_credentials(self, window=iface):
        msg = "The connection paramenters are invalid. Generate a new token and try again"
        window.messageBar().pushMessage(
            "Error", 
            msg, 
            level=Qgis.Critical, 
            duration=10
            )

    def raise_invalid_credentials(self):
        raise Exception("The connection paramenters are invalid. Generate a new token and try again")


    def list_children(self, uid: int, type: swagger_client.ConquestApiObjectType) -> set:
        # if not self.is_valid: return []
        body = swagger_client.ConquestApiListHierarchyNodesQuery(
            include_ancestors=False, 
            include_children=True, 
            include_sub_items=False,
            include_siblings=False,
            object_key=swagger_client.ConquestApiObjectKey(int32_value=uid, 
                                                    object_type=type)
        )
        output = swagger_client.ViewServiceApi(self.api_client).view_service_list_hierarchy_nodes(body=body)
        # depth = 0
        # filtered_output = []
        # for o in output.headers:
        #     print(o)
        #     if o.object_key.int32_value == uid and uid != 0:
        #         depth = o.depth
        #     elif o.parent_key.int32_value == uid:
        #         filtered_output.append(o)
            
        # output = sorted([o for o in output.headers if o.depth == depth+1 and o.object_key.int32_value != uid], key=lambda o: o.object_name)
        output = sorted([o for o in output.headers if o.parent_key.int32_value == uid and o.object_key.int32_value != uid], key=lambda o: o.object_name)
        return output

    def create_asset(self, description: str, parent_id: int, type_id: int=None, wkt_geometry: str=None):
        geog = ConquestApiGeographyData(wkt=wkt_geometry)
        body = swagger_client.ConquestApiCreateAssetCommand(
            asset_description=str(description), 
            parent_id=parent_id, 
            type_id=type_id
           #geography_data=geog
        )
        new_asset_id= swagger_client.AssetServiceApi(self.api_client).asset_service_create_asset(body=body)
        print(f'created asset {new_asset_id}')
        return new_asset_id

        

settings = Settings()
client = Client()
