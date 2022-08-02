"""
Author: Ian, TheLittleDoc, Fisk, Dan, Glenn
"""

import os, sys
from .abstractcmd import AbstractCmd
from PyQt6.QtCore import QPoint

PATH = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
if PATH not in sys.path:
    sys.path.append(PATH)

from layout.ctrllayout import CtrlLayout
from component.compfactory import CompFactory
from component.abstractcomp import AbstractComp

class InsertCmd(AbstractCmd):
    """
    Command used when insertting a component
    to the layout
    """

    def __init__(self, layout: CtrlLayout, type: str, pos: QPoint, count: int):
        """
        :param layout: Layout
        :param type: Component type (Ex. Clock)
        :param pos: Position of the component
        :param name: Object name
        """
        super().__init__()
        self.layout = layout
        self.type = type
        self.pos = pos
        self.count = count

    def execute(self) -> None:
        """
        Insert command is executed and 
        component gets insertted to the layout

        :param: none
        :return: none
        """
        self.component = CompFactory.makeComponent(self.type, True, self.layout)
        if (self.component != None):
            self.component.move(self.pos)
            self.component.disableWidget()
            self.component.firstTimeProp()
            name = self.component.getName() + str(self.count)
            self.component.setObjectName(name)
            self.layout.addComponent(self.component)
            if (self.layout.defaultSize() != self.layout.size()):
                self.component.insertCalc(self.layout.size())

    def getComponent(self) -> AbstractComp:
        """
        Returns the component this command is insertting.

        :param: none
        :return: Component
        """
        return self.component