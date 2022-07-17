"""
Author: Ian, TheLittleDoc, Fisk, Dan, Glenn
"""

from PyQt6.QtWidgets import QPushButton
from PyQt6 import uic
from gm_resources import *
from ..abstractcomp import AbstractComp

class ButtonComp(AbstractComp):
    """
    Button widget for scoreboard.
    """
    
    def __init__(self, parent=None):
        super().__init__(parent)
        path = resourcePath("src\\component\\basiccomp\\buttoncomp.ui")
        uic.loadUi(path, self) # Load the .ui file
        
    def disableWidget(self) -> None:
        self.pushButton.setEnabled(False)

    def setButtonColor(self, hexval: str) -> None:
        self.setStyleSheet("QPushButton {background-color: " + hexval + ";}")

    def getName() -> str:
        return "Button"