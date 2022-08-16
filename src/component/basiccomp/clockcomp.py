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

    clockProperty = {
        "Stopwatch": {
            CompAttr.TYPE: CompAttr.CHECKBOX,
            CompAttr.VALUE: False
        },
        "Format": {
            CompAttr.TYPE: CompAttr.TEXTEDIT,
            CompAttr.VALUE: "mm:ss"
        },
        "Default Time": {
            CompAttr.TYPE: CompAttr.TEXTEDIT,
            CompAttr.VALUE: "00:00"
        }
    }

    def __init__(self, edit=False, parent=None):
        super().__init__(parent)
        path = resourcePath("src/component/basiccomp/clockcomp.ui")
        uic.loadUi(path, self) # Load the .ui file
        self.clock = Clock(False, self.clockLabel, self.fileOut, self)
        self.defaultTime = "00:00"

        self._initConn()

    def disableWidget(self) -> None:
        # Nothing to implement here since clock is just a label
        pass

    # Override
    def firstTimeProp(self):
        self.properties.appendProperty("File Properties", CompAttr.fileProperty)
        self.properties["File Output Location"] = self.properties["File Output Location"].format(self.objectName())
        self.fileOut.setOutputFile(self.properties["File Output Location"])
        self.fileOut.outputFile("")
        self.properties.appendProperty("Clock Properties", self.clockProperty)
        self.properties.appendProperty("Connection Properties", CompAttr.connProperty)

    def _initConn(self):
        self.connection.appendConnType("Clock Start")
        self.connection.appendConnType("Clock Stop")
        self.connection.appendCallBack("Start", self._start)
        self.connection.appendCallBack("Stop", self._stop)
        self.connection.appendCallBack("Reset", self._reset)
        self.connection.appendCallBack("Set Time", self._setTime)

        self.connection.appendCallBack("ADDS", self._addSec)
        self.connection.appendCallBack("ADDM", self._addMin)
        self.connection.appendCallBack("SUBS", self._subSec)
        self.connection.appendCallBack("SUBM", self._subMin)

    def _start(self):
        self.clock.startClock()

    def _stop(self):
        self.clock.stopClock()

    def _setTime(self, value):
        self.clock.setClockFromStr(value)

    def _reset(self):
        self.clock.setClockFromStr(self.defaultTime)

    def _addSec(self):
        self.clock.addTime(0, 1)

    def _addMin(self):
        self.clock.addTime(1, 0)

    def _subSec(self):
        self.clock.addTime(0, -1)

    def _subMin(self):
        self.clock.addTime(-1, 0)

    # Override
    def getName(self) -> str:
        return "Time Display"

    # Override
    def reloadProperty(self) -> None:
        self.properties["Default Time"] = self.defaultTime
        self.properties["Format"] = self.clock.getTimeFormat()
        self.properties["File Output Location"] = self.fileOut.getOutputFile()

    def reconfProperty(self) -> None:
        self.defaultTime = self.properties["Default Time"]
        self.fileOut.setOutputFile(self.properties["File Output Location"])
        self.clock.setTimeFormat(self.properties["Format"])
        
        if (not self.clock.setClockFromStr(self.defaultTime)):
            info = GMessageBox("Default Time Invalid", "Please reenter the time", "Info")
            info.exec()