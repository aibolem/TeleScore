"""
Author: Ian, TheLittleDoc, Fisk, Dan, Glenn
"""
from PyQt6.QtWidgets import QWidget, QTreeWidgetItem, QPushButton, QComboBox
from PyQt6 import uic
from gm_resources import *
import os, sys

PATH = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
if PATH not in sys.path:
    sys.path.append(PATH)

from .conninst import ConnInst

class ConnMan(QWidget):
    def __init__(self, objectName, parent=None):
        super().__init__(parent)
        path = resourcePath("src/editor/connection/connman.ui")
        uic.loadUi(path, self) # Load the .ui file
        self.buttonToCombo = {} # Dictionary that connects button to the combobox
        self.objectName = objectName
        self.nameList = []  # Will need to change the key to have both name and signal type or else only one receiver would work
        self.initTable(None)

    def initTable(self, data):
        connInst = ConnInst(ConnInst.ADD, self.treeWidget, self.objectName)
        connInst.setAddCall(self.addCallBack)
        self.treeWidget.addTopLevelItem(connInst)
        connInst.exec()

    def addCallBack(self, signal, name):
        if ((name, signal) not in self.nameList):
            connInst = ConnInst(ConnInst.REMOVE, self.treeWidget, name, signal)
            self.treeWidget.addTopLevelItem(connInst)
            connInst.exec()
            connInst.setRemCall(self.remCallBack)
            self.nameList.append((name, signal))

    def remCallBack(self, inst: ConnInst, signal, name):
        self.nameList.remove((name, signal))
        self.treeWidget.takeTopLevelItem(self.treeWidget.indexOfTopLevelItem(inst))

    def getConnections(self) -> list:
        return self.nameList
            




    
