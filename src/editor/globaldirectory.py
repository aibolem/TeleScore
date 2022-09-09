"""
Developed By: JumpShot Team
Written by: riscyseven
"""

from PyQt6.QtWidgets import QDialog, QMessageBox
from PyQt6 import uic
from editor.proptab.fileseldialog import FileSelWidget

from gm_resources import resourcePath
from attr import CompAttr

class GlobalDirectory(QDialog):
    def __init__(self, dirName, parent=None):
        super().__init__(parent)
        path = resourcePath("src/editor/globaldirectory.ui")
        uic.loadUi(path, self) # Load the .ui file
        self.fileDialog = FileSelWidget(CompAttr.DRSAVE, self._fileSelected, dirName, self)
        self.verticalLayout.addWidget(self.fileDialog)
        self.setWindowTitle("Set Global File Output Location")
        self.pushButton.clicked.connect(self._setClicked)
        self.dir = dirName

    def _fileSelected(self, dirName):
        self.dir = dirName

    def _setClicked(self):
        if (QMessageBox.warning(self, "Are you sure?", "This action will:\n"
            "   1. Change the root directory of each display component\n"
            "   2. Change all output file names to its component names\n"
            "Do you want to proceed?", QMessageBox.StandardButton.Ok |
                 QMessageBox.StandardButton.Cancel) == QMessageBox.StandardButton.Cancel):
                 self.dir = ""
        self.close()

    def getDirectory(self) -> str:
        return self.dir