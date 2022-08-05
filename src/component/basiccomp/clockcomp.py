"""
Author: Ian, TheLittleDoc, Fisk, Dan, Glenn
"""

from ..property import Property

import os, sys

PATH = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
if PATH not in sys.path:
    sys.path.append(PATH)

from attr import CompAttr
from PyQt6 import uic
from PyQt6.QtCore import pyqtSlot
from ..abstractcomp import AbstractComp
from ..element.clock import Clock
from gm_resources import *


class ClockComp(AbstractComp):
    """
    CLock widget for scoreboard.

    This class has one clock object from the backend.
    """

    def __init__(self, layout, edit=False, parent=None):
        super().__init__(parent)
        path = resourcePath("src/component/basiccomp/clockcomp.ui")
        uic.loadUi(path, self) # Load the .ui file
        self.clock = Clock(label=self.clockLabel) 

    def disableWidget(self) -> None:
        # Nothing to implement here since clock is just a label
        pass

    # Override
    def firstTimeProp(self):
        self.properties.appendProperty("Clock Properties", CompAttr.clockProperty)
        self.properties.appendProperty("Connection Properties", CompAttr.connProperty)
        self.connection.appendSignalType("Clock Start")
        self.connection.appendSignalType("Clock Stop")
        self.connection.appendReceiverType("Start", self.start)
        self.connection.appendReceiverType("Stop", self.stop)
        self.connection.appendReceiverType("Reset", self.reset)

    def start(self):
        self.clock.startTimer()

    def stop(self):
        self.clock.stopClock()

    def reset(self):
        pass

    # Override
    def getName(self) -> str:
        return "Time Display"

    # Override
    def reloadProperty(self) -> None:
        pass

    def reconfProperty(self) -> None:
        pass