"""
Author: Ian, TheLittleDoc, Fisk, Dan, Glenn
"""

from PyQt6.QtWidgets import QMainWindow, QFrame
from PyQt6 import uic
from gm_resources import *
from layout import ctrllayout

from editor.complisttab import CompListTab
from editor.propertytab import PropertyTab

class Editor(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent) # Call the inherited classes __init__ method
        path = resourcePath("src\\window\\ui\\editor.ui")
        uic.loadUi(path, self) # Load the .ui file
        self.initUI()
        self.cmdHistory = []

    def initUI(self):
        self.comp = CompListTab()
        self.compDock.setWidget(self.comp)

        self.prop = PropertyTab()
        self.propDock.setWidget(self.prop)

        ctrl = ctrllayout.CtrlLayout()
        ctrl.setMinimumSize(800, 600)
        ctrl.setFrameShape(QFrame.Shape.Box)
        self.setCentralWidget(ctrl)

        self.setAcceptDrops(True)

    def dragEnterEvent(self, evt):
        if (evt.mimeData().hasFormat("application/x-comp")):
            evt.setAccepted(True)
            evt.acceptProposedAction()
            evt.accept()

