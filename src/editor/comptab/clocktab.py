from .compwidgethead import CompWidgetHead
from .compwidgetitem import CompWidgetItem
from gm_resources import resourcePath

class ClockTab():
    def __init__(self, treeWidget):
        self.treeWidget = treeWidget
        self.parent = treeWidget
        self.insertItems();

    def insertItems(self):
        header = CompWidgetHead("Time Based Buttons", parent=self.parent)
        header.setExpanded(True)

        CompWidgetItem(resourcePath("src\\resources\\tdisp.png"), header, self.parent, "Time Display")
        CompWidgetItem(resourcePath("src\\resources\\startButton.png"), header, self.parent, "Start Time")
        CompWidgetItem(resourcePath("src\\resources\\stopButton.png"), header, self.parent, "Stop Time")
        CompWidgetItem(resourcePath("src\\resources\\rstButton.png"), header, self.parent, "Reset Time")
        CompWidgetItem(resourcePath("src\\resources\\addSec.png"), header, self.parent, "Add Seconds")
        CompWidgetItem(resourcePath("src\\resources\\subSec.png"), header, self.parent , "Subtract Seconds")
        CompWidgetItem(resourcePath("src\\resources\\addMin.png"), header, self.parent, "Add Minutes")
        CompWidgetItem(resourcePath("src\\resources\\subMin.png"), header, self.parent, "Subtract Minutes")
        CompWidgetItem(resourcePath("src\\resources\\setTime.png"), header, self.parent, "Type Time Amount")