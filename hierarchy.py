from dataclasses import asdict, dataclass
from .client import client
from .vendor.conquest.models.conquest_api_object_type import ConquestApiObjectType
from .vendor.conquest.models.conquest_api_object_key import ConquestApiObjectKey
from .vendor.conquest.models.conquest_api_geography_data import ConquestApiGeographyData
from qgis.PyQt.QtWidgets import QTreeWidgetItem, QTreeWidget
from qgis.PyQt.QtGui import QStandardItemModel, QStandardItem
from typing import Optional
# from .vendor import dacite

@dataclass(frozen=True, eq=True, repr=True)
class ConquestObject:
    # uid: int
    # parent: int = 0
    # type: ConquestApiObjectType = ConquestApiObjectType.ASSET
    object_name: str
    object_key: ConquestApiObjectKey
    parent_key: Optional[ConquestApiObjectKey]
    geography: Optional[ConquestApiGeographyData] = None
    # depth: int
    def __str__(self):
        return f'{self.object_name} ({self.object_key.int32_value})'

    to_dict = asdict
    # def from_dict(self, data):
    #     return dacite.from_dict(ConquestObject, data)


    # def object_key(self):
    #     return ConquestApiObjectKey(self.uid, self.type)

    # def parent_key(self):
    #     return ConquestApiObjectKey(self.parent, self.type)


class HierarchyItem(QStandardItem):
    
    def __init__(self, cq_obj: ConquestObject):
        super().__init__()
        self.cq_obj = cq_obj
        self.setText(str(cq_obj))
        self.setEditable(False)



class HierarchyController:
    # items = set()

    def __init__(self, type, tree) -> None:
        self.type = type
        self.tree = tree
        # self.setHeaderLabel(type)
        root_node = tree.model().invisibleRootItem()
        self.root_node = root_node
        self.load_items(0)
    
    def load_items(self, parent, dummy: bool=True):
        uid = parent if not parent else parent.cq_obj.object_key.int32_value
        # if parent==0:
        new_items = client.list_children(uid=uid, type=self.type)
        new_items = [ConquestObject(o.object_name, o.object_key, o.parent_key) for o in new_items]
        print(new_items)
        # tree_items = [QTreeWidgetItem(None, i.object_name) for i in new_items]
        tree_items = [HierarchyItem(i) for i in new_items]
        for i in tree_items:
            if not dummy: break
            i.appendRows([self.dummy_item()]) # adding a dummy item to allow expanding the node
        if parent==0:
            self.root_node.appendRows(tree_items)
        # self.tree.insertTopLevelItems(None, tree_items)
        # self.items.update(new_items)
        return new_items, tree_items

    def dummy_item(self):
        return QStandardItem()






