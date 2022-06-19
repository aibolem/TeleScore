# This Python file uses the following encoding: utf-8
from PyQt6.QtWidgets import QWidget, QPushButton

from .freelayout import FreeLayout

class CtrlLayout(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.layout = FreeLayout()
        self.setLayout(self.layout)
        
        item = QPushButton("Hello")
        self.layout.addWidget(item)
