# This Python file uses the following encoding: utf-8
from PyQt6.QtWidgets import QFrame, QPushButton

from .abstract_layout.freelayout import FreeLayout

class CtrlLayout(QFrame):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.layout = FreeLayout()
        self.setLayout(self.layout)
        
        item = QPushButton("Hello")
        item.setGeometry(10, 50, 30, 30)
        self.layout.addWidget(item)

        item = QPushButton("Hello")
        item.setGeometry(50, 40, 30, 30)
        self.layout.addWidget(item)
