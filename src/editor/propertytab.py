"""
Author: Ian, TheLittleDoc, Fisk, Dan, Glenn
"""

from PyQt6.QtWidgets import QWidget, QPushButton
from PyQt6 import uic
import sys, os

PATH = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
if PATH not in sys.path:
    sys.path.append(PATH)

from gm_resources import resourcePath

class PropertyTab(QWidget):
    """
    Widget that displays the properties information for a component
    """
    
    def __init__(self, parent=None):
        super().__init__(parent) # Call the inherited classes __init__ method
        path = resourcePath("src/editor/propertytab.ui")
        uic.loadUi(path, self) # Load the .ui file
        self.dockWidget.setTitleBarWidget(QWidget())


    def loadProperties(self):
        pass
        