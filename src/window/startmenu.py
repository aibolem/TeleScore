import os

from PyQt6 import QtWidgets, uic
from pathlib import Path
from gm_resources import *

class StartMenu(QtWidgets.QWidget):
    def __init__(self, *args):
        super().__init__(*args) # Call the inherited classes __init__ method
        path = resourcePath("src\\window\\ui\\startmenu.ui")
        uic.loadUi(path, self) # Load the .ui file
