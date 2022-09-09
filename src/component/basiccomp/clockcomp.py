"""
Developed by: JumpShot Team
Written by: riscyseven
UI designed by: Fisk31
"""

from PyQt6.QtMultimedia import QMediaPlayer, QAudioOutput, QMediaDevices
from PyQt6.QtCore import QUrl

from attr import CompAttr
from component.abstractcomp import AbstractComp
from component.element.clock import Clock
from fileio.fileout import TextOut
from gm_resources import GMessageBox

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
        },
        "Clr file when time = 0": {
            CompAttr.TYPE: CompAttr.CHECKBOX,
            CompAttr.VALUE: False
        },
        "Buzzer Sound": {
            CompAttr.TYPE: CompAttr.FLOPEN,
            CompAttr.VALUE: ""
        }
    }

    def __init__(self, objectName, edit=False, parent=None):
        super().__init__(objectName, "src/component/basiccomp/clockcomp.ui", edit, parent)

        self.fileOut = TextOut(parent=self)
        self.fileOut.setOutputFile(self.properties["File Output Location"])
        self.clock = Clock(False, self.clockLabel, self.fileOut, self)
        self.clock.setStopCallback(self._stopCallback)
        self.defaultTime = "00:00"
        self.buzzAudio = None
        self._initConn()

    # Override
    def _firstTimeProp(self):
        self.properties.appendProperty("File Properties", CompAttr.fileProperty)
        self.properties["File Output Location"] = self.properties["File Output Location"].format(self.objectName())
        self.properties.appendProperty("Clock Properties", self.clockProperty)
        self.properties.appendProperty("Connection Properties", CompAttr.connProperty)

    # Override
    def getName(self) -> str:
        return "Time Display"

    # Override
    def _reloadProperty(self) -> None:
        self.properties["Default Time"] = self.defaultTime
        self.properties["Format"] = self.clock.getTimeFormat()
        self.properties["File Output Location"] = self.fileOut.getOutputFile()
        if (self.buzzAudio == None):
            self.properties["Buzzer Audio"] = ""
        else:
            self.properties["Buzzer Audio"] = self.buzzAudio.source().fileName()

    # Override
    def _reconfProperty(self) -> None:
        self.defaultTime = self.properties["Default Time"]
        self.fileOut.setOutputFile(self.properties["File Output Location"])
        if (self.fileOut.getOutputFile() != self.properties["File Output Location"]):
            self.attrChanged.emit()
        self.clock.setTimeFormat(self.properties["Format"])
        self.clock.setStopWatch(self.properties["Stopwatch"])
        self.clock.setClearTimeZero(self.properties["Clr file when time = 0"])
        if (self.properties["Buzzer Sound"] != ""):
            self.audioOutput = QAudioOutput(QMediaDevices.defaultAudioOutput())
            self.audioOutput.setVolume(100)
            self.buzzAudio = QMediaPlayer()
            self.buzzAudio.setAudioOutput(self.audioOutput)
            self.buzzAudio.setSource(QUrl.fromLocalFile(self.properties["Buzzer Sound"]))
        else:
            self.audioOutput = None
            self.buzzAudio = None
        
        if (not self.clock.setClockFromStr(self.defaultTime)):
            info = GMessageBox("Default Time Invalid", "Please check your time format", "Info")
            info.exec()

    # Override
    def setFileDir(self, dirName):
        self.properties["File Output Location"] = dirName.format(self.objectName())
        self.fileOut.setOutputFile(self.properties["File Output Location"])

    def _initConn(self):
        self.connection.appendConnType("Clock Stop")
        self.connection.appendCallBack("Start", self._start)
        self.connection.appendCallBack("Stop", self._stop)
        self.connection.appendCallBack("Reset", self._reset)
        self.connection.appendCallBack("Set Time", self._setTime)

        self.connection.appendCallBack("ADDS", self._addSec)
        self.connection.appendCallBack("ADDM", self._addMin)
        self.connection.appendCallBack("SUBS", self._subSec)
        self.connection.appendCallBack("SUBM", self._subMin)
        self.connection.appendCallBack("Clock Stop", self._stop)

    def _start(self):
        self.clock.startClock()

    def _stop(self):
        self.clock.stopClock()

    def _setTime(self, value):
        self.clock.setClockFromStr(value)

    def _reset(self):
        self.clock.setClockFromStr(self.defaultTime)
        if (self.buzzAudio != None):
            self.buzzAudio.stop()

    def _addSec(self):
        self.clock.addTime(0, 1)

    def _addMin(self):
        self.clock.addTime(1, 0)

    def _subSec(self):
        self.clock.addTime(0, -1)

    def _subMin(self):
        self.clock.addTime(-1, 0)

    def _stopCallback(self):
        if (self.buzzAudio != None):
            self.buzzAudio.play()
        self.connection.emitSignal("Clock Stop")