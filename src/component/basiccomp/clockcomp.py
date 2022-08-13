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
from component.element.clock import Clock
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
        self.clock = Clock(False, self.clockLabel, self)
        self.defaultTime = "00:00"

    def disableWidget(self) -> None:
        # Nothing to implement here since clock is just a label
        pass

    # Override
    def firstTimeProp(self):
        self.properties.appendProperty("Clock Properties", CompAttr.clockProperty)
        self.properties.appendProperty("Connection Properties", CompAttr.connProperty)
        self.connection.appendConnType("Clock Start")
        self.connection.appendConnType("Clock Stop")
        self.connection.appendCallBack("Start", self.start)
        self.connection.appendCallBack("Stop", self.stop)
        self.connection.appendCallBack("Reset", self.reset)
        self.connection.appendCallBack("Set Time", self.setTime)

    def debug(self):
        self.clock.debug()

    def start(self):
        self.clock.startClock()

    def stop(self):
        self.clock.stopClock()

    def setTime(self, value):
        self.clock.setClockFromStr(value)

    def reset(self):
        self.clock.setClockFromStr(self.defaultTime)

    # Override
    def getName(self) -> str:
        return "Time Display"

    # Override
    def reloadProperty(self) -> None:
        self.properties["Default Time"] = self.defaultTime
        self.properties["Format"] = self.clock.getTimeFormat()

    def reconfProperty(self) -> None:
        self.defaultTime = self.properties["Default Time"]
        self.clock.setTimeFormat(self.properties["Format"])
        
        if (not self.clock.setClockFromStr(self.defaultTime)):
            info = GMessageBox("Default Time Invalid", "Please reenter the time", "Info")
            info.exec()