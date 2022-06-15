import os

from PyQt6 import QtWidgets, uic
from pathlib import Path
from .startmenu import StartMenu
from .editor import Editor
from gm_resources import * # Importing my PyInstaller resource manager

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self, *args):
        super().__init__(*args) # Call the inherited classes __init__ method
        self.initUI()
        self.setWindowTitle("GameMaster")

    def initUI(self):
        path = os.fspath(Path(__file__).resolve().parent / "ui/mainwindow.ui") # This is very clunky, should change this.
        path = resourcePath("src\\window\\ui\\mainwindow.ui") # replaced complicated path logic with resourcePath()
        uic.loadUi(path, self) # Load the .ui file
        self.show() # Show the GUI

        menu = Editor()
        self.setCentralWidget(menu)