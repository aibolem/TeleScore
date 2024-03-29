"""
Developed By: JumpShot Team
Written by: riscyseven
"""
from PyQt6.QtWidgets import QWidget, QVBoxLayout
from PyQt6.QtCore import QTimer

from component.abstractcomp import AbstractComp 
from component.penalty.penaltyinstance import PenaltyInstance
from attr import CompAttr

class PenaltyComp(AbstractComp):
    clockProperty = {
        "Format": {
            CompAttr.TYPE: CompAttr.TEXTEDIT,
            CompAttr.VALUE: "mm:ss"
        }
    }

    def __init__(self, objectName, edit=False, parent=None):
        super().__init__(objectName, "src/component/penalty/penaltycomp.ui", edit, parent)
        self.undoInst = None
        self.pInstList = []
        self.isRunning = False
        self.scrollWidget = QWidget()
        self.scrollArea.setWidget(self.scrollWidget)
        self.layoutList = QVBoxLayout()
        self.scrollWidget.setLayout(self.layoutList)

        self.add_pushButton.clicked.connect(self._addClicked)
        self.undo_pushButton.clicked.connect(self._undoClicked)

        self._initConn()

    # Override
    def _firstTimeProp(self):
        self.properties.appendProperty("Clock Properties", self.clockProperty)
        self.properties.appendProperty("File Properties", CompAttr.fileProperty)
        
    # Override
    def _reloadProperty(self):
        pass

    # Override
    def _reconfProperty(self):
        pass

    # Override
    def getName(self) -> str:
        return "Penalty"

    # Override
    def setFileDir(self, dirName):
        self.properties["File Output Location"] = dirName.format(self.objectName())

    def _initConn(self):
        self.connection.appendCallBack("Clock Stop", self._stop)
        self.connection.appendCallBack("Start", self._start)
        self.connection.appendCallBack("Stop", self._stop)
        self.connection.appendCallBack("Reset", self._reset)

    def _start(self):
        self.isRunning = True
        for inst in self.pInstList:
            inst.start()

    def _stop(self):
        self.isRunning = False
        for inst in self.pInstList:
            inst.stop()

    def _reset(self):
        self._stop()
        while len(self.pInstList) > 0:
            inst = self.pInstList.pop(0)
            inst.clear()
            inst.deleteLater()

    def _addClicked(self):
        self._addPenalty(self.plyr_lineEdit.text(), self.time_lineEdit.text())

    def _addPenalty(self, player: str, time: str):
        if (self.undoInst != None and self.undo_pushButton.isEnabled()):
            self.undo_pushButton.setDisabled(True)
            self.undoInst = None

        inst = PenaltyInstance(player, time, self.properties["Format"],
         self.properties["File Output Location"], len(self.pInstList))

        self.layoutList.addWidget(inst)

        inst.emitRemove.connect(self._removeInst)
        self.pInstList.append(inst)

        if (self.isRunning == True):
            QTimer.singleShot(1000, lambda: inst.start())
            
    def _removeInst(self, inst: PenaltyInstance, end: bool):
        index = self.pInstList.index(inst)
        inst.clear()
        self.pInstList[len(self.pInstList)-1].clear()

        if (end):
            self.undo_pushButton.setDisabled(True)
            self.layoutList.removeWidget(inst)
            inst.deleteLater()
            self.undoInst = None
        else:
            self.undo_pushButton.setEnabled(True)
            if (self.undoInst != None):
                self.undoInst.deleteLater()
            self.undoInst = inst
            self.layoutList.removeWidget(inst)
            inst.setVisible(False)

            if (self.isRunning == True):
                self.undoInst.stop()
                self.undoInst.clear()

        self._pushBack(index)
        self.pInstList.pop(len(self.pInstList)-1)

    def _pushBack(self, index):
        for i in range(index+1, len(self.pInstList)):
            self.pInstList.insert(i-1, self.pInstList.pop(i))
            self.pInstList[i-1].changeIndex(i-1)

    def _pushFront(self, index):
        if (len(self.pInstList)-1 >= 0):
            self.pInstList.append(self.pInstList[len(self.pInstList)-1])

            for i in range(len(self.pInstList)-1, index, -1):
                self.pInstList[i] = self.pInstList[i-1]
                self.pInstList[i].changeIndex(i)

            self.pInstList[index] = self.undoInst
            self.undoInst.changeIndex(index)
        else:
            self.pInstList.append(self.undoInst)
            self.undoInst.changeIndex(index)

    def _undoClicked(self):
        if (self.isRunning):
            self.undoInst.start()

        self._pushFront(self.undoInst.getIndex())
        self.undo_pushButton.setDisabled(True)
        self.layoutList.insertWidget(self.undoInst.getIndex(), self.undoInst)
        self.undoInst.setVisible(True)
        self.undoInst = None

        

