"""
Author: Ian, TheLittleDoc, Fisk, Dan, Glenn
"""

import os, sys
from PyQt6.QtCore import QPoint
from PyQt6.QtGui import QUndoCommand

PATH = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
if PATH not in sys.path:
    sys.path.append(PATH)

from layout.ctrllayout import CtrlLayout
from component.compfactory import CompFactory
from component.abstractcomp import AbstractComp

class InsertCmd(QUndoCommand):
    """
    Command used when insertting a component
    to the layout
    """

    def __init__(self, layout: CtrlLayout, type: str, pos: QPoint, count: int, parent=None):
        """
        :param layout: Layout
        :param type: Component type (Ex. Clock)
        :param pos: Position of the component
        :param name: Object name
        """
        super().__init__(parent)
        self.layout = layout
        self.type = type
        self.pos = pos
        self.count = count
        self.component = None

    # Override
    def redo(self) -> None:
        """
        Insert command is executed and 
        component gets insertted to the layout

        :param: none
        :return: none
        """
        self.component = CompFactory.makeComponent(self.type, self.type + str(self.count), True, self.layout)
        if (self.component != None):
            self.component.move(self.pos)
            self.layout.addComponent(self.component)

    # Override
    def undo(self) -> None:
        self.layout.removeComponent(self.component)

    def getComponent(self) -> AbstractComp:
        """
        Returns the component this command is insertting.

        :param: none
        :return: Component
        """
        return self.component