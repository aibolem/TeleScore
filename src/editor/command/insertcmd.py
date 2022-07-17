"""
Author: Ian, TheLittleDoc, Fisk, Dan, Glenn
"""

import os, sys
from .abstractcmd import AbstractCmd

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

    def __init__(self, layout: CtrlLayout, type: str, pos, name):
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
        self.name = name
        pass

    def execute(self):
        freelayout = self.layout.getLayout()
        button = CompFactory.makeComponent("Clock")
        button.move(self.pos)
        freelayout.addComponent(button, self.layout.size())
        pass