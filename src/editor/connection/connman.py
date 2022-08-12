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
        self.callBack = callBack
        self.initTable(data)

    def initTable(self, data):
        connInst = ConnInst(ConnInst.ADD, self.treeWidget, self.objectName)
        connInst.setAddCall(self._addA2BCallBack)
        self.treeWidget.addTopLevelItem(connInst)
        connInst.exec()
        self.A2B = data[0]
        self.B2A = data[1]
        for type in self.A2B:
            for component in self.A2B[type]:
                self._addA2BCallBack(component, type, True)
 
        for tuple in self.B2A:
            self._addB2ACallBack(tuple[0], tuple[1], True)
            connInst.exec()

    def _addA2BCallBack(self, object: AbstractComp, signal: str, init=False):
        if (object not in self.A2B[signal] or init): # Check to make sure we are not duplicating, assuming signal exists for the connected comp
            connInst = ConnInst(ConnInst.REMOVE, self.treeWidget, object.objectName(), signal)
            self.treeWidget.addTopLevelItem(connInst)
            connInst.exec()
            connInst.setRemCall(self._remA2BCallBack)
            if (init == False):
                self.A2B[signal].append(object)
                self.callBack()

    def _addB2ACallBack(self, object: AbstractComp, signal: str, init=False):
        connInst = ConnInst(ConnInst.REMOVE, self.treeWidget_2, object.objectName(), signal)
        self.treeWidget_2.addTopLevelItem(connInst)
        connInst.exec()
        connInst.setRemCall(self._remB2ACallBack)
        #if (init == False):
            #self.B2A.append((object, signal))

    def _remA2BCallBack(self, object: AbstractComp, signal: str, inst: ConnInst):
        self.A2B[signal].remove(object)
        self.treeWidget.takeTopLevelItem(self.treeWidget.indexOfTopLevelItem(inst))
        self.callBack()

    def _remB2ACallBack(self, object: AbstractComp, signal: str, inst: ConnInst):
        self.treeWidget_2.takeTopLevelItem(self.treeWidget_2.indexOfTopLevelItem(inst))
        self.B2A.remove((object, signal))
        self.callBack()

            




    
