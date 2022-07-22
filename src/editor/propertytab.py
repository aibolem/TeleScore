"""
Author: Ian, TheLittleDoc, Fisk, Dan, Glenn
"""

from PyQt6.QtWidgets import QWidget, QPushButton
from PyQt6 import uic
from PyQt6.QtCore import Qt
import sys, os
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

    prop = [
            {
                "TABNAME": "Add [+] Properties",
                "PROPERTIES": [
                    ["Increase Number By:", "TEXTEDIT"],
                    ["Hotkey Button:", "TEXTEDIT"],
                    ]
            },
            {
                "TABNAME": "Button Properties",
                "PROPERTIES": [
                    ["Text Info:", "TEXTEDIT"],
                    ["Width", "NUMEDIT"],
                    ["Height", "NUMEDIT"],
                    ["Text Font:", "FONTEDIT"]
                ]
            }
        ]
    
    
    def __init__(self, parent=None):
        super().__init__(parent) # Call the inherited classes __init__ method
        path = resourcePath("src/editor/propertytab.ui")
        uic.loadUi(path, self) # Load the .ui file
        self.dockWidget.setTitleBarWidget(QWidget())
        self.loadProperties(self.prop)

    def loadProperties(self, settings: list):
        """
        Method that gets the property (list) from the caller
        and sets the tab
        """

        #try:
        for tab in settings:    # Goes through the dictionary
            tabName = tab[self.TABNAME]
            tabHead = PropWidgetHead(tabName, self.treeWidget)
            for properties in tab[self.PROPERTIES]:
                #tabItem = '
                tabItem = PropWidgetItem(None, tabHead, self.treeWidget, properties[0])
        #except Exception:
            #pass
        
    def resizeEvent(self, evt) -> None:
        width = int(self.width()/self.treeWidget.columnCount())

        for i in range(self.treeWidget.columnCount()):
            self.treeWidget.header().resizeSection(0, width) 
        