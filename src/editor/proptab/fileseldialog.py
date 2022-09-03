"""
Developed By: JumpShot Team
Written by: riscyseven
"""

from PyQt6.QtWidgets import QWidget, QFileDialog
from PyQt6 import uic
from gm_resources import resourcePath
from attr import CompAttr

class FileSelDialog(QWidget):
    def __init__(self, mode, callback, fileName="", parent=None):
        super().__init__(parent)
        path = resourcePath("src/editor/proptab/fileseldialog.ui") # replaced complicated path logic with resourcePath()
        uic.loadUi(path, self) # Load the .ui file
        self.lineEdit.setText(fileName)
        if (mode == CompAttr.FLOPEN):
            self.absPathButton.clicked.connect(self._openFile)
        else:
            self.absPathButton.clicked.connect(self._saveFile)

        self.callBack = callback
        self.lineEdit.editingFinished.connect(self._editFinished)

    def _saveFile(self):
        fileName = QFileDialog.getSaveFileName(caption="Set Output File Name", directory="")
        if (fileName[0] != '' and fileName[0] != ''):
            fileName = fileName[0]
            if (".txt" in fileName):
                fileName = fileName.replace(".txt", "")
            self.lineEdit.setText(fileName)
            self._editFinished()

    def _openFile(self):
        fileName = QFileDialog.getOpenFileName(caption="Open File", directory="")
        self.lineEdit.setText(fileName[0])
        self._editFinished()

    def _editFinished(self):
        self.callBack(self.lineEdit.text())