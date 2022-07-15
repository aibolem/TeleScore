from PyQt6.QtWidgets import QWidget
from PyQt6 import uic

from ..gm_resources import resourcePath

class Property(QWidget):
    """
    Widget that displays the properties information for a component
    """
    
    def __init__(self, parent=None):
        super().__init__(parent) # Call the inherited classes __init__ method
        path = resourcePath("src\\editor\\complist.ui")
        uic.loadUi(path, self) # Load the .ui file
        