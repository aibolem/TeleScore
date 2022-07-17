"""
Author: Ian, TheLittleDoc, Fisk, Dan, Glenn
"""
from tkinter import Button
from .basiccomp.buttoncomp import ButtonComp

class CompFactory():
    """
    Factory design patttern used to create category tabs in the component list.
    """
    
    Clock = "Clock"
    Name = "Name"
    Score = "Score"
    Period = "Period"

    def __init__():
        pass

    @classmethod
    def makeComponent(self, compName: str):
        match compName:
            case self.Clock:
                button = ButtonComp()
                button.setButtonColor("#FF00FF")
                button.setFixedSize(150, 100)
                return button

    @classmethod
    def categories(self):
        categories = [self.Clock, self.Score]
        return categories

