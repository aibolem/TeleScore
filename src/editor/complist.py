# This Python file uses the following encoding: utf-8
from PyQt6.QtWidgets import QWidget
from PyQt6.QtGui import QDrag
from PyQt6.QtCore import QMimeData, Qt, QByteArray
from PyQt6 import uic
from gm_resources import *
from .comptab.tabfactory import TabFactory

class CompList(QWidget):
    """
    Widget that displays all of the components for the scoreboard. 
    """
    
    def __init__(self, parent=None):
        super().__init__(parent) # Call the inherited classes __init__ method
        path = resourcePath("src\\editor\\complist.ui")
        uic.loadUi(path, self) # Load the .ui file
        self.tab = []
        self.loadTabs()
        self.catWidget.itemClicked.connect(self.compItemClicked)

    def loadTabs(self):
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

    def compItemClicked(self, item):
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
        if (drag.exec(Qt.DropAction.MoveAction | Qt.DropAction.CopyAction)): # Seem to get null for the pixmap (file not found)
            pass

