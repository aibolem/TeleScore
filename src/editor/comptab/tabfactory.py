from .clocktab import ClockTab
from .scoretab import ScoreTab

class TabFactory():
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
    def makeTab(self, tabName, treeWidget):
        match tabName:
            case self.Clock:
                return ClockTab(treeWidget)
            case self.Name:
                return ClockTab(treeWidget)
            case self.Score:
                return ScoreTab(treeWidget)
            case self.Period:
                return ClockTab(treeWidget)

    @classmethod
    def categories(self):
        categories = [self.Clock, self.Score]
        return categories

