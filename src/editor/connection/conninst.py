"""
Author: Ian, TheLittleDoc, Fisk, Dan, Glenn
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

    def __init__(self, type, tree, name, signal="", parent=None):
        super().__init__(parent)
        self.type = type
        self.tree = tree
        self.objectName = name
        self.sigComboBox = QComboBox()
        self.recvComboBox = QComboBox()
        self.button = QPushButton()

        self.sigLineEdit = QLineEdit(signal)
        self.sigLineEdit.setEnabled(False)
        self.recvLineEdit = QLineEdit(name)
        self.recvLineEdit.setEnabled(False)
        interface = ProgInterface()
        self.signals = interface.getComponent(self.objectName).getConnection().getSignalTypes()

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

    def exec(self):
        match self.type:
            case self.ADD:
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
        match self.type:
            case self.ADD:
                if (len(self.recvComboBox.currentText()) > 0):
                    self.addCallBack(self.sigComboBox.currentText(), self.recvComboBox.currentText())
            case self.REMOVE:
                self.remCallBack(self, self.sigLineEdit.text(), self.recvLineEdit.text())

    
