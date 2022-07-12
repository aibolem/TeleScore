from PyQt6.QtWidgets import QTreeWidgetItem
from PyQt6.QtGui import QIcon

class CompWidgetItem(QTreeWidgetItem):
    """
    Each component listed in the component list is made from 
    this class object. This widget item will standardize attributes
    such as the fonts, icon image size, etc.
    """

    def __init__(self, parent=None):
        super().__init__(parent)

    # Override
    def __lt__(self):
        raise NotImplementedError

    # Override
    def clone(self):
        raise NotImplementedError

    # Override
    def data(self, column, role):
        raise NotImplementedError

    # Override
    def read(self, input):
        raise NotImplementedError

    # Override
    def setData(self, column, role, value):
        raise NotImplementedError

    # Override
    def write(self, out):
        raise NotImplementedError

    # Override
    def setIconFile(self, iconFile):
        self.setIcon