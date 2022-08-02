"""
Author: Ian, TheLittleDoc, Fisk, Dan, Glenn
"""

import os, sys
from types import NoneType
from PyQt6.QtWidgets import QWidget
from PyQt6 import uic
from PyQt6.QtCore import QModelIndex, pyqtSlot, pyqtSignal
from PyQt6.QtGui import QStandardItemModel, QStandardItem
from .proptab.propwidgethead import PropWidgetHead
from .proptab.propwidgetitem import PropWidgetItem
from gm_resources import resourcePath, GMessageBox

PATH = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
if PATH not in sys.path:
    sys.path.append(PATH)

from component.compattr import CompAttr

class PropertyTab(QWidget):
    """
    Widget that displays the properties information for a component
    """

    propChanged = pyqtSignal()

    def __init__(self, parent=None):
        super().__init__(parent) # Call the inherited classes __init__ method
        path = resourcePath("src/editor/propertytab.ui")
        uic.loadUi(path, self) # Load the .ui file
        self.model = QStandardItemModel(0, 2)
        self.treeView.setModel(self.model)

    def clearTree(self):
        if (self.model.hasChildren()):
            self.model.removeRows(0, self.model.rowCount())

    def resizeEvent(self, evt) -> None:
        """
        Anytime the treeview is resized, this is called to have
        each column to be sized proportionately. 

        :param evt: resize event information
        :return: none
        """
        width = int(self.width()/self.model.columnCount())

        for i in range(self.model.columnCount()):
            self.treeView.header().resizeSection(0, width) 

    def loadProperties(self, settings: dict) -> None:
        """
        Method that gets the property (list) from the caller
        and sets the tab

        :param settings: List that contains all the properties information
        :return: none
        """
        self.clearTree()
        self.settings = settings
        if (type(settings) == None):
            settings = CompAttr.defaultProp

        try:
            self._parseProperties(settings)
        except Exception as ex:
            self.clearTree()
            errMsg = GMessageBox("Error Loading Properties",
                                "There was an issue parsing the properties dictionary.\n"
                                "Exception: " + str(ex) +"\nPlease check the "
                                "format of the properties dictionary!", "Info")
            errMsg.exec()
    
    def _parseProperties(self, settings: dict):
        for i, tabName in enumerate(settings):    # Goes through the dictionary
            tabHead = PropWidgetHead(tabName)
            self.model.appendRow(tabHead)
            # This sets the header to span all the columns
            self.treeView.setFirstColumnSpanned(i, QModelIndex(), True)
            self.treeView.setExpanded(tabHead.index(), True) # Making sure the tabs are expanded

            properties = settings[tabName][CompAttr.PROPERTIES]
            for i, propertyName in enumerate(properties):
                property = properties[propertyName]
                tabItem = PropWidgetItem(tabHead, propertyName, 
                property[CompAttr.TYPE], property[CompAttr.VALUE])
                tabItem.setCallBack(self.propItemChanged)
                
                instance = QStandardItem()

                tabHead.insertRow(i, [tabItem, instance])
                self.treeView.setIndexWidget(instance.index(),
                    tabItem.getWidget())

    def propItemChanged(self, item: PropWidgetItem, value: str):
        self.settings[item.parent().text()][CompAttr.PROPERTIES][item.text()][CompAttr.VALUE] = value
        self.propChanged.emit()

        