"""
Author: Ian, TheLittleDoc, Fisk, Dan, Glenn
"""
from .basiccomp.clocksetcomp import ClockSetComp
from .basiccomp.buttoncomp import ButtonComp
from .basiccomp.clockcomp import ClockComp
from .basiccomp.defaultcomp import DefaultComp

import os, sys
PATH = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
if PATH not in sys.path:
    sys.path.append(PATH)

from attr import CompAttr

class CompFactory():
    """
    Factory design patttern used to create category tabs in the component list.
    """
    
    NAME = "NAME"
    COLOR = "COLOR"
    TIMEDISPLAY = "Time Display"
    TIMESET = "Type Time Amount"

    def __init__():
        pass

    @classmethod
    def makeComponent(self, compName: str, edit=False, parent=None):
        comp = DefaultComp(parent)
        buttons = CompAttr.timeComponent

        if (compName in buttons):        # Change this for future
            item = buttons[compName]
            if (self.NAME in item and self.COLOR in item):
                comp = ButtonComp(item[self.NAME], item[CompAttr.SIGNAL], edit, parent)
                comp.setButtonColor(item[self.COLOR])

        match compName:
            case self.TIMEDISPLAY:
                comp = ClockComp(edit, parent)
            case self.TIMESET:
                comp = ClockSetComp(edit, parent)

        comp.setFixedSize(100, 70)
        return comp
