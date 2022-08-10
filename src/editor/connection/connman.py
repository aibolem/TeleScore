"""
Author: Ian, TheLittleDoc, Fisk, Dan, Glenn
"""
from PyQt6.QtWidgets import QWidget
from PyQt6 import uic
from gm_resources import *
import os, sys

PATH = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
if PATH not in sys.path:
    sys.path.append(PATH)

from editor.connection.conninst import ConnInst
from component.abstractcomp import AbstractComp

class ConnMan(QWidget):
    def __init__(self, objectName, data, callBack, parent=None):
        super().__init__(parent)
        path = resourcePath("src/editor/connection/connman.ui")
        uic.loadUi(path, self) # Load the .ui file
        self.buttonToCombo = {} # Dictionary that connects button to the combobox
        self.objectName = objectName
        self.A2BList = []
        self.B2AList = []
        self.callBack = callBack
        self.initTable(data)

    def initTable(self, data):
        connInst = ConnInst(ConnInst.ADD, self.treeWidget, self.objectName)
        connInst.setAddCall(self._addA2BCallBack)
        self.treeWidget.addTopLevelItem(connInst)
        connInst.exec()
        # Assumption: List is formatted as tuple [(Component, Signal)]

        for i in data[0]:
            self._addA2BCallBack(i[1], i[0], True)
 
        for i in data[1]:
            self._addB2ACallBack(i[1], i[0])
            connInst.exec()

    def _addA2BCallBack(self, object: AbstractComp, signal: str, init=False):
        if ((object, signal) not in self.A2BList):
            connInst = ConnInst(ConnInst.REMOVE, self.treeWidget, object.objectName(), signal)
            self.treeWidget.addTopLevelItem(connInst)
            connInst.exec()
            connInst.setRemCall(self._remA2BCallBack)
            self.A2BList.append((object, signal))
            if (init == False):
                self.callBack((self.A2BList, self.B2AList))

    def _addB2ACallBack(self, object: AbstractComp, signal: str):
        connInst = ConnInst(ConnInst.REMOVE, self.treeWidget_2, object.objectName(), signal)
        self.treeWidget_2.addTopLevelItem(connInst)
        connInst.exec()
        connInst.setRemCall(self._remB2ACallBack)
        self.B2AList.append((object, signal))

    def _remA2BCallBack(self, object: AbstractComp, signal: str, inst: ConnInst):
        self.A2BList.remove((object, signal))
        self.treeWidget.takeTopLevelItem(self.treeWidget.indexOfTopLevelItem(inst))
        self.callBack((self.A2BList, self.B2AList))

    def _remB2ACallBack(self, object: AbstractComp, signal: str, inst: ConnInst):
        self.treeWidget_2.takeTopLevelItem(self.treeWidget_2.indexOfTopLevelItem(inst))
        self.B2AList.remove((object, signal))
        self.callBack((self.A2BList, self.B2AList))

    def getConnections(self) -> list:
        return (self.A2BList, self.B2AList)

            




    
