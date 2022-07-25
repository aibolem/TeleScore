"""
Author: Ian, TheLittleDoc, Fisk, Dan, Glenn
"""

from PyQt6.QtWidgets import QWidget, QLineEdit
from PyQt6 import uic
from PyQt6.QtCore import QModelIndex
from PyQt6.QtGui import QStandardItemModel, QStandardItem
from .proptab.propwidgethead import PropWidgetHead
from .proptab.propwidgetitem import PropWidgetItem
from gm_resources import resourcePath

class PropertyTab(QWidget):
    """
    Widget that displays the properties information for a component
    """

    TEXTEDIT = "TEXTEDIT"
    FONTEDIT = "FONTEDIT"
    NUMEDIT = "NUMEDIT"
    TABNAME = "TABNAME"
    PROPERTIES = "PROPERTIES"

    # CUSTOMWIDGET = "CUSTOMWIDGET" Maybe for the future

    defaultButtonProp = [
            {
                "TABNAME": "General Properties",
                "PROPERTIES": [
                    ["Component Name:", "TEXTEDIT"],
                    ["Width:", "TEXTEDIT"],
                    ["Height:", "TEXTEDIT"]
                ]
            },
            {
                "TABNAME": "Button Properties",
                "PROPERTIES": [
                    ["Text Info:", "TEXTEDIT"],
                    ["Text Font:", "TEXTEDIT"]
                ]
            }
        ]
    
    def __init__(self, parent=None):
        super().__init__(parent) # Call the inherited classes __init__ method
        path = resourcePath("src/editor/propertytab.ui")
        uic.loadUi(path, self) # Load the .ui file
        self.model = QStandardItemModel(0, 2)
        self.treeView.setModel(self.model)
        self.loadProperties(self.defaultButtonProp)

    def loadProperties(self, settings: list) -> None:
        """
        Method that gets the property (list) from the caller
        and sets the tab

        :param settings: List that contains all the properties information
        :return: none
        """

        for i, tab in enumerate(settings):    # Goes through the dictionary
            tabName = tab[self.TABNAME]
            tabHead = PropWidgetHead(tabName)
            self.model.appendRow(tabHead)
            # This sets the header to span all the columns
            self.treeView.setFirstColumnSpanned(i, QModelIndex(), True)
            self.treeView.setExpanded(tabHead.index(), True) # Making sure the tabs are expanded
            for i, properties in enumerate(tab[self.PROPERTIES]):
                tabItem = PropWidgetItem(tabHead, properties[0])
                tabHead.setChild(i, tabItem)
                
                instance = QStandardItem()
                tabHead.setChild(i, 1, instance)
                wid = None
                match properties[1]:
                    case self.TEXTEDIT:
                        wid = self._createTextEdit()
                
                self.treeView.setIndexWidget(instance.index(), wid)

    def _createTextEdit(self) -> None:
        """
        Creates a new QLineEdit widget to insert
        to the treeview

        :param: none (might change in the future for some attribute changes)
        :return: none
        """
        lineEdit = QLineEdit();
        return lineEdit

    def _createFontEdit(self):
        """
        Creates a new QPushButton widget to insert
        to the treeview, this pushbutton will open a font dialog

        :param: none (might change in the future for some attribute changes)
        :return: none
        """
        pass

    def _createNumEdit(self):
        """
        Creates a new QLineEdit widget to insert
        to the treeview. Restricted to only numbers

        :param: none (might change in the future for some attribute changes)
        :return: none
        """
        pass
        
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
        