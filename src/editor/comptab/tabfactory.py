from .clocktab import ClockTab

class TabFactory():
    Clock = "Clock"
    Name = "Name"
    Score = "Score"
    Period = "Period"

    def __init__():
        pass

    @classmethod
    def makeTab(self, tabName):
        match tabName:
            case self.Clock:
                return ClockTab()
            case self.Name:
                return ClockTab()
            case self.Score:
                return ClockTab()
            case self.Period:
                return ClockTab()

    @classmethod
    def categories(self):
        categories = [self.Clock, self.Name,
         self.Score, self.Period]
        return categories
