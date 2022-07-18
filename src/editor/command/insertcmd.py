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

class InsertCmd(AbstractCmd):
    """
    Command used when insertting a component
    to the layout
    """

    def __init__(self, layout: CtrlLayout, type: str, pos: QPoint, name: str):
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

    def execute(self):
        freelayout = self.layout.getLayout()
        component = CompFactory.makeComponent(self.type)
        if (component != None):
            component.move(self.pos)
            freelayout.addComponent(component, self.layout.defaultSize())
