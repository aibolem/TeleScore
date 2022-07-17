"""
Author: Ian, TheLittleDoc, Fisk, Dan, Glenn
"""

from PyQt6.QtWidgets import QMainWindow, QFrame
from PyQt6 import uic, QtGui
from PyQt6.QtCore import QPoint, pyqtSlot
from gm_resources import *
from layout import ctrllayout

from editor.complisttab import CompListTab
from editor.propertytab import PropertyTab
from editor.command.insertcmd import InsertCmd

class Editor(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent) # Call the inherited classes __init__ method
        path = resourcePath("src\\window\\ui\\editor.ui")
        uic.loadUi(path, self) # Load the .ui file
        self.cmdStack = []
        self.ctrl = ctrllayout.CtrlLayout()
        self.ctrl.dropSignal.connect(self.dropSlot)
        self._initUI()
        

    def _initUI(self):
        self.comp = CompListTab()
        self.compDock.setWidget(self.comp)

        self.prop = PropertyTab()
        self.propDock.setWidget(self.prop)

        self.ctrl.setMinimumSize(800, 600)
        self.ctrl.setFrameShape(QFrame.Shape.Box)
        self.setCentralWidget(self.ctrl)

    @pyqtSlot(QtGui.QDropEvent)
    def dropSlot(self, evt: QtGui.QDropEvent) -> None:
        """
        
        """
        type = evt.mimeData().data("application/x-comp")
        point = QPoint(int(evt.position().x()), int(evt.position().y()))
        insert = InsertCmd(self.ctrl, type, point, "")
        insert.execute()
        self.cmdStack.append(insert)