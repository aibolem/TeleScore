"""
Author: Ian, TheLittleDoc, Fisk, Dan, Glenn
"""

import os

from PyQt6 import QtWidgets, uic
from PyQt6.QtGui import QIcon # Went ahead and added QIcon
from pathlib import Path
from .startmenu import StartMenu
from .editor import Editor
from gm_resources import * # Importing my PyInstaller resource manager

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent) # Call the inherited classes __init__ method
        self.initUI()
        self.setWindowTitle("GameMaster")
        self.setWindowIcon(QIcon(resourcePath("src\\resources\\icon.ico"))) # Using a slightly modified version of my PyInstaller Resource system. Also seen on line 18. Basically uses working directory OR temp directory for absolute paths to files.

    def initUI(self):
        path = resourcePath("src\\window\\ui\\mainwindow.ui") # replaced complicated path logic with resourcePath()
        uic.loadUi(path, self) # Load the .ui file
        self.show() # Show the GUI

        menu = Editor()
        self.setCentralWidget(menu)