"""
Developed By: JumpShot Team
Written by: riscyseven
"""

from PyQt6 import QtWidgets, uic
from PyQt6.QtGui import QIcon

from window.editor import Editor
from gm_resources import resourcePath, GMessageBox # Importing my PyInstaller resource manager
from fileio.layoutfile import LayoutFile
from layout.ctrllayout import CtrlLayout

class MainWindow(QtWidgets.QMainWindow):
    """
    
    """

    def __init__(self, parent=None):
        super().__init__(parent) # Call the inherited classes __init__ method
        self.initUI()
        self.layout = None

    def initUI(self):
        path = resourcePath("src/window/ui/mainwindow.ui") # replaced complicated path logic with resourcePath()
        uic.loadUi(path, self) # Load the .ui file
        self.setWindowTitle("TeleScore")
        self.setWindowIcon(QIcon(resourcePath("src/resources/icon.ico"))) # Using a slightly modified version of my PyInstaller Resource system. Also seen on line 18. Basically uses working directory OR temp directory for absolute paths to files.
        self.show() # Show the GUI

        self.toolBar.addWidget(QtWidgets.QPushButton(QIcon(resourcePath("src/resources/icon.ico")), " TeleScore v1.0"))
        self.toolBar.addSeparator()
        self.editModeButton = QtWidgets.QPushButton("Editor Mode")
        self.toolBar.addWidget(self.editModeButton)
        self.editModeButton.setEnabled(False)
        self.editModeButton.clicked.connect(self._editModeClicked)

        self.editor = Editor()
        self.setCentralWidget(self.editor)

        self.actionSaveAs.triggered.connect(self._saveAsTriggered)
        self.actionOpen.triggered.connect(self._openTriggered)
        self.actionNew.triggered.connect(self._newTriggered)
        self.actionSave.triggered.connect(self._saveTriggered)

    def _saveTriggered(self):
        if (self.editor != None):
            self.editor.saveAction()

    def _saveAsTriggered(self):
        if (self.editor != None):
            self.editor.saveAsAction()

    def _openTriggered(self):
        self.fileName = QtWidgets.QFileDialog.getOpenFileName(self, "Open Layout File", ".", "JSON File (*.json)")
        if (self.fileName[0] != "" and self.fileName[1] == "JSON File (*.json)"):
            self.editor = None
            self.layout = CtrlLayout()
            self.setCentralWidget(self.layout)
            try:
                file = LayoutFile(self.fileName[0], self.layout)
                file.load()
            except Exception:
                msg = GMessageBox("Layout File Load Error", "This file is not compatible with this version of JumpShot", "Info")
                msg.exec()
                return
            self.editModeButton.setEnabled(True)

    def _editModeClicked(self):
        self.layout = CtrlLayout()
        file = LayoutFile(self.fileName[0], self.layout)
        file.load(True)
        self.editor = Editor(self.layout, file)
        self.editModeButton.setEnabled(False)

        self.setCentralWidget(self.editor)

    def _newTriggered(self):
        self.layout = None
        self.editModeButton.setEnabled(False)
        self.editor = Editor()
        self.setCentralWidget(self.editor)
