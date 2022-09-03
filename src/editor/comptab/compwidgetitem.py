"""
Developed By: JumpShot Team
Written by: riscyseven
"""

from PyQt6.QtWidgets import QPushButton
from PyQt6.QtGui import QIcon, QFont, QStandardItem
from PyQt6.QtCore import Qt, QSize

from gm_resources import GMessageBox, resourcePath
from editor.comptab.compwidgethead import CompWidgetHead

class CompWidgetItem(QStandardItem):
    """
    Each component listed in the component list is made from 
    this class object. This widget item will standardize attributes
    such as the fonts, icon image size, etc.
    """

    def __init__(self, icon: QIcon, parent: CompWidgetHead, text="Default"):
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
        self.setText(text)
        self.setTextAlignment(Qt.AlignmentFlag.AlignLeft | Qt.AlignmentFlag.AlignVCenter)
        self.setFont(QFont("Open Sans Bold", 12))
        if (icon != None):
            self.setIconFile(icon)

    def setInfoButton(self, infoButton: QPushButton) -> None:
        self.infoButton = infoButton
        self.infoButton.setProperty("class", "InfoButton")
        self.infoButton.setIcon(QIcon(resourcePath("src/resources/infoButton.png")))
        self.infoButton.setStyleSheet("QPushButton {border: none;}")
        self.infoButton.pressed.connect(self.infoButtonClicked)
        self.infoButton.released.connect(self.infoButtonReleased)
        self.infoButton.setIconSize(QSize(20, 20))

    def infoButtonReleased(self):
        self.infoButton.setIcon(QIcon(resourcePath("src/resources/infoButton.png")))

    def infoButtonClicked(self):
        self.infoButton.setIcon(QIcon(resourcePath("src/resources/infoButtonDown.png")))
        msg = GMessageBox("Coming Soon", "Coming Soon", "Info")
        msg.exec()

    def setIconFile(self, iconFile: str) -> None:
        """
        Sets the icon next to the description

        :param iconFile: icon file location
        """
        icon = QIcon(iconFile)
        self.setIcon(icon)
        