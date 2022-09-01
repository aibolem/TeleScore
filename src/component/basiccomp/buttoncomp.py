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
from gm_resources import *
from component.abstractcomp import AbstractComp

class ButtonComp(AbstractComp):
    """
    Button widget for scoreboard.
    """
    
    def __init__(self, type, text, signal: str, objectName, edit=False, parent=None):
        super().__init__(objectName, "src/component/basiccomp/buttoncomp.ui", edit, parent)

        self.signal = signal
        self.buttonType = type
        self.text = text
        self.setStyleSheet("QPushButton {border: none; color: white; \
         font-size: 17px; border-radius: 4px;}")
        self.pushButton.setText(text)
        self.pushButton.clicked.connect(self._onClick)
        self.connection.appendConnType(self.signal)

        if (edit == True):
            self.pushButton.installEventFilter(self)

    # Override
    def _firstTimeProp(self):
        self.properties.appendProperty("Appearance Properties", CompAttr.appearProperty)
        self.properties.appendProperty("Connection Properties", CompAttr.connProperty)

    # Override
    def _reloadProperty(self):
        self.properties["Display Text"] = self.pushButton.text()
        self.properties["Display Font"] = self.pushButton.font().family()
        self.properties["Font Size"] = self.pushButton.font().pixelSize()

    # Override
    def _reconfProperty(self) -> None:
        self.pushButton.setStyleSheet("font-size: {}px;\
            font-family: {}".format(self.properties["Font Size"], self.properties["Display Font"]))
        self.pushButton.setText(self.properties["Display Text"])

    # Override
    def getName(self) -> str:
        return self.buttonType

    def _onClick(self):
        self.connection.emitSignal(self.signal)

    def setButtonColor(self, hexval: str) -> None:
        dimmed = QColor(hexval)
        dimmed.setRgb(dimmed.red() // 2, dimmed.green() // 2, dimmed.blue() // 2)
        self.setStyleSheet(self.styleSheet() +
                             "QPushButton {background-color: " +
                            hexval + ";}" + 
                            "QPushButton:pressed{background-color: " + 
                             dimmed.name(QColor.NameFormat.HexRgb) + ";}" +
                            "QPushButton:hover{color: #e8e8e8;}")
