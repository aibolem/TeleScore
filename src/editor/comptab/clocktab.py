from .compwidgethead import CompWidgetHead
from .compwidgetitem import CompWidgetItem
from gm_resources import resourcePath

class ClockTab():
    def __init__(self, treeWidget, parent=None):
        self.treeWidget = treeWidget
        self.parent = parent
        self.insertItems();

    def insertItems(self):
        header = CompWidgetHead(text="Time Based Buttons")
        self.treeWidget.addTopLevelItem(header)
        header.setExpanded(True)

        timeDisplay = CompWidgetItem(text="Time Display", icon=resourcePath("src\\resources\\tdisp.png"), parent=self.parent)
        startTime = CompWidgetItem(text="Start Time", icon=resourcePath("src\\resources\\startButton.png"), parent=self.parent)
        stopTime = CompWidgetItem(text="Stop Time", icon=resourcePath("src\\resources\\stopButton.png"), parent=self.parent)
        rstTime = CompWidgetItem(text="Reset Time", icon=resourcePath("src\\resources\\rstButton.png"), parent=self.parent)
        addSec = CompWidgetItem(text="Add Seconds", icon=resourcePath("src\\resources\\addSec.png"), parent=self.parent)
        subSec = CompWidgetItem(text="Subtract Seconds", icon=resourcePath("src\\resources\\subSec.png"), parent=self.parent)
        addMin = CompWidgetItem(text="Add Minutes", icon=resourcePath("src\\resources\\addMin.png"), parent=self.parent)
        subMin = CompWidgetItem(text="Subtract Minutes", icon=resourcePath("src\\resources\\subMin.png"), parent=self.parent)
        setTime = CompWidgetItem(text="Type Time Amount", icon=resourcePath("src\\resources\\setTime.png"), parent=self.parent)

        header.addChildren([timeDisplay, startTime, stopTime, rstTime,
         addSec, subSec, addMin, subMin, setTime])