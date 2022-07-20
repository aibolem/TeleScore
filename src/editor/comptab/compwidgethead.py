"""
Author: Ian, TheLittleDoc, Fisk, Dan, Glenn
"""

from ctypes import alignment
from PyQt6.QtWidgets import QTreeWidgetItem
from PyQt6.QtGui import QFont, QColor
from PyQt6.QtCore import Qt

class CompWidgetHead(QTreeWidgetItem):
    """
    Header item for the category list
    """

    def __init__(self, text="Default", align=Qt.AlignmentFlag.AlignCenter, parent=None):
        super().__init__(parent)
        self.role = Qt.ItemDataRole.DisplayRole; # All the items are for displaying
        spacing = 7
        if (align == Qt.AlignmentFlag.AlignLeft):
            spacing = 0
        else:
            self.setTextAlignment(0, Qt.AlignmentFlag.AlignCenter)
        self.setText(0, " "*spacing + text) # Very bad way of centering it, change it at some point
        self.setFont(0, QFont("Open Sans Bold", 14))
        self.setBackground(0, QColor(200, 200, 200))
        self.setBackground(1, QColor(200, 200, 200))