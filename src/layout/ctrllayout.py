"""
Developed By: JumpShot Team
Written by: riscyseven
"""

# This Python file uses the following encoding: utf-8
from PyQt6.QtWidgets import QFrame
from PyQt6.QtCore import QEvent, pyqtSignal, QSize
from PyQt6.QtGui import QDropEvent, QResizeEvent

from layout.abstract_layout.freelayout import FreeLayout
from component.abstractcomp import AbstractComp
from proginterface import ProgInterface

class CtrlLayout(QFrame):
    """
    This class is used to create a scoreboard control
    layout
    """
    dropSignal = pyqtSignal(QDropEvent)

    def __init__(self, projSize=QSize(800, 600), remCallBack=None, parent=None):
        super().__init__(parent)
        self.actualLayout = FreeLayout(projSize)
        self.setLayout(self.actualLayout)
        self.setAcceptDrops(True)
        self.setSize(projSize)
        self.projSize = projSize
        self.compDict = {} # This list should only contain AbstractComp
        self.interface = ProgInterface()
        self.interface.setAllComponent(self.compDict)
        self.remCallBack = remCallBack

    def setRemoveCallBack(self, callback):
        self.remCallBack = callback

    def setSize(self, size: QSize) -> None:
        self.setMinimumSize(size)
        self.projSize = size

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
        component.initRatio(self.projSize, self.size())
        self.compDict[component.objectName()] = component

        self.actualLayout.addWidget(component)

    def removeComponent(self, component: AbstractComp) -> None:
        for i in self.compDict:
            self.compDict[i].getConnection().checkDeletion(component)
        
        self.compDict.pop(component.objectName())
        self.actualLayout.removeWidget(component)
        if (self.remCallBack != None):
            self.remCallBack(component)
        component.setParent(None)
        component.deleteLater()
        component = None

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
            self.compDict[comp].parentResized(self.size())

    def getComponents(self) -> dict:
        return self.compDict

    def getProjSize(self) -> QSize:
        return self.projSize

    def getCurrSize(self) -> QSize:
        return self.size()
