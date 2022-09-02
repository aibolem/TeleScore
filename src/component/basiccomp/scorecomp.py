"""
Author: Ian, TheLittleDoc, Fisk, Dan, Glenn
"""

import os, sys

PATH = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
if PATH not in sys.path:
    sys.path.append(PATH)

from attr import CompAttr
from component.abstractcomp import AbstractComp
from component.element.counter import Counter
from gm_resources import *
from fileio.fileout import TextOut


class ScoreComp(AbstractComp):
    """
    CLock widget for scoreboard.

    This class has one clock object from the backend.
    """

    scoreDispProperty = {
        "Suffix (st, nd, rd, th)": {
            CompAttr.TYPE: CompAttr.CHECKBOX,
            CompAttr.VALUE: 0
        }
    }

    def __init__(self, objectName, edit=False, parent=None):
        super().__init__(objectName, "src/component/basiccomp/scorecomp.ui", edit, parent)

        self.fileOut = TextOut(parent=self)
        self.fileOut.setOutputFile(self.properties["File Output Location"])
        self.score = Counter(self.label, self.fileOut, self)

    # Override
    def _firstTimeProp(self):
        self.properties.appendProperty("File Properties", CompAttr.fileProperty)
        self.properties["File Output Location"] = self.properties["File Output Location"].format(self.objectName(), "txt")
        self.properties.appendProperty("Score Properties", self.scoreDispProperty)
        self.properties.appendProperty("Connection Properties", CompAttr.connProperty)

        self.connection.appendCallBack("Add Score", self.addPoint)
        self.connection.appendCallBack("Sub Score", self.subPoint)
        self.connection.appendCallBack("Set Score", self.setScore)

    # Override
    def getName(self) -> str:
        return "Score Display"

    # Override
    def _reloadProperty(self) -> None:
        self.properties["Suffix (st, nd, rd, th)"] = self.score.getSuffix()
        self.properties["File Output Location"] = self.fileOut.getOutputFile()

    # Override 
    def _reconfProperty(self) -> None:
        self.score.setSuffix(self.properties["Suffix (st, nd, rd, th)"])
        self.fileOut.setOutputFile(self.properties["File Output Location"].format("", "txt"))
        if (self.fileOut.getOutputFile() != self.properties["File Output Location"]):
            self.attrChanged.emit()

    def addPoint(self, value):
        self.score.increment(value)

    def subPoint(self, value):
        self.score.decrement(value)

    def setScore(self, value):
        self.score.setValue(value)