"""
Author: Ian, TheLittleDoc, Fisk, Dan, Glenn
"""

from PyQt6.QtWidgets import QWidget
from PyQt6.QtGui import QIcon, QFont, QStandardItem, QColor
from PyQt6.QtCore import Qt, QSize
from .propwidgethead import PropWidgetHead
from gm_resources import *

class PropWidgetItem(QStandardItem):
    """
    Each component listed in the component list is made from 
    this class object. This widget item will standardize attributes
    such as the fonts, icon image size, etc.
    """

    def __init__(self, parent: PropWidgetHead, text="Default"):
        """
        Consturctor for a component list item

        :param icon: Icon for the component
        :param parent: Header/category of the item
        :param treeWidget: Main component list widget
        :param text: Description of the component

        :return: none
        """
        super().__init__(parent) # This sets this component to be the subcomponent of the header
        self.role = Qt.ItemDataRole.DisplayRole; # All the items are for displaying
        self.setText(text)
        self.setTextAlignment(Qt.AlignmentFlag.AlignCenter | Qt.AlignmentFlag.AlignVCenter)
        self.setFont(QFont("Open Sans Bold", 11))
        self.setBackground(QColor(255, 255, 255))
        #self.setSizeHint(QSize(1000000, 50))
        
    def setEditWidget(self, widget:QWidget) -> None:
        self.editWidget = widget
