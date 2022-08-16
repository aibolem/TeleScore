"""
Author: Ian, TheLittleDoc, Fisk, Dan, Glenn
"""

from PyQt6.QtCore import QFile, QByteArray, QTextStream

class TextOut:
    def __init__(self, parent=None):
        self.fileIO = QFile(parent)
        self.fileName = ""

    def setOutputFile(self, fileAddr: str) -> None:
        self.fileIO.setFileName(fileAddr)
        self.fileName= fileAddr

    def outputFile(self, value):
        if (self.fileIO.open(QFile.OpenModeFlag.WriteOnly)):
            self.fileIO.write(QByteArray(bytes(value, "utf-8")))
            self.fileIO.close()

    def getOutputFile(self) -> str:
        return self.fileIO.fileName()