"""
Developed By: JumpShot Team
Written by: riscyseven
"""

from PyQt6.QtGui import QFont, QStandardItem
from PyQt6.QtCore import Qt

class CompWidgetHead(QStandardItem):
    """
    Header item for the category list
    """

    def __init__(self, text="Default"):
        super().__init__()
        self.setTextAlignment(Qt.AlignmentFlag.AlignCenter)
        self.setText(text)
        self.setFont(QFont("Open Sans Bold", 13))
        self.setEditable(False)