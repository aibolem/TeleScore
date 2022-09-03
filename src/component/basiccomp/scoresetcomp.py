"""
Developed by: JumpShot Team
Written by: riscyseven
Designed by: Fisk31
"""

from attr import CompAttr
from component.basiccomp.buttoncomp import ButtonComp

class ScoreSetComp(ButtonComp):
    """
    Score Set Button

    Class defines the functionality for the button that 
    sets the score
    """

    SET = "Score Set"
    INC = "Add Points"
    DEC = "Sub Points"

    scoreSetProperty = {
        "Set Amount": {
            CompAttr.TYPE: CompAttr.NUMEDIT,
            CompAttr.VALUE: 0
        }
    }

    def __init__(self, objectName, delta=SET, edit=False, parent=None):
        super().__init__("", "", "", objectName, edit, parent) # Probably want to refract this

        self.setButtonColor("#863EA8")
        self.connection.removeConnType("")
        self.delta = delta
        self.value = 1
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
        
    # Override
    def _firstTimeProp(self):
        self.properties.appendProperty("Appearance Properties", CompAttr.appearProperty)
        self.properties.appendProperty("Set Properties", self.scoreSetProperty)
        self.properties.appendProperty("Connection Properties", CompAttr.connProperty)

    # Override
    def _reloadProperty(self) -> None:
        self.properties["Display Text"] = self.pushButton.text()
        self.properties["Display Font"] = self.pushButton.font().family()
        self.properties["Font Size"] = self.pushButton.font().pixelSize()
        self.properties["Set Amount"] = self.value

    # Override
    def _reconfProperty(self) -> None:
        self.value = self.properties["Set Amount"]
        self.pushButton.setText(str(self.value))
        self.pushButton.setStyleSheet(" font-size: {}px;\
            font-family: {}".format(self.properties["Font Size"], self.properties["Display Font"]))
        if (len(self.properties["Display Text"]) > 0):
            self.pushButton.setText(self.properties["Display Text"])

    # Override
    def getName(self) -> str:
        return self.delta

    # Override
    def _onClick(self):
        match self.delta:
            case self.SET:
                self.connection.emitSignal("Set Score", self.value)
            case self.INC:
                self.connection.emitSignal("Add Score", self.value)
            case self.DEC:
                self.connection.emitSignal("Sub Score", self.value)