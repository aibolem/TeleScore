"""
Author: Ian, TheLittleDoc, Fisk, Dan, Glenn
"""

from .abstractcmd import AbstractCmd

class InsertCmd(AbstractCmd):
    """
    Command used when insertting a component
    to the layout
    """

    def __init__(self, layout, type, pos, name):
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
        pass