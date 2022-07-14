from PyQt6.QtWidgets import QTreeWidgetItem
from PyQt6.QtGui import QIcon, QFont
from PyQt6.QtCore import Qt

class CompWidgetItem(QTreeWidgetItem):
    """
    Each component listed in the component list is made from 
    this class object. This widget item will standardize attributes
    such as the fonts, icon image size, etc.
    """

    def __init__(self, text="Default", icon=None, parent=None):
        super().__init__(parent)
        self.role = Qt.ItemDataRole.DisplayRole; # All the items are for displaying
        self.setText(0, text)
        self.setFont(0, QFont("Open Sans Bold", 12))
        if (icon != None):
            self.setIconFile(icon)

    def setIconFile(self, iconFile):
        icon = QIcon(iconFile)
        self.setIcon(0, icon)
        