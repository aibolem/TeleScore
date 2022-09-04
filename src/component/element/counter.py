"""
Developed by: JumpShot Team
Written by: riscyseven
"""

from PyQt6.QtCore import QObject

class Counter(QObject):
    def __init__(self, label=None, file=None, parent=None):
        super(QObject, self).__init__(parent)
        self.value = 0
        self.label = label
        self.suffix = ["st", "nd", "rd", "th"]
        self.currSuffix = ""
        self.suffixEn = 0
        self.file = file
        self.clearScoreZero = False

    def getValue(self):
        return self.value

    def setValue(self, value):
        self.value = value
        self.updateValue()

    def increment(self, inc=1):
        self.value += inc
        self.updateValue()

    def decrement(self, dec=1):
        self.value -= dec
        self.updateValue()

    def updateValue(self):
        self.computeSuffix()

        text = str(self.value)
        if (self.suffixEn == 2):
            text = str(self.value) + self.currSuffix

        if(self.file != None):
            outFile = text
            if (self.clearScoreZero and self.value == 0):
                outFile = ""
            self.file.outputFile(outFile)

        if (self.label != None):
            self.label.setText(text)

    def computeSuffix(self):
        tenth = (abs(self.value)%10)-1
        self.currSuffix = self.suffix[3]
        try:
            if (self.value < 10 or self.value > 20):
                self.currSuffix = self.suffix[tenth]
        except IndexError:
            pass

    def setSuffix(self, value):
        self.suffixEn = value
        self.updateValue()

    def getSuffix(self) -> bool:
        return self.suffixEn

    def toString(self):
        return str(self.value)

    def setClearScoreZero(self, value):
        self.clearScoreZero = value
        self.updateValue()