"""
Author: Ian, TheLittleDoc, Fisk, Dan, Glenn
"""

from PyQt6 import uic
from ..abstractcomp import AbstractComp
from gm_resources import *


class DefaultComp(AbstractComp):
    """
    You found me, easteregg
    """

    def __init__(self, parent=None):
        super().__init__(parent)
        path = resourcePath("src/component/basiccomp/defaultcomp.ui")
        uic.loadUi(path, self) # Load the .ui file

    def disableWidget(self) -> None:
        # Nothing to implement here since clock is just a label
        pass

    # Override
    def getName(self) -> str:
        return ""