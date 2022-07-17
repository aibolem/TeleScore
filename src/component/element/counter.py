"""
Author: Ian, TheLittleDoc, Fisk, Dan, Glenn
"""

from PyQt6.QtCore import QObject

class Counter(QObject):
    def __init__(self):
        self.value = 0

    def getValue(self):
        return self.value;

    def setValue(self, value):
        self.value = value;

    def increment(self, inc=1):
        self.value += inc

    def decrement(self, dec=1):
        self.value -= dec

    def toString(self):
        return str(self.value)