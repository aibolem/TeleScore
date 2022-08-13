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
from component.element.counter import Counter
from gm_resources import *


class ScoreComp(AbstractComp):
    """
    CLock widget for scoreboard.

    This class has one clock object from the backend.
    """

    def __init__(self, edit=False, parent=None):
        super().__init__(parent)
        path = resourcePath("src/component/basiccomp/scorecomp.ui")
        uic.loadUi(path, self) # Load the .ui file
        self.score = Counter(self.label, self)

    def disableWidget(self) -> None:
        # Nothing to implement here since clock is just a label
        pass

    # Override
    def firstTimeProp(self):
        self.properties.appendProperty("Score Properties", CompAttr.scoreDispProperty)
        self.properties.appendProperty("Connection Properties", CompAttr.connProperty)
        self.connection.appendCallBack("Add Score", self.addPoint)
        self.connection.appendCallBack("Sub Score", self.subPoint)
        self.connection.appendCallBack("Set Score", self.setScore)

    def addPoint(self, value):
        self.score.increment(value)

    def subPoint(self, value):
        self.score.decrement(value)

    def setScore(self, value):
        self.score.setValue(value)

    # Override
    def getName(self) -> str:
        return "Score Display"

    # Override
    def reloadProperty(self) -> None:
        self.properties["Suffix (st, nd, rd, th)"] = self.score.getSuffix()

    def reconfProperty(self) -> None:
        self.score.setSuffix(self.properties["Suffix (st, nd, rd, th)"])