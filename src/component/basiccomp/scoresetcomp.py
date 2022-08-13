"""
Author: Ian, TheLittleDoc, Fisk, Dan, Glenn
"""

import os, sys
from PyQt6 import uic
from PyQt6.QtGui import QColor

PATH = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
if PATH not in sys.path:
    sys.path.append(PATH)

from attr import CompAttr
from component.abstractcomp import AbstractComp
from component.element.counter import Counter
from gm_resources import *

class ScoreSetComp(AbstractComp):
    """
    Clock widget for scoreboard.

    This class has one clock object from the backend.
    """

    SET = -1
    INC = 0
    DEC = 1

    def __init__(self, delta=SET, edit=False, parent=None):
        super().__init__(parent)
        path = resourcePath("src/component/basiccomp/scoresetcomp.ui")
        uic.loadUi(path, self) # Load the .ui file
        self.setStyleSheet("QPushButton {border: none; color: white; \
         font-size: 17px; border-radius: 4px;}")
        self.setButtonColor("#863EA8")
        self.delta = delta
        match delta:
            case self.SET:
                self.pushButton.setText("Set\nNumber")
                self.connection.appendConnType("Set Score")
            case self.INC:
                self.pushButton.setText("Add [+]\nScore")
                self.setButtonColor("#4357ad")
                self.connection.appendConnType("Add Score")
            case self.DEC:
                self.pushButton.setText("Sub [-]\nScore")
                self.setButtonColor("#e15554")
                self.connection.appendConnType("Sub Score")
        

        if (edit == True):
            self.pushButton.installEventFilter(self)
        self.value = 1

        self.pushButton.pressed.connect(self.buttonPressed)

    def disableWidget(self) -> None:
        # Nothing to implement here since clock is just a label
        pass

    def buttonPressed(self):
        match self.delta:
            case self.SET:
                self.connection.emitSignal("Set Score", self.value)
            case self.INC:
                self.connection.emitSignal("Add Score", self.value)
            case self.DEC:
                self.connection.emitSignal("Sub Score", self.value)
        

    # Override
    def firstTimeProp(self):
        self.properties.appendProperty("Appearance Properties", CompAttr.appearProperty)
        self.properties.appendProperty("Set Properties", CompAttr.scoreSetProperty)
        self.properties.appendProperty("Connection Properties", CompAttr.connProperty)

    # Override
    def getName(self) -> str:
        return "Score Set"

    def setButtonColor(self, hexval: str) -> None:
        dimmed = QColor(hexval)
        dimmed.setRgb(dimmed.red()//2, dimmed.green()//2, dimmed.blue()//2)
        self.setStyleSheet(self.styleSheet() +
                             "QPushButton {background-color: " +
                            hexval + ";}" + 
                            "QPushButton:pressed{background-color: " + 
                             dimmed.name(QColor.NameFormat.HexRgb) + ";}" +
                            "QPushButton:hover{color: #e8e8e8;}")

    # Override
    def reloadProperty(self) -> None:
        self.properties["Display Text"] = self.pushButton.text()
        self.properties["Display Font"] = self.pushButton.font().family()
        self.properties["Font Size"] = self.pushButton.font().pixelSize()
        self.properties["Set Amount"] = self.value

    def reconfProperty(self) -> None:
        self.value = self.properties["Set Amount"]
        self.pushButton.setText(str(self.value))
        self.pushButton.setStyleSheet(" font-size: {}px;\
            font-family: {}".format(self.properties["Font Size"], self.properties["Display Font"]))
        if (len(self.properties["Display Text"]) > 0):
            self.pushButton.setText(self.properties["Display Text"])