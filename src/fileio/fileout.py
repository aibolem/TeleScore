"""
Author: Ian, TheLittleDoc, Fisk, Dan, Glenn
"""

from abc import abstractmethod
from PyQt6.QtCore import QFile, QByteArray
from PyQt6.QtGui import QPixmap

class FileOut:
    def __init__(self, fileName="", parent=None):
        self.fileIO = QFile(fileName, parent)
        
    def setOutputFile(self, fileAddr: str):
        self.fileIO.setFileName(fileAddr)
        self.outputFile(None)
        self.fileName = fileAddr

    def getOutputFile(self) -> str:
        return self.fileIO.fileName()

    @abstractmethod
    def outputFile(self, value):
        pass

class TextOut(FileOut):
    def __init__(self, fileName="", parent=None):
        super().__init__(fileName, parent)

    # Override
    def outputFile(self, value):
        if (value == None):
            value = ""
        if (self.fileIO.open(QFile.OpenModeFlag.WriteOnly)):
            self.fileIO.write(QByteArray(bytes(value, "utf-8")))
            self.fileIO.close()

class ImageOut(FileOut):
    def __init__(self, fileName="", parent=None):
        super().__init__(fileName, parent)

    # Override
    def outputFile(self, value: QPixmap):
        if (value == None):
            value = QPixmap()

        # Modify it in the future
        value.save(self.getOutputFile(), "PNG")