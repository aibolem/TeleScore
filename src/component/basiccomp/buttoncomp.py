"""
Author: Ian, TheLittleDoc, Fisk, Dan, Glenn
"""

from PyQt6 import uic
from PyQt6.QtCore import QEvent, QObject
from PyQt6.QtGui import QColor
from gm_resources import *
from ..abstractcomp import AbstractComp

class ButtonComp(AbstractComp):
    """
    Button widget for scoreboard.
    """
    
    def __init__(self, text, edit=False, parent=None):
        super().__init__(parent)
        path = resourcePath("src\\component\\basiccomp\\buttoncomp.ui")
        uic.loadUi(path, self) # Load the .ui file
        self.setStyleSheet("QPushButton {border: none; color: white; \
         font-size: 17px; border-radius: 4px;}")
        self.pushButton.setText(text)

        if (edit == True):
            self.pushButton.installEventFilter(self)

    def clicked(self):
        print("hello")
        
    def disableWidget(self) -> None:
        #self.pushButton.setDisabled(True)
        pass

    def setButtonColor(self, hexval: str) -> None:
        dimmed = QColor(hexval)
        dimmed.setRgb(dimmed.red()//2, dimmed.green()//2, dimmed.blue()//2)
        self.setStyleSheet(self.styleSheet() +
                             "QPushButton {background-color: " +
                            hexval + ";}" + 
                            "QPushButton:pressed{background-color: " + 
                             dimmed.name(QColor.NameFormat.HexRgb) + ";}" +
                            "QPushButton:hover{color: #e8e8e8;}")
        pass

    def getName(self) -> str:
        return "Button"
