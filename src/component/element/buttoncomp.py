from PyQt6.QtWidgets import QPushButton
from gm_resources import *
from src.component.abstractcomp import AbstractComp

class ButtonComp(AbstractComp):
    """
    Button widget for scoreboard.
    """
    
    def __init__(self, *args):
        super().__init__(self)
        path = resourcePath("src\\editor\\complist.ui\\buttoncomp.ui")
        uic.loadUi(path, self) # Load the .ui file
        