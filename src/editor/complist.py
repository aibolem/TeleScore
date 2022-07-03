# This Python file uses the following encoding: utf-8
from unicodedata import category
from PyQt6.QtWidgets import QWidget
from PyQt6 import uic
from gm_resources import *
from .comptab.tabfactory import TabFactory

class CompList(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent) # Call the inherited classes __init__ method
        path = resourcePath("src\\editor\\complist.ui")
        uic.loadUi(path, self) # Load the .ui file
        self.loadTabs()

    def loadTabs(self):
        self.categoryTab.clear()
        for cat in TabFactory.categories():
            self.categoryTab.addTab(TabFactory.makeTab(cat), cat)

    def dragEvent(self):
        pass

        
