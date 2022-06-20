# This Python file uses the following encoding: utf-8
from PyQt6 import uic
from comptab import CompTab
from gm_resources import *

class ScoreTab(CompTab):
    def __init__(self, parent=None):
        super().__init__(parent) # Call the inherited classes __init__ method
        self.gridlayout.addWidget()
