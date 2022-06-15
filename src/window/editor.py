import os

from PyQt6 import QtWidgets, uic
from pathlib import Path
from gm_resources import *

class Editor(QtWidgets.QMainWindow):
    def __init__(self, *args):
        super().__init__(*args) # Call the inherited classes __init__ method
        path = os.fspath(Path(__file__).resolve().parent / "ui/editor.ui")
        path = resourcePath("src\\window\\ui\\editor.ui")
        uic.loadUi(path, self) # Load the .ui file
