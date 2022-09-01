"""
Author: Ian, TheLittleDoc, Fisk, Dan, Glenn
"""

import os, sys

from PyQt6.QtCore import Qt
from PyQt6.QtGui import QIcon, QPixmap
from PyQt6.QtWidgets import QFileDialog

PATH = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
if PATH not in sys.path:
    sys.path.append(PATH)

from attr import CompAttr
from gm_resources import *
from component.abstractcomp import AbstractComp
from fileio.fileout import TextOut, ImageOut

class TeamComp(AbstractComp):
    """
    Name component for now
    """

    imageProperty = {
        "Logo Width": {
            CompAttr.TYPE: CompAttr.NUMEDIT,
            CompAttr.VALUE: 80
        },
        "Logo Height": {
            CompAttr.TYPE: CompAttr.NUMEDIT,
            CompAttr.VALUE: 80
        }
    }
    
    def __init__(self, objectName, edit=False, parent=None):
        super().__init__(objectName, "src/component/teamcomp/teamcomp.ui", edit, parent)

        self.fileName = self.properties["File Output Location"]
        self.logo = None
        self.verticalLayout.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        self.icon_pushButton.clicked.connect(self._onLogoButton)
        self.setteam_PushButton.clicked.connect(self._setTeamButton)

        self.nameOut = TextOut(self.properties["File Output Location"].format("-name", "txt"), self)
        self.attrOut = TextOut(self.properties["File Output Location"].format("-attr", "txt"), self)
        self.logoOut = ImageOut(self.properties["File Output Location"].format("-logo", "png"), self)

    # Override
    def _firstTimeProp(self):
        self.properties.appendProperty("File Properties", CompAttr.fileProperty)
        self.properties["File Output Location"] = self.properties["File Output Location"].format(self.objectName() + "{}", "{}")
        self.properties.appendProperty("Logo Properties", self.imageProperty)

    # Override
    def _reloadProperty(self):
        self.properties["File Output Location"] = self.fileName

    # Override
    def _reconfProperty(self):
        if (self.fileName != self.properties["File Output Location"]):
            self.fileName = self.properties["File Output Location"]
            self.nameOut.setOutputFile(self.properties["File Output Location"].format("-name", "txt"))
            self.attrOut.setOutputFile(self.properties["File Output Location"].format("-attr", "txt"))
            self.logoOut.setOutputFile(self.properties["File Output Location"].format("-logo", "png"))
            self.attrChanged.emit()

    # Override
    def getName(self) -> str:
        return "Team Attribute"

    def _onLogoButton(self):
        fileName = QFileDialog.getOpenFileName(self, "Open Image Location", "", "Image File (*.png *.jpg)")[0]

        pixmap = QPixmap(fileName)
        icon = QIcon(pixmap)
        self.icon_pushButton.setIcon(icon)
        self.icon_pushButton.setIconSize(self.icon_pushButton.size())
        self.icon_pushButton.setText("")

        self.logo = pixmap.scaled(self.properties["Logo Width"], self.properties["Logo Height"])

    def _setTeamButton(self):
        name = self.nameLineEdit.text()
        attr = self.attrLineEdit.text()
        self.nameOut.outputFile(name)
        self.attrOut.outputFile(attr)

        if (self.logo != None):
            self.logoOut.outputFile(self.logo)
        