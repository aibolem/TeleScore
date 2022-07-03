# This Python file uses the following encoding: utf-8
from PyQt6 import uic
from .comptab import CompTab
from gm_resources import *

class ClockTab(CompTab):
    def __init__(self, parent=None):
        super().__init__(parent) # Call the inherited classes __init__ method
        path = resourcePath("src\\editor\\comptab\\clocktab.ui")
        uic.loadUi(path, self) # Load the .ui file
