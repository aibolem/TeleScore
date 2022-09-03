"""
Developed by: JumpShot Team
Written by: riscyseven
Designed by: Fisk31
"""

from attr import CompAttr
from component.abstractcomp import AbstractComp

class ScoreNumComp(AbstractComp):
    """
    CLock widget for scoreboard.

    This class has one clock object from the backend.
    """

    def __init__(self, objectName, edit=False, parent=None):
        super().__init__(objectName, "src/component/basiccomp/scorenumcomp.ui", edit, parent)

        if (edit == True):
            self.lineEdit.installEventFilter(self)
            self.pushButton.installEventFilter(self)

        self.pushButton.pressed.connect(self.pressed)

    # Override
    def _firstTimeProp(self) -> None:
        self.properties.appendProperty("Connection Properties", CompAttr.connProperty)
        self.connection.appendConnType("Set Score")

    # Override
    def _reloadProperty(self) -> None:
        pass

    # Override
    def getName(self) -> str:
        return "Type Score Amount"

    # Override
    def _reconfProperty(self) -> None:
        pass

    def pressed(self):
        self.connection.emitSignal("Set Score", int(self.lineEdit.text()))