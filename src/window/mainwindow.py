"""
Author: Ian, TheLittleDoc, Fisk, Dan, Glenn
"""

import os, sys

from PyQt6 import QtWidgets, uic
from PyQt6.QtGui import QIcon

PATH = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
if PATH not in sys.path:
    sys.path.append(PATH)

from window.editor import Editor
from gm_resources import * # Importing my PyInstaller resource manager
from fileio.layoutfile import LayoutFile
from layout.ctrllayout import CtrlLayout

class MainWindow(QtWidgets.QMainWindow):
    """

    """

    def __init__(self, parent=None):
        super().__init__(parent) # Call the inherited classes __init__ method
        self.initUI()

    def initUI(self):
        path = resourcePath("src/window/ui/mainwindow.ui") # replaced complicated path logic with resourcePath()
        uic.loadUi(path, self) # Load the .ui file
        self.setWindowTitle("JumpShot")
        self.setWindowIcon(QIcon(resourcePath("src/resources/icon.ico"))) # Using a slightly modified version of my PyInstaller Resource system. Also seen on line 18. Basically uses working directory OR temp directory for absolute paths to files.
        self.show() # Show the GUI

        self.editor = Editor()
        self.setCentralWidget(self.editor)

        self.actionSaveAs.triggered.connect(self.saveAsTriggered)
        self.actionOpen.triggered.connect(self.openTriggered)
        self.actionNew.triggered.connect(self.newTriggered)

        self.toolBar.addWidget(QtWidgets.QPushButton(QIcon(resourcePath("src/resources/icon.ico")), " JumpShot v1.0"))
        self.toolBar.addSeparator()
        self.editModeButton = QtWidgets.QPushButton("Editor Mode")
        self.toolBar.addWidget(self.editModeButton)
        self.editModeButton.setEnabled(False)
        self.editModeButton.clicked.connect(self._editModeClicked)

    def saveAsTriggered(self):
        if (self.editor != None):
            self.editor.saveAction()

    def openTriggered(self):
        self.fileName = QtWidgets.QFileDialog.getOpenFileName(self, "Open Layout File", ".", "JSON File (*.json)")
        if (self.fileName[0] != "" and self.fileName[1] == "JSON File (*.json)"):
            del self.editor # Assuming editor will be the first thing to open. If the order changes, change this too.
            self.editor = None
            self.layout = CtrlLayout()
            self.setCentralWidget(self.layout)
            file = LayoutFile(self.fileName[0], self.layout)
            file.load()
            self.editModeButton.setEnabled(True)

    def _editModeClicked(self):
        del self.layout
        layout = CtrlLayout()
        file = LayoutFile(self.fileName[0], layout)
        file.load(True)
        self.editor = Editor(layout)
        self.editModeButton.setEnabled(False)

        self.setCentralWidget(self.editor)

    def newTriggered(self):
        if (self.editor == None):
            del self.layout
            self.editor = Editor()
            self.setCentralWidget(self.editor)
