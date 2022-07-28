"""
Author: Ian, TheLittleDoc, Fisk, Dan, Glenn
"""

from PyQt6.QtGui import QFont, QColor, QStandardItem
from PyQt6.QtCore import Qt

class PropWidgetHead(QStandardItem):
    """
    Header item for the category list
    """

    def __init__(self, text="Default"):
        super().__init__()
        self.setText(text)
        self.setFont(QFont("Open Sans Bold", 13))
        self.setEditable(False)
        self.setBackground(QColor(200, 200, 200))