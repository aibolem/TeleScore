"""
Author: Ian, TheLittleDoc
"""

import os

from PyQt6 import uic
from PyQt6.QtWidgets import QWidget
from gm_resources import *

class StartMenu(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent) # Call the inherited classes __init__ method
        path = resourcePath("src/window/ui/startmenu.ui")
        uic.loadUi(path, self) # Load the .ui file
