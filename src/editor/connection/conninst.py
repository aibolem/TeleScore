"""
Developed By: JumpShot Team
Written by: riscyseven
"""

import os, sys

from PyQt6.QtWidgets import QTreeWidgetItem, QPushButton, QComboBox, QLineEdit

PATH = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
if PATH not in sys.path:
    sys.path.append(PATH)

from proginterface import ProgInterface

class ConnInst(QTreeWidgetItem):
    ADD = 0
    REMOVE = 1

    def __init__(self, type, tree, objectName, addedCompDict={}, signal=""):
        super().__init__()
        self.instType = type
        self.tree = tree
        self.objectName = objectName
        self.addedCompDict = addedCompDict
        self.button = QPushButton()

        if (type == self.REMOVE):
            self.sigLineEdit = QLineEdit(signal)
            self.sigLineEdit.setEnabled(False)
            self.recvLineEdit = QLineEdit(objectName)
            self.recvLineEdit.setEnabled(False)
        
        interface = ProgInterface()
        self.object = interface.getComponent(objectName)
        self.signals = self.object.getConnection().getSignalTypes()

    def _loadCombo(self):
        interface = ProgInterface()

        compDict = interface.getAllComponent()

        for i in self.signals:
            self.sigComboBox.addItem(i)

        if (len(self.signals) <= 1):
            self.sigComboBox.setDisabled(True)

        for i in compDict:
            recvType = compDict[i].getConnection().getRecvTypes()
            check = any(item in self.signals for item in recvType)
            if (i != self.objectName and check):
                self.recvComboBox.addItem(i)

    def setAddCall(self, callback):
        self.addCallBack = callback
    
    def setRemCall(self, callback):
        self.remCallBack = callback

    def removedComp(self):
        if (self.type == self.ADD):
            self.recvComboBox.clear()
            self._loadCombo()

    def exec(self):
        match self.instType:
            case self.ADD:
                self.sigComboBox = QComboBox()
                self.recvComboBox = QComboBox()
                self.tree.setItemWidget(self, 0, self.button)
                self.tree.setItemWidget(self, 1, self.sigComboBox)
                self.tree.setItemWidget(self, 2, self.recvComboBox)
                self.button.setText("+ ADD")
                self._loadCombo()
            case self.REMOVE:
                self.tree.setItemWidget(self, 0, self.button)
                self.tree.setItemWidget(self, 1, self.sigLineEdit)
                self.tree.setItemWidget(self, 2, self.recvLineEdit)
                self.button.setText("- REMOVE")

        self.button.clicked.connect(self.buttonClicked)

    def buttonClicked(self):
        interface = ProgInterface()
        match self.instType:
            case self.ADD:
                if (len(self.recvComboBox.currentText()) > 0):
                    self.addCallBack(interface.getComponent(self.recvComboBox.currentText()), self.sigComboBox.currentText())
            case self.REMOVE:
                self.remCallBack(interface.getComponent(self.recvLineEdit.text()), self.sigLineEdit.text(), self)

    def removeItem(self, objName):
        if (self.instType == self.ADD):
            self.recvComboBox.removeItem(self.recvComboBox.findText(objName))
    
    def addItem(self, objName):
        if (self.instType == self.ADD):
            self.recvComboBox.addItem(objName)