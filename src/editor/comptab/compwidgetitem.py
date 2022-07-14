from PyQt6.QtWidgets import QTreeWidgetItem, QPushButton
from PyQt6.QtGui import QIcon, QFont
from PyQt6.QtCore import Qt, QSize
from gm_resources import resourcePath

class CompWidgetItem(QTreeWidgetItem):
    """
    Each component listed in the component list is made from 
    this class object. This widget item will standardize attributes
    such as the fonts, icon image size, etc.
    """

    def __init__(self, icon, parent, treeWidget, text="Default"):
        """
        Consturctor for a component list item

        :param icon: Icon for the component
        :param parent: Header/category of the item
        :param treeWidget: Main component list widget
        :param text: Description of the component

        :return: none
        """
        super().__init__(parent) # This sets this component to be the subcomponent of the header
        self.role = Qt.ItemDataRole.DisplayRole; # All the items are for displaying
        self.setText(0, text)
        self.setFont(0, QFont("Open Sans Bold", 12))
        if (icon != None):
            self.setIconFile(icon)

        infoButton = QPushButton()
        infoButton.setIconSize(QSize(20, 20))
        infoButton.setIcon(QIcon(resourcePath("src\\resources\\infoButton.png")))
        infoButton.setStyleSheet("border: none;")
        treeWidget.setItemWidget(self, 1, infoButton)

    def setIconFile(self, iconFile):
        icon = QIcon(iconFile)
        self.setIcon(0, icon)
        