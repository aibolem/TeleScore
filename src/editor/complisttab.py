"""
Developed By: JumpShot Team
Written by: riscyseven
Designed by: Fisk31
"""

# This Python file uses the following encoding: utf-8
from PyQt6.QtWidgets import QWidget, QPushButton
from PyQt6.QtGui import QDrag, QStandardItemModel, QStandardItem
from PyQt6.QtCore import QMimeData, Qt, QByteArray, QModelIndex
from PyQt6 import uic

from attr import CompAttr
from gm_resources import resourcePath
from editor.comptab.compwidgethead import CompWidgetHead
from editor.comptab.compwidgetitem import CompWidgetItem


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
        self.treeView.setProperty("class", "CompListView")
        self.treeView.setAlternatingRowColors(True)

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
        for i, cat in enumerate(CompAttr.category):
            header = CompWidgetHead(cat[CompAttr.TABNAME])
            self.model.appendRow(header)
            self.treeView.setFirstColumnSpanned(i, QModelIndex(), True)
            self.treeView.setExpanded(header.index(), True)
            for i, comp in enumerate(cat[CompAttr.COMPONENT]):  # Refractor this please
                item = cat[CompAttr.COMPONENT][comp]

                iconPath = resourcePath(item[CompAttr.ICON])
                component = CompWidgetItem(iconPath, header, comp)
                instance = QStandardItem()
  
                header.insertRow(i, [component, instance])
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



