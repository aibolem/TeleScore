"""
Developed By: JumpShot Team
Written by: riscyseven
"""

from PyQt6.QtWidgets import QWidget
from PyQt6 import uic

from editor.connection.conninst import ConnInst
from component.abstractcomp import AbstractComp
from gm_resources import resourcePath

class ConnMan(QWidget):
    def __init__(self, objectName, data, parent=None):
        super().__init__(parent)
        path = resourcePath("src/editor/connection/connman.ui")
        uic.loadUi(path, self) # Load the .ui file
        self.objectName = objectName
        self.connection = data
        self.initTable()

    def initTable(self):
        expanded = self.connection.getData()
        self.A2B = expanded[0]
        self.B2A = expanded[1]

        self.addItem = ConnInst(ConnInst.ADD, self.treeWidget, self.objectName, self.A2B)
        self.addItem.setAddCall(self._addA2BCallBack)
        self.treeWidget.addTopLevelItem(self.addItem)
        self.addItem.exec()

        for type in self.A2B:
            for component in self.A2B[type]:
                self._addA2BCallBack(component, type, True)
 
        for tuple in self.B2A:
            self._addB2ACallBack(tuple[0], tuple[1], True)

    def _addA2BCallBack(self, object: AbstractComp, signal: str, init=False):
        if (object not in self.A2B[signal] or init): # Check to make sure we are not duplicating, assuming signal exists for the connected comp
            connInst = ConnInst(ConnInst.REMOVE, self.treeWidget, object.objectName(), {}, signal)
            self.treeWidget.addTopLevelItem(connInst)
            connInst.exec()
            connInst.setRemCall(self._remA2BCallBack)
            if (init == False):
                self.A2B[signal].append(object)
            self.addItem.removeItem(object.objectName())
            self.connection.dataChanged()

    def _addB2ACallBack(self, object: AbstractComp, signal: str, init=False):
        connInst = ConnInst(ConnInst.REMOVE, self.treeWidget_2, object.objectName(), {}, signal)
        self.treeWidget_2.addTopLevelItem(connInst)
        connInst.exec()
        connInst.setRemCall(self._remB2ACallBack)
        self.connection.dataChanged()

    def _remA2BCallBack(self, object: AbstractComp, signal: str, inst: ConnInst):
        self.A2B[signal].remove(object)
        self.treeWidget.takeTopLevelItem(self.treeWidget.indexOfTopLevelItem(inst))
        self.addItem.addItem(object.objectName())
        self.connection.dataChanged()

    def _remB2ACallBack(self, object: AbstractComp, signal: str, inst: ConnInst):
        self.treeWidget_2.takeTopLevelItem(self.treeWidget_2.indexOfTopLevelItem(inst))
        self.B2A.remove((object, signal))
        self.connection.dataChanged()

            




    
