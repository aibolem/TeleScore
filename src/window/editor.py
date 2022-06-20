import os

from PyQt6.QtWidgets import QMainWindow, QFrame
from PyQt6 import uic
from PyQt6.QtCore import QRect
from gm_resources import *
from layout import ctrllayout

PATH = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
if PATH not in sys.path:
    sys.path.append(PATH)

from editor.complist import CompList

class Editor(QMainWindow):
    def __init__(self, *args):
        super().__init__(*args) # Call the inherited classes __init__ method
        path = resourcePath("src\\window\\ui\\editor.ui")
        uic.loadUi(path, self) # Load the .ui file

        self.comp = CompList()
        self.compDock.setWidget(self.comp);

        ctrl = ctrllayout.CtrlLayout()
        ctrl.setMinimumSize(800, 600)
        ctrl.setFrameShape(QFrame.Shape.Box)
        self.setCentralWidget(ctrl)

