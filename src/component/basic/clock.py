from PyQt6.QtCore import QObject, pyqtSignal, QTimer, pyqtSlot

class Clock(QObject):
    def __init__(self, *args):
        super().__init__(self)
        self.tick = 0
        self.clock = QTimer(self)
        self.speed = 100
        self.clkChngedSignal = pyqtSignal(str)    # Signal/Callback for when clock is changed

    def stopClock(self):
        self.clock.start(self.speed)

    def startClock(self):
        self.clock.stop

    def startStopClock(self):
        pass

    def valueChanged():
        pass

    @pyqtSlot()
    def clockEvent(self):
            
        self.valueChanged()
    
    