"""
Author: Ian, TheLittleDoc, Fisk, Dan, Glenn
"""

from PyQt6 import uic
from ..abstractcomp import AbstractComp
from gm_resources import *


class ClockSetComp(AbstractComp):
    """
    CLock widget for scoreboard.

    This class has one clock object from the backend.
    """

    def __init__(self, parent=None):
        super().__init__(parent)
        path = resourcePath("src/component/basiccomp/clocksetcomp.ui")
        uic.loadUi(path, self) # Load the .ui file

    def disableWidget(self) -> None:
        # Nothing to implement here since clock is just a label
        pass

    # Override
    def getName(self) -> str:
        return "Time Type Amount"