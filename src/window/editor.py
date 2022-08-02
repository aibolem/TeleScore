"""
Author: Ian, TheLittleDoc, Fisk, Dan, Glenn
"""

from PyQt6.QtWidgets import QMainWindow, QFrame
from PyQt6 import uic, QtGui
from PyQt6.QtCore import QPoint, pyqtSlot, QSize
from gm_resources import *
from layout.ctrllayout import CtrlLayout

from editor.complisttab import CompListTab
from editor.propertytab import PropertyTab
from editor.command.insertcmd import InsertCmd

PATH = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
if PATH not in sys.path:
    sys.path.append(PATH)

from component.element.clock import Clock

from component.abstractcomp import AbstractComp

class Editor(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent) # Call the inherited classes __init__ method
        path = resourcePath("src/window/ui/editor.ui")
        uic.loadUi(path, self) # Load the .ui file
        self.cmdStack = []
        self.ctrl = CtrlLayout(projSize=QSize(800, 600))
        self.ctrl.dropSignal.connect(self._dropSlot)
        self.currComp = None
        self._initUI()

    def _initUI(self) -> None:
        """
        Initializes the editor UI.

        :param: none
        :return: none
        """
        self.comp = CompListTab()
        self.compDock.setWidget(self.comp)

        self.prop = PropertyTab()
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
            self.prop.propChanged.connect(comp.propChanged)
            self.prop.loadProperties(comp.getPropertyTab())

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
        insert.execute()
        self.cmdStack.append(insert)

        comp = insert.getComponent()

        comp.compClicked.connect(self._compClicked)
        