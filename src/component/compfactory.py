"""
Author: Ian, TheLittleDoc, Fisk, Dan, Glenn
"""

import os, sys

PATH = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
if PATH not in sys.path:
    sys.path.append(PATH)

from attr import CompAttr
from component.basiccomp.clocksetcomp import ClockSetComp
from component.basiccomp.buttoncomp import ButtonComp
from component.basiccomp.clockcomp import ClockComp
from component.basiccomp.scorecomp import ScoreComp
from component.basiccomp.defaultcomp import DefaultComp
from component.basiccomp.scoresetcomp import ScoreSetComp
from component.basiccomp.scorecomp import ScoreComp

class CompFactory():
    """
    Factory design patttern used to create category tabs in the component list.
    """
    
    NAME = "NAME"
    COLOR = "COLOR"
    TIMEDISPLAY = "Time Display"
    TIMESET = "Type Time Amount"
    SCOREDISPLAY = "Score Display"
    SCORESET = "Score Set"

    def __init__():
        pass

    @classmethod
    def makeComponent(self, compName: str, edit=False, parent=None):
        comp = DefaultComp()
        buttons = CompAttr.getAllCategory()

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
            case self.SCOREDISPLAY:
                comp = ScoreComp(edit, parent)
            case "Add Points":
                comp = ScoreSetComp(ScoreSetComp.INC, edit, parent)
            case "Sub Points":
                comp = ScoreSetComp(ScoreSetComp.DEC, edit, parent)
            case self.SCORESET:
                comp = ScoreSetComp(ScoreSetComp.SET, edit, parent)

        comp.setFixedSize(100, 70)
        return comp
