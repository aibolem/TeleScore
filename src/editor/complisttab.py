"""
Author: Ian, TheLittleDoc, Fisk, Dan, Glenn
"""

# This Python file uses the following encoding: utf-8
from PyQt6.QtWidgets import QWidget, QPushButton
from PyQt6.QtGui import QDrag, QStandardItemModel, QStandardItem
from PyQt6.QtCore import QMimeData, Qt, QByteArray, QModelIndex
from PyQt6 import uic
from gm_resources import *
from .comptab.compwidgethead import CompWidgetHead
from .comptab.compwidgetitem import CompWidgetItem

PATH = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
if PATH not in sys.path:
    sys.path.append(PATH)

from component.compattr import CompAttr

class CompListTab(QWidget):
    """
    Widget that displays all of the components for the scoreboard. 
    """
    
    def __init__(self, parent=None):
        super().__init__(parent) # Call the inherited classes __init__ method
        path = resourcePath("src/editor/complisttab.ui")
        uic.loadUi(path, self) # Load the .ui file
        self.tab = []
        self.loadTabs()
        self.treeView.pressed.connect(self.compItemClicked)

    def loadTabs(self) -> None:
        """
        Loads the category tab.

        :param: none
        :return: none
        """
        self.model = QStandardItemModel(0, 2)
        self.treeView.setModel(self.model)
        self.treeView.header().resizeSection(0, 240) 
        self.treeView.header().resizeSection(1, 30)
        for cat in CompAttr.category:
            header = CompWidgetHead(cat[CompAttr.TABNAME])
            self.model.appendRow(header)
            self.treeView.setFirstColumnSpanned(0, QModelIndex(), True)
            for i, comp in enumerate(cat[CompAttr.COMPONENT]):  # Refractor this please
                item = cat[CompAttr.COMPONENT][comp]
                component = CompWidgetItem(item[CompAttr.ICON], header, comp)
                header.setChild(i, component)
                instance = QStandardItem()
                header.setChild(i, 1, instance)
                infoButton = QPushButton()
                self.treeView.setIndexWidget(instance.index(), infoButton)
                component.setInfoButton(infoButton)


    def compItemClicked(self, index: QModelIndex) -> None:
        """
        Initiates drag support

        :param index: Item that is clicked
        :return: none
        """
        item = self.model.itemFromIndex(index)
        if (type(item) != CompWidgetHead):
            mimeData = QMimeData()
            convByte = str.encode(item.text())
            mimeData.setData("application/x-comp", QByteArray(convByte))
            drag = QDrag(self)
        
            drag.setMimeData(mimeData)
            drag.setPixmap(item.icon().pixmap(20, 20))
            drag.exec(Qt.DropAction.MoveAction | Qt.DropAction.CopyAction)



