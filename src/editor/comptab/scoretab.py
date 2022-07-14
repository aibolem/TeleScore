from .compwidgethead import CompWidgetHead
from .compwidgetitem import CompWidgetItem
from gm_resources import resourcePath

class ScoreTab():
    def __init__(self, treeWidget, parent=None):
        self.treeWidget = treeWidget
        self.parent = parent
        self.insertItems();

    def insertItems(self):
        pass