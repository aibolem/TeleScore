"""
Author: Ian, TheLittleDoc, Fisk, Dan, Glenn
"""

from PyQt6.QtWidgets import QPushButton
from PyQt6 import uic
from PyQt6.QtGui import QColor
from gm_resources import *
from ..abstractcomp import AbstractComp

class ButtonComp(AbstractComp):
    """
    Button widget for scoreboard.
    """
    
    def __init__(self, text, parent=None):
        super().__init__(parent)
        path = resourcePath("src\\component\\basiccomp\\buttoncomp.ui")
        uic.loadUi(path, self) # Load the .ui file
        self.setStyleSheet("QPushButton {border: none; color: white; \
         font-size: 17px; border-radius: 4px;}")
        self.pushButton.setText(text)
        
    def disableWidget(self) -> None:
        self.pushButton.setEnabled(False)

    def setButtonColor(self, hexval: str) -> None:
        dimmed = QColor(hexval)
        dimmed.setRgb(dimmed.red()//2, dimmed.green()//2, dimmed.blue()//2)
        self.setStyleSheet(self.styleSheet() +
                             "QPushButton {background-color: " +
                            hexval + ";}" + 
                            "QPushButton:pressed{background-color: " + 
                             dimmed.name(QColor.NameFormat.HexRgb) + ";}" +
                            "QPushButton:hover{color: #e8e8e8;}")

    def getName(self) -> str:
        return "Button"