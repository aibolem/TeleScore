"""
Author: Ian, TheLittleDoc, Fisk, Dan, Glenn
"""

from PyQt6 import uic
from PyQt6.QtCore import pyqtSlot
from PyQt6.QtGui import QColor, QFont
from gm_resources import *
from ..abstractcomp import AbstractComp

import os, sys

PATH = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
if PATH not in sys.path:
    sys.path.append(PATH)

from attr import CompAttr

class ButtonComp(AbstractComp):
    """
    Button widget for scoreboard.
    """
    
    def __init__(self, text, signal: str, edit=False, parent=None):
        super().__init__(parent)
        path = resourcePath("src/component/basiccomp/buttoncomp.ui")
        uic.loadUi(path, self) # Load the .ui file
        self.setStyleSheet("QPushButton {border: none; color: white; \
         font-size: 17px; border-radius: 4px;}")
        self.pushButton.setText(text)
        self.pushButton.clicked.connect(self.onClick)
        self.signal = signal

        if (edit == True):
            self.pushButton.installEventFilter(self)

    def onClick(self):
        self.connection.emitSignal(self.signal)

    # Override
    def firstTimeProp(self):
        self.properties.appendProperty("General Properties", CompAttr.genProperty)
        self.properties.appendProperty("Appearance Properties", CompAttr.appearProperty)
        self.properties.appendProperty("Connection Properties", CompAttr.connProperty)

        self.connection.appendConnType(self.signal)
        
    # Override
    def disableWidget(self) -> None:
        #self.pushButton.setDisabled(True)
        pass

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
    def reloadProperty(self):
        self.properties["Display Text"] = self.pushButton.text()
        self.properties["Display Font"] = self.pushButton.font().family()
        self.properties["Font Size"] = self.pushButton.font().pixelSize()

    # Override
    def reconfProperty(self) -> None:
        self.pushButton.setStyleSheet("font-size: {}px;\
            font-family: {}".format(self.properties["Font Size"], self.properties["Display Font"]))
        self.pushButton.setText(self.properties["Display Text"])

    # Override
    def getName(self) -> str:
        return "Button"
