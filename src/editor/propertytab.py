"""
Author: Ian, TheLittleDoc, Fisk, Dan, Glenn
"""

import os, sys
from tkinter import Spinbox
from types import NoneType
from PyQt6.QtWidgets import QWidget, QLineEdit, QSpinBox
from PyQt6 import uic
from PyQt6.QtCore import QModelIndex
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

    def __init__(self, parent=None):
        super().__init__(parent) # Call the inherited classes __init__ method
        path = resourcePath("src/editor/propertytab.ui")
        uic.loadUi(path, self) # Load the .ui file
        self.model = QStandardItemModel(0, 2)
        self.treeView.setModel(self.model)

    def clearTree(self):
        if (self.model.hasChildren()):
            self.model.removeRows(0, self.model.rowCount())


    def loadProperties(self, settings: list) -> None:
        """
        Method that gets the property (list) from the caller
        and sets the tab

        :param settings: List that contains all the properties information
        :return: none
        """
        self.clearTree()

        if (type(settings) == NoneType):
            settings = CompAttr.default
        
        try: 
            for i, tab in enumerate(settings):    # Goes through the dictionary
                tabName = tab[CompAttr.TABNAME]
                tabHead = PropWidgetHead(tabName)
                self.model.appendRow(tabHead)
                # This sets the header to span all the columns
                self.treeView.setFirstColumnSpanned(i, QModelIndex(), True)
                self.treeView.setExpanded(tabHead.index(), True) # Making sure the tabs are expanded

                for i, properties in enumerate(tab[CompAttr.PROPERTIES]):
                    property = tab[CompAttr.PROPERTIES][properties]
                    tabItem = PropWidgetItem(tabHead, properties)
                    tabHead.setChild(i, tabItem)
                    
                    instance = QStandardItem()
                    tabHead.setChild(i, 1, instance)
                    wid = None
                    match property[CompAttr.TYPE]:
                        case CompAttr.TEXTEDIT:
                            wid = self._createTextEdit(property[CompAttr.VALUE])
                        case CompAttr.NUMEDIT:
                            wid = self._createNumEdit(property[CompAttr.VALUE])
                    
                    self.treeView.setIndexWidget(instance.index(), wid)
        except Exception as ex:
            msgBox = GMessageBox("Error loading property tab", "TypeError: " + str(ex), "AskYesNo")
            msgBox.exec()

    def _createTextEdit(self, value) -> None:
        """
        Creates a new QLineEdit widget to insert
        to the treeview

        :param: none (might change in the future for some attribute changes)
        :return: none
        """
        lineEdit = QLineEdit(value)
        return lineEdit

    def _createFontEdit(self, value):
        """
        Creates a new QPushButton widget to insert
        to the treeview, this pushbutton will open a font dialog

        :param: none (might change in the future for some attribute changes)
        :return: none
        """
        pass

    def _createNumEdit(self, value):
        """
        Creates a new QLineEdit widget to insert
        to the treeview. Restricted to only numbers

        :param: none (might change in the future for some attribute changes)
        :return: none
        """
        spinBox = QSpinBox()
        if (type(value) == int):
            spinBox.setValue(value)
        else:
            spinBox.setValue(0)

        return spinBox
        
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
        