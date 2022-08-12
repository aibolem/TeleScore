"""
Author: Ian, TheLittleDoc, Fisk, Dan, Glenn
"""

from PyQt6.QtWidgets import QMainWindow, QFrame
from PyQt6 import uic, QtGui
from PyQt6.QtCore import QPoint, pyqtSlot, QSize
from gm_resources import *

PATH = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
if PATH not in sys.path:
    sys.path.append(PATH)

from component.abstractcomp import AbstractComp
from editor.complisttab import CompListTab
from editor.propertytab import PropertyTab
from editor.command.insertcmd import InsertCmd
from layout.ctrllayout import CtrlLayout

class Editor(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent) # Call the inherited classes __init__ method
        path = resourcePath("src/window/ui/editor.ui")
        uic.loadUi(path, self) # Load the .ui file
        self.cmdStack = QtGui.QUndoStack(self)
        self.ctrl = CtrlLayout(QSize(800, 600), self.remCallBack, self)
        self.ctrl.dropSignal.connect(self._dropSlot)
        self.currComp = None
        self._initUI()

    def _initUI(self) -> None:
        """
        Initializes the editor UI.

        :param: none
        :return: none
        """
        self.comp = CompListTab(self)
        self.compDock.setWidget(self.comp)

        self.prop = PropertyTab(self)
        self.propDock.setWidget(self.prop)

        self.ctrl.setFrameShape(QFrame.Shape.Box)
        self.setCentralWidget(self.ctrl)

    @pyqtSlot(object)
    def _compClicked(self, comp: AbstractComp) -> None:
        """
        If any of the component is clicked, this
        slot gets called. This should process the property
        tab initiation. Get the property of the component
        and pass it onto the property tab.

        :param comp: Component that has been clicked
        :return: none
        """
        if (self.currComp != comp):
            if (self.currComp != None):
                self.prop.propChanged.disconnect(self.currComp.propChanged)
                self.currComp.attrChanged.disconnect(self.prop.externalChange)
                self.currComp.setFrameShape(QFrame.Shape.NoFrame)
            self.prop.propChanged.connect(comp.propChanged)
            self.prop.loadProperties(comp.getPropertyTab())
            comp.attrChanged.connect(self.prop.externalChange)
            comp.setFrameShape(QFrame.Shape.Box)
            comp.setLineWidth(3)

        self.currComp = comp

    @pyqtSlot(QtGui.QDropEvent)
    def _dropSlot(self, evt: QtGui.QDropEvent) -> None:
        """
        When component is dropped from the components list, 
        this is called and adds the right component to the layout

        :param evt: event information
        :return: none
        """
        type = evt.mimeData().data("application/x-comp").data().decode()
        point = QPoint(int(evt.position().x()), int(evt.position().y()))
        insert = InsertCmd(self.ctrl, type, point, self.ctrl.count())
        self.cmdStack.push(insert)

        comp = insert.getComponent()
        comp.compClicked.connect(self._compClicked)

    def remCallBack(self, component: AbstractComp):
        if (self.currComp == component):
            self.prop.propChanged.disconnect(self.currComp.propChanged)
            self.currComp.attrChanged.disconnect(self.prop.externalChange)
            self.currComp = None
            self.prop.clearTree()
        component.compClicked.disconnect(self._compClicked)
        