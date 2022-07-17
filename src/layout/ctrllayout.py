"""
Author: Ian, TheLittleDoc
"""

# This Python file uses the following encoding: utf-8
from turtle import width
from PyQt6.QtWidgets import QFrame
from PyQt6.QtCore import QEvent, QRect
import os, sys

PATH = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
if PATH not in sys.path:
    sys.path.append(PATH)

from .abstract_layout.freelayout import FreeLayout
from component.basiccomp.buttoncomp import ButtonComp
from component.abstractcomp import AbstractComp

class CtrlLayout(QFrame):
    """
    This class is used to create a scoreboard control
    layout
    """

    def __init__(self, parent=None):
        super().__init__(parent)
        self.actualLayout = FreeLayout()
        self.actualLayout.setGeometry(QRect(0, 0, self.width(), self.height()))
        self.setLayout(self.actualLayout)

    def resizeEvent(self, event: QEvent) -> None:
        """
        Anytime the control layout is resized, 
        this is called.

        :param event: QResizeEvent information 
        :return: none
        """
        self.actualLayout.resizeEvent(event)
        
    def addComponent(self, component: AbstractComp) -> None:
        """
        Method that adds component to the layout.
        :param component: AbstractComp, a component to add
        :return: none
        """
        pass

    def test(self):
        for i in range(0, 500, 10):
            item = ButtonComp()
            item.setGeometry(10+i, 10+i, 30, 30)
            self.actualLayout.addComponent(item, self.size())


