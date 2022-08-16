"""
Author: Ian, TheLittleDoc, Fisk, Dan, Glenn
"""

import os, sys
from PyQt6 import uic

PATH = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
if PATH not in sys.path:
    sys.path.append(PATH)

from attr import CompAttr
from component.abstractcomp import AbstractComp
from gm_resources import *

class ClockSetComp(AbstractComp):
    """
    CLock widget for scoreboard.

    This class has one clock object from the backend.
    """

    def __init__(self, edit=False, parent=None):
        super().__init__(parent)
        path = resourcePath("src/component/basiccomp/clocksetcomp.ui")
        uic.loadUi(path, self) # Load the .ui file

        if (edit == True):
            self.lineEdit.installEventFilter(self)
            self.pushButton.installEventFilter(self)

        self.pushButton.pressed.connect(self.pressed)

    # Override
    def firstTimeProp(self) -> None:
        self.properties.appendProperty("Connection Properties", CompAttr.connProperty)
        self.connection.appendConnType("Set Time")

    def disableWidget(self) -> None:
        # Nothing to implement here since clock is just a label
        pass

    def reloadProperty(self) -> None:
        pass

    # Override
    def getName(self) -> str:
        return "Time Type Amount"

    def reconfProperty(self) -> None:
        pass

    def pressed(self):
        self.connection.emitSignal("Set Time", self.lineEdit.text())