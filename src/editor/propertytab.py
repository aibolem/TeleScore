"""
Developed By: JumpShot Team
Written by: riscyseven
Designed by: Fisk31
"""

from PyQt6.QtWidgets import QWidget
from PyQt6 import uic
from PyQt6.QtCore import QModelIndex, pyqtSignal
from PyQt6.QtGui import QStandardItemModel, QStandardItem

from attr import CompAttr
from editor.proptab.propwidgethead import PropWidgetHead
from editor.proptab.propwidgetitem import PropWidgetItem
from gm_resources import resourcePath

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
        self.treeView.setAlternatingRowColors(True)
        self.treeView.setProperty("class", "PropListView")
        self.objectName = ""

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

        #try:
        self._parseProperties(settings)
        '''except Exception as ex:
            self.clearTree()
            errMsg = GMessageBox("Error Loading Properties",
                                "There was an issue parsing the properties dictionary.\n"
                                "Exception: " + str(ex) +"\nPlease check the "
                                "format of the properties dictionary!", "Info")
            errMsg.exec()'''
    
    def _parseProperties(self, settings: dict):
        for i, tabName in enumerate(settings):    # Goes through the dictionary
            tabHead = PropWidgetHead(tabName)
            self.model.appendRow(tabHead)
            # This sets the header to span all the columns
            self.treeView.setFirstColumnSpanned(i, QModelIndex(), True)
            self.treeView.setExpanded(tabHead.index(), True) # Making sure the tabs are expanded

            properties = settings[tabName][CompAttr.PROPERTIES]
            for i, propertyName in enumerate(properties):                
                instance = QStandardItem()
                tabItem = None
                property = properties[propertyName]

                if (tabName == "Connection Properties"): # We are assuming that Component Name has been called before
                    tabItem = PropWidgetItem(tabHead, propertyName, 
                    property[CompAttr.TYPE], (self.objectName, property[CompAttr.VALUE]))
                    tabItem.setCallBack(self._propItemChanged)
                    tabHead.insertRow(i, [tabItem, instance])
                    self.treeView.setFirstColumnSpanned(i, tabHead.index(), True)
                else:
                    tabItem = PropWidgetItem(tabHead, propertyName, 
                    property[CompAttr.TYPE], property[CompAttr.VALUE])
                    tabItem.setCallBack(self._propItemChanged)
                    tabHead.insertRow(i, [tabItem, instance])

                self.treeView.setIndexWidget(instance.index(),
                    tabItem.getWidget())

                if (propertyName == "Component Name"):
                    self.objectName = property[CompAttr.VALUE]

    def _propItemChanged(self, item: PropWidgetItem, value):
        # This should be rewritten. Possible edge case is that if there are more than one linedit with editFinish,
        # editFinish could get called after item is deleted
        if (value != None):
            self.settings[item.parent().text()][CompAttr.PROPERTIES][item.text()][CompAttr.VALUE] = value
        self.propChanged.emit()
            

    def externalChange(self):
        self.loadProperties(self.settings)

        