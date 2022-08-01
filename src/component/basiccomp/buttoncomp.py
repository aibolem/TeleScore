"""
Author: Ian, TheLittleDoc, Fisk, Dan, Glenn
"""

from PyQt6 import uic
from PyQt6.QtCore import pyqtSlot
from PyQt6.QtGui import QColor, QFont
from gm_resources import *
from ..abstractcomp import AbstractComp
from ..property import Property

from component.compattr import CompAttr

class ButtonComp(AbstractComp):
    """
    Button widget for scoreboard.
    """
    
    def __init__(self, text, edit=False, parent=None):
        super().__init__(parent)
        path = resourcePath("src/component/basiccomp/buttoncomp.ui")
        uic.loadUi(path, self) # Load the .ui file
        self.setStyleSheet("QPushButton {border: none; color: white; \
         font-size: 17px; border-radius: 4px;}")
        self.pushButton.setText(text)

        if (edit == True):
            self.pushButton.installEventFilter(self)

    # Override
    def firstTimeProp(self):
        self.prop = Property()
        self.prop.appendProperty("General Properties", CompAttr.genProperty)
        self.prop.appendProperty("Appearance Properties", CompAttr.appearProperty)

    def clicked(self):
        print("hello")
        
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
        pass

    def _reloadProp(self):
        self.prop.changeValue("Component Name", "Test")
        self.prop.changeValue("Width", self.height())
        self.prop.changeValue("Height", self.width())
        self.prop.changeValue("X", self.x())
        self.prop.changeValue("Y", self.y())
        self.prop.changeValue("Display Text", self.pushButton.text())
        self.prop.changeValue("Display Font", self.pushButton.font().family())
        self.prop.changeValue("Font Size", self.pushButton.font().pixelSize())

    def getPropertyTab(self) -> list:
        """
        Method that returns how the property tab should
        be setup for this instance of a button

        :param: none
        :return: list containing the layout info
        """
        self._reloadProp()

        return self.prop.getList()

    @pyqtSlot()
    def propChanged(self) -> None:
        fontFamily = self.prop.getValue("Display Font")
        fontSize = self.prop.getValue("Font Size")
        displayText = self.prop.getValue("Display Text")
        self.pushButton.setStyleSheet("font-size: {}px; font-family: {}".format(fontSize, fontFamily))
        self.pushButton.setText(displayText)

    def getName(self) -> str:
        return "Button"
