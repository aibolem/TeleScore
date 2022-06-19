import os

from PyQt6 import QtWidgets, uic
from PyQt6.QtCore import QRect
from gm_resources import *
from layout import ctrllayout

class Editor(QtWidgets.QMainWindow):
    def __init__(self, *args):
        super().__init__(*args) # Call the inherited classes __init__ method
        path = resourcePath("src\\window\\ui\\editor.ui")
        uic.loadUi(path, self) # Load the .ui file

        ctrl = ctrllayout.CtrlLayout(self)
        ctrl.setGeometry(QRect(0,0,1000,1000))
        self.setCentralWidget(ctrl)
