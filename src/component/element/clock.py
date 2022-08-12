"""
Author: Ian, TheLittleDoc, Fisk, Dan, Glenn
"""

from PyQt6.QtCore import QObject, pyqtSignal, QTimer, pyqtSlot, QDateTime
from PyQt6.QtWidgets import QLabel

class Clock(QObject):
    """
    Class that implements a basic clock (timer or stopwatch),
    Utitlizes QTimer for the clock to update. 
    For cleaner code, QTimer is updated every milliseconds
    instead of seconds.
    """

    clkChngedSignal = pyqtSignal(str)    # Signal/Callback for when clock is changed

    def __init__(self, stopwatch=False, label: QLabel=None, parent=None):
        """
        """
        super(QObject, self).__init__(parent)
        self.tick = 0
        self.clock = QTimer()
        self.speed = 1
        self.tickTo = 0
        self.stopwatch = stopwatch
        self.timeFormat = "mm:ss"

        self.label = label

        self.clock.timeout.connect(self._clockEvent)

    def getTick(self) -> int:
        return self.tick

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
        timeStr = QDateTime.fromMSecsSinceEpoch(self.tick).toString(self.timeFormat)
        if (self.label != None):
            self.label.setText(timeStr)
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

    @pyqtSlot()
    def _clockEvent(self):
        if (self.stopwatch):
            self.stopWatch()
        else:
            self._timer()
        self._valueChanged()
    
    