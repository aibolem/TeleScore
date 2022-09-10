"""
Developed by: JumpShot Team
Written by: riscyseven
"""

from email.policy import default
from os import times
from PyQt6.QtCore import QObject, pyqtSignal, QTimer, QTime
from PyQt6.QtWidgets import QLabel

from fileio.fileout import TextOut

class Clock(QObject):
    """
    Class that implements a basic clock (timer or stopwatch),
    Utitlizes QTimer for the clock to update. 
    For cleaner code, QTimer is updated every milliseconds
    instead of seconds.
    """

    clkChngedSignal = pyqtSignal(str) # Signal/Callback for when clock is changed

    def __init__(self, stopwatch=False, label: QLabel=None, file:TextOut=None, parent=None):
        """
        """
        super(QObject, self).__init__(parent)
        self.tick = 0
        self.clock = QTimer()
        self.speed = 1000
        self.tickTo = 0
        self.stopwatch = stopwatch
        self.file = file
        self.clearZero = False
        self.carryOver = False
        self.timeFormat = "mm:ss"

        self.label = label
        self.clearTimeZero = False

        self.clock.timeout.connect(self._clockEvent)
        
    def setStopCallback(self, callback):
        self.setStopCallback = callback

    def getTick(self) -> int:
        return self.tick

    def setTimeFormat(self, value):
        if (value.lower().count("h") > 0):
            self.carryOver = True
        else:
            self.carryOver = False
        self.timeFormat = value

    def setStopWatch(self, value: bool):
        self.stopwatch = value

    def getTimeFormat(self):
        return self.timeFormat

    def stopClock(self):
        self.clock.stop()

    def startClock(self):
        self.clock.start(self.speed)

    def startStopClock(self):
        if (self.clock.isActive()):
            self.clock.stop()
        else:
            self.clock.start(self.speed)

    def _valueChanged(self):
        # Potential issue for soccer clock, 60:00 -> 1 hour
        timeStr = self._convTicktoStr(self.tick, self.timeFormat)

        if (self.label != None):
            self.label.setText(timeStr)
        if (self.file != None):
            if (self.clearTimeZero and self.tick <= 0):
                timeStr = ""
            self.file.outputFile(timeStr)
        self.clkChngedSignal.emit(timeStr)

    def _stopWatch(self):
        self.tick += 1
        self._valueChanged()

    def _timer(self):
        self.tick -= 1

        if (self.tick < self.tickTo):
            self.tick = self.tickTo
            self._valueChanged()
            if (self.setStopCallback != None):  # Refractor this in the future
                self.setStopCallback()
            self.stopClock()
        else:
            self._valueChanged()

    def setClockTick(self, tick):
        if (tick >= 0 and tick < 86400):
            self.tick = tick
            self._valueChanged()

    def addTime(self, min, sec):
        tempTick = self.tick + min * 60 + sec
        self.setClockTick(tempTick)

    def setClockFromStr(self, str, timeFormat=None) -> bool:
        if (timeFormat == None):
            timeFormat = self.timeFormat
        time = QTime.fromString(str, timeFormat)
        if (time.isValid()):
            self.setClockTick(time.hour()*3600+time.minute()*60+time.second())
        else:
            self._valueChanged()
        return time.isValid()

    def setClearTimeZero(self, value):
        self.clearTimeZero = value

    def _clockEvent(self):
        if (self.stopwatch):
            self._stopWatch()
        else:
            self._timer()
    
    def _convTicktoStr(self, tick: int, timeFormat: str) -> str:
        sec = tick % 60
        min = (tick // 60) % 60
        if (not self.carryOver):
            min = (tick // 60)
        hour = (tick // 3600) % 24

        lastPos = 0
        currPos = 0
        currChar = ''
        newStr = ""
        timeFormat += " "
        for i in timeFormat:
            if (currChar != i):
                match currChar:
                    case "h":
                        newStr += ("{:0" + str(currPos-lastPos) + "d}").format(hour)
                    case "m":
                        newStr += ("{:0" + str(currPos-lastPos) + "d}").format(min)
                    case "s":
                        newStr += ("{:0" + str(currPos-lastPos) + "d}").format(sec)
                    case _:
                        newStr += currChar
                currChar = i
                lastPos = currPos
            currPos += 1

        return newStr