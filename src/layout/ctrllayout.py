"""
Author: Ian, TheLittleDoc, Fisk, Dan, Glenn
"""

# This Python file uses the following encoding: utf-8
from PyQt6.QtWidgets import QFrame
from PyQt6.QtCore import QEvent, QRect, pyqtSignal, QSize
from PyQt6.QtGui import QDropEvent, QResizeEvent
import os, sys

PATH = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
if PATH not in sys.path:
    sys.path.append(PATH)

from .abstract_layout.freelayout import FreeLayout
from component.abstractcomp import AbstractComp
from proginterface import ProgInterface

class CtrlLayout(QFrame):
    """
    This class is used to create a scoreboard control
    layout
    """
    dropSignal = pyqtSignal(QDropEvent)

    def __init__(self, projSize=QSize(800, 600), parent=None):
        super().__init__(parent)
        self.actualLayout = FreeLayout()
        self.actualLayout.setGeometry(QRect(0, 0, self.width(), self.height()))
        self.setLayout(self.actualLayout)
        self.setAcceptDrops(True)
        self.setSize(projSize)
        self.projSize = projSize
        self.setStyleSheet("background-color: white;")
        self.compDict = {} # This list should only contain AbstractComp
        self.interface = ProgInterface()
        self.interface.setAllComponent(self.compDict)


    def setSize(self, size: QSize) -> None:
        self.setMinimumSize(size)

    def defaultSize(self):
        return self.projSize

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
        component.sizeInit(self.projSize)
        self.compDict[component.objectName()] = component
        self.actualLayout.addWidget(component)

    def removeComponent(self, component: AbstractComp) -> None:
        for i in self.compDict:
            self.compDict[i].getConnections().checkDeletion(component.objectName())
        
        self.compDict.pop(component.objectName())
        self.actualLayout.removeWidget(component)

    def dragEnterEvent(self, evt) -> None:
        """
        Method is called when anything dragged is entered.

        :param evt: event
        :return: none
        """
        if (evt.mimeData().hasFormat("application/x-comp")):
            evt.setAccepted(True)
            evt.acceptProposedAction()
            evt.accept()

    def count(self) -> int:
        return self.actualLayout.count()

    def dropEvent(self, evt) -> None:
        self.dropSignal.emit(evt)

    def resizeEvent(self, event: QResizeEvent) -> None:
        for comp in self.compDict:
            self.compDict[comp].parentResizeEvent(event.size())
