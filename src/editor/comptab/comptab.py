# This Python file uses the following encoding: utf-8
from PyQt6.QtWidgets import QWidget, QGridLayout
from PyQt6 import uic
from gm_resources import *

class CompTab(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent) # Call the inherited classes __init__ method
