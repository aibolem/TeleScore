"""
Developed by: JumpShot Team
Written by: riscyseven
UI designed by: Fisk31
"""

from attr import CompAttr
from component.abstractcomp import AbstractComp

class ClockSetComp(AbstractComp):
    """
    CLock widget for scoreboard.

    This class has one clock object from the backend.
    """

    def __init__(self, objectName, edit=False, parent=None):
        super().__init__(objectName, "src/component/basiccomp/clocksetcomp.ui", edit, parent)

        if (edit == True):
            self.lineEdit.installEventFilter(self)
            self.pushButton.installEventFilter(self)

        self.pushButton.pressed.connect(self.pressed)

    # Override
    def _firstTimeProp(self) -> None:
        self.properties.appendProperty("Connection Properties", CompAttr.connProperty)
        self.connection.appendConnType("Set Time")

    # Override
    def _reloadProperty(self) -> None:
        pass

    # Override
    def getName(self) -> str:
        return "Type Time Amount"

    # Override
    def _reconfProperty(self) -> None:
        pass

    # Override
    def setFileDir(self, dirName):
        pass

    def pressed(self):
        self.connection.emitSignal("Set Time", self.lineEdit.text())