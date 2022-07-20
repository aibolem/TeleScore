"""
Author: Ian, TheLittleDoc, Fisk, Dan, Glenn
"""
from .basiccomp.clocksetcomp import ClockSetComp
from .basiccomp.buttoncomp import ButtonComp
from .basiccomp.clockcomp import ClockComp
from .basiccomp.defaultcomp import DefaultComp

class CompFactory():
    """
    Factory design patttern used to create category tabs in the component list.
    """
    
    NAME = "NAME"
    COLOR = "COLOR"
    TIMEDISPLAY = "Time Display"
    TIMESET = "Type Time Amount"

    buttonName = {
                "Start Time": {NAME: "Start", COLOR: "#000000"},
                "Stop Time": {NAME: "Stop", COLOR: "#e15554"},
                "Reset Time": {NAME: "Reset", COLOR: "#4357ad"},
                "Add Seconds": {NAME: "Add [+]\nSeconds", COLOR: "#242325"},
                "Subtract Seconds": {NAME: "Subtract [+]\nSeconds", COLOR: "#242325"},
                "Add Minutes": {NAME: "Add [-]\nMinutes", COLOR: "#242325"},
                "Subtract Minutes": {NAME: "Subtract [-]\nMinutes", COLOR: "#242325"}
                }

    def __init__():
        pass

    @classmethod
    def makeComponent(self, compName: str, edit=False):
        comp = DefaultComp()

        if (compName in self.buttonName):
            comp = ButtonComp(self.buttonName[compName][self.NAME], edit)
            comp.setButtonColor(self.buttonName[compName][self.COLOR])

        match compName:
            case self.TIMEDISPLAY:
                comp = ClockComp(edit)
            case self.TIMESET:
                comp = ClockSetComp(edit)

        comp.setFixedSize(100, 70)
        return comp
