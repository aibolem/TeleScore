"""
Author: Ian, TheLittleDoc
"""

# This Python file uses the following encoding: utf-8
from PyQt6.QtWidgets import QWidget
from PyQt6.QtGui import QDrag
from PyQt6.QtCore import QMimeData, Qt, QByteArray
from PyQt6 import uic
from gm_resources import *
from .comptab.tabfactory import TabFactory
from .comptab.compwidgetitem import CompWidgetItem

class CompListTab(QWidget):
    """
    Widget that displays all of the components for the scoreboard. 
    """
    
    def __init__(self, parent=None):
        super().__init__(parent) # Call the inherited classes __init__ method
        path = resourcePath("src\\editor\\complisttab.ui")
        uic.loadUi(path, self) # Load the .ui file
        self.tab = []
        self.loadTabs()
        self.catWidget.itemPressed.connect(self.compItemClicked)

    def loadTabs(self) -> None:
        """
        Loads the category tab.

        :param: none
        :return: none
        """
        self.catWidget.header().resizeSection(0, 240) 
        self.catWidget.header().resizeSection(1, 30)
        self.catWidget.clear()
        for cat in TabFactory.categories():
            TabFactory.makeTab(cat, self.catWidget)

    def compItemClicked(self, item: CompWidgetItem) -> None:
        """
        Initiates drag support

        :param item: Item that is clicked
        :return: none
        """
        mimeData = QMimeData()
        convByte = str.encode(item.text(0))
        mimeData.setData("application/x-comp", QByteArray(convByte))
        drag = QDrag(self)
    
        drag.setMimeData(mimeData)
        drag.exec(Qt.DropAction.MoveAction | Qt.DropAction.CopyAction)



