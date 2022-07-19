"""
Author: Ian, TheLittleDoc, Fisk, Dan, Glenn
"""

from PyQt6 import uic
from ..abstractcomp import AbstractComp
from ..element.clock import Clock
from gm_resources import *


class ClockComp(AbstractComp):
    """
    CLock widget for scoreboard.

    This class has one clock object from the backend.
    """

    def __init__(self, edit=False, parent=None):
        super().__init__(parent)
        path = resourcePath("src/component/basiccomp/clockcomp.ui")
        uic.loadUi(path, self) # Load the .ui file
        self.clock = Clock(label=self.clockLabel) 

    def disableWidget(self) -> None:
        # Nothing to implement here since clock is just a label
        pass

    # Override
    def getName(self) -> str:
        return "Time Display"