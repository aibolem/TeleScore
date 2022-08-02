"""
Author: Ian, TheLittleDoc, Fisk, Dan, Glenn
"""

# This Python file uses the following encoding: utf-8
from PyQt6.QtWidgets import QLayout
from PyQt6.QtCore import QSize
import os, sys

class FreeLayout(QLayout):
    """
    New QLayout subclass that enables the component/widgets
    to be placed any where in the layout without any restrictions.
    """

    def __init__(self, parent=None):
        super().__init__(parent)
        self.items = [] # QLayoutItem List
        self.space = -1
        self.size = QSize()

    # Override
    def addItem(self, item) -> None:
        self.items.append(item)

    # Override
    def count(self) -> None:
        return len(self.items)

    # Override
    def indexOf(self, item) -> None:
        return self.items.index(item)

    # Override
    def itemAt(self, index) -> None:
        if (index < self.count()):
            return self.items[index]

    # Override
    def setSpacing(self, value) -> None: # Check documentation
        self.space = value

    def spacing(self):
        return self.space

    # Override
    def takeAt(self, index):
        self.items.remove(self.items[index])

    # Override
    def sizeHint(self):
        return self.size
        
