from PyQt6.QtWidgets import QLabel, QPushButton
from PyQt6 import uic
from ..abstractcomp import AbstractComp
from ..element.clock import Clock
from gm_resources import *


class ClockComp(AbstractComp):
    """
    CLock widget for scoreboard.

    This class has one clock object from the backend.
    """

    def __init__(self):
        super().__init__(self)
        path = resourcePath("src/component/basiccomp/clockcomp.ui")
        uic.loadUi(path, self) # Load the .ui file
        self.clock = Clock(label=self.clockLabel) 

    def disableWidget(self):
        # Nothing to implement here since clock is just a label
        pass