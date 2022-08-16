"""
Author: Ian, TheLittleDoc, Fisk, Dan, Glenn
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
        self.timeFormat = "mm:ss"

        self.label = label

        self.clock.timeout.connect(self._clockEvent)

    def getTick(self) -> int:
        return self.tick

    def setTimeFormat(self, value):
        self.timeFormat = value

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
            self.file.outputFile(timeStr)
        self.clkChngedSignal.emit(timeStr)

    def _stopWatch(self):
        self.tick += 1

    def _timer(self):
        if (self.tick <= self.tickTo):
            self.stopClock()
        else:
            self._valueChanged()
            self.tick -= 1

    def setClockTick(self, tick):
        self.tick = tick
        self._valueChanged()

    def addTime(self, min, sec):
        time = QTime(0, min, sec, 0).addSecs(self.tick)
        if (sec < 0):
            time = QTime(0, min, 0, 0).addSecs(self.tick)
            time = time.addMSecs(sec)

        if (min < 0):
            time = QTime(0, 0, sec, 0).addSecs(self.tick)
            time = time.addSecs(min*60)
            
        self.setClockTick(time.hour()*3600+time.minute()*60+time.second())

    def setClockFromStr(self, str) -> bool:
        time = QTime.fromString(str, self.timeFormat)
        self.setClockTick(time.hour()*3600+time.minute()*60+time.second())
        if (not time.isValid()):
            self.setClockTick(0)
        return time.isValid()

    def _clockEvent(self):
        if (self.stopwatch):
            self.stopWatch()
        else:
            self._timer()
        self._valueChanged()
    
    