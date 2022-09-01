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
from component.teamcomp.teamcomp import TeamComp

class CompFactory():
    """
    Factory design patttern used to create category tabs in the component list.
    """

    def __init__():
        pass

    @classmethod
    def makeComponent(self, compName: str, objectName, edit=False, parent=None):
        allCompList = CompAttr.getAllCategory()

        if (compName not in allCompList):
            return DefaultComp(parent)

        comp = None
        if (allCompList[compName][CompAttr.TYPE] == "BUTTON"):
            try:
                item = allCompList[compName]
                comp = ButtonComp(compName, item[CompAttr.TEXT], item[CompAttr.SIGNAL], objectName, edit, parent)
                comp.setButtonColor(item[CompAttr.COLOR])
            except:
                return DefaultComp(objectName, parent)

        # If the component isn't a button, go through possibility. 
        match compName:
            case "Time Display":
                comp = ClockComp(objectName, edit, parent)
            case "Type Time Amount":
                comp = ClockSetComp(objectName, edit, parent)
            case "Score Display":
                comp = ScoreComp(objectName, edit, parent)
            case "Add Points":
                comp = ScoreSetComp(objectName, ScoreSetComp.INC, edit, parent)
            case "Sub Points":
                comp = ScoreSetComp(objectName, ScoreSetComp.DEC, edit, parent)
            case "Score Set":
                comp = ScoreSetComp(objectName, ScoreSetComp.SET, edit, parent)
            case "Team Attribute":
                return TeamComp(objectName, edit, parent)

        comp.setFixedSize(100, 70)
        return comp
