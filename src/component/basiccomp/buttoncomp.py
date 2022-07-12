from PyQt6.QtWidgets import QPushButton
from PyQt6 import uic
from gm_resources import *
from src.component.abstractcomp import AbstractComp

class ButtonComp(AbstractComp):
    """
    Button widget for scoreboard.
    """
    
    def __init__(self, prebutton=None):
        super().__init__(self)
        path = resourcePath("src\\editor\\\\buttoncomp.ui")
        uic.loadUi(path, self) # Load the .ui file
        
    def disableWidget(self):
        self.pushButton.setEnabled(False)