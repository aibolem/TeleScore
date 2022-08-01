"""
Author: Ian, TheLittleDoc, Fisk, Dan, Glenn
"""

from PyQt6 import uic
from PyQt6.QtCore import pyqtSlot
from ..abstractcomp import AbstractComp
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

    # Override
    def firstTimeProp(self) -> None:
        pass

    def disableWidget(self) -> None:
        # Nothing to implement here since clock is just a label
        pass

    def getPropertyTab(self) -> list:
        pass

    # Override
    def getName(self) -> str:
        return "Time Type Amount"

    @pyqtSlot()
    def propChanged(self) -> None:
        pass