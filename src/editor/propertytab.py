"""
Author: Ian, TheLittleDoc, Fisk, Dan, Glenn
"""

from PyQt6.QtWidgets import QWidget, QPushButton
from PyQt6 import uic
from PyQt6.QtCore import Qt
import sys, os
from .comptab.compwidgethead import CompWidgetHead
from .proptab.propwidgetitem import PropWidgetItem

PATH = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
if PATH not in sys.path:
    sys.path.append(PATH)

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
            tabHead = CompWidgetHead(tabName, Qt.AlignmentFlag.AlignLeft, self.treeWidget)
            for properties in tab[self.PROPERTIES]:
                #tabItem = '
                tabItem = PropWidgetItem(None, tabHead, self.treeWidget, properties[0])
        #except Exception:
            #pass
        

        