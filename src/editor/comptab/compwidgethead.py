from PyQt6.QtWidgets import QTreeWidgetItem
from PyQt6.QtGui import QFont, QColor
from PyQt6.QtCore import Qt

class CompWidgetHead(QTreeWidgetItem):
    """
    Header item for the category list
    """

    def __init__(self, text="Default", parent=None):
        super().__init__(parent)
        self.role = Qt.ItemDataRole.DisplayRole; # All the items are for displaying
        self.setText(0, " "*8 + text) # Very bad way of centering it, change it at some point
        self.setFont(0, QFont("Open Sans Bold", 14))
        self.setTextAlignment(0, Qt.AlignmentFlag.AlignCenter)
        self.setBackground(0, QColor(200, 200, 200))
        self.setBackground(1, QColor(200, 200, 200))