"""
Author: Ian, TheLittleDoc, Fisk, Dan, Glenn
"""

from PyQt6 import uic
from PyQt6.QtCore import pyqtSlot
from PyQt6.QtGui import QColor
from gm_resources import *
from ..abstractcomp import AbstractComp

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

        self.firstTimeProp()

    def firstTimeProp(self):
        self.genProperty = CompAttr.genProperty
        self.appProperty = CompAttr.appearProperty
        self.prop = CompAttr.defaultButtonProp
        self.prop["General Properties"][CompAttr.PROPERTIES] = self.genProperty
        self.prop["Appearance Properties"][CompAttr.PROPERTIES] = self.appProperty

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

    def getPropertyTab(self) -> list:
        """
        Method that returns how the property tab should
        be setup for this instance of a button

        :param: none
        :return: list containing the layout info
        """
        self.genProperty["Component Name"][CompAttr.VALUE] = "Test"
        self.genProperty["Width"][CompAttr.VALUE] = str(self.width())
        self.genProperty["Height"][CompAttr.VALUE] = str(self.height())
        self.genProperty["X"][CompAttr.VALUE] = str(self.x())
        self.genProperty["Y"][CompAttr.VALUE] = str(self.y())
        self.appProperty["Display Text"][CompAttr.VALUE] = self.pushButton.text()
        self.appProperty["Display Font"][CompAttr.VALUE] = self.pushButton.font().toString()
        self.appProperty["Font Size"][CompAttr.VALUE] = str(self.pushButton.font().pixelSize())

        return self.prop

    @pyqtSlot()
    def propChanged(self) -> None:
        pass

    def getName(self) -> str:
        return "Button"
