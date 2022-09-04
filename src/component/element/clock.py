"""
Developed by: JumpShot Team
Written by: riscyseven
"""

from PyQt6.QtCore import QObject, pyqtSignal, QTimer, QTime
from PyQt6.QtWidgets import QLabel

class Clock(QObject):
    """
    Class that implements a basic clock (timer or stopwatch),
    Utitlizes QTimer for the clock to update. 
    For cleaner code, QTimer is updated every milliseconds
    instead of seconds.
    """

    clkChngedSignal = pyqtSignal(str)    # Signal/Callback for when clock is changed

    def __init__(self, stopwatch=False, label: QLabel=None, file=None, parent=None):
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
        self.timeFormat = "mm:ss"

        self.label = label
        self.clearTimeZero = False

        self.clock.timeout.connect(self._clockEvent)

    def setStopCallback(self, callback):
        self.setStopCallback = callback

    def getTick(self) -> int:
        return self.tick

    def setTimeFormat(self, value):
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
        timeStr = QTime(0, 0, 0, 0).addSecs(self.tick).toString(self.timeFormat)
        
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
        self._valueChanged()
        self.tick -= 1

        if (self.tick <= self.tickTo):
            if (self.setStopCallback != None):  # Refractor this in the future
                self.setStopCallback()
                self.tick = self.tickTo
            self.stopClock()

    def setClockTick(self, tick):
        if (tick >= 0 and tick < 86400):
            self.tick = tick
            self._valueChanged()

    def addTime(self, min, sec):
        tempTick = self.tick + min * 60 + sec
        self.setClockTick(tempTick)

    def setClockFromStr(self, str) -> bool:
        time = QTime.fromString(str, self.timeFormat)
        self.setClockTick(time.hour()*3600+time.minute()*60+time.second())
        if (not time.isValid()):
            self.setClockTick(0)
        return time.isValid()

    def setClearTimeZero(self, value):
        self.clearTimeZero = value

    def _clockEvent(self):
        if (self.stopwatch):
            self._stopWatch()
        else:
            self._timer()
        self._valueChanged()
    
    