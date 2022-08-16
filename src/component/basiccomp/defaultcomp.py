"""
Author: Ian, TheLittleDoc, Fisk, Dan, Glenn
"""

import os, sys
from PyQt6 import uic

PATH = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
if PATH not in sys.path:
    sys.path.append(PATH)

from component.abstractcomp import AbstractComp
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
    def firstTimeProp(self) -> None:
        pass

    # Override
    def getName(self) -> str:
        return ""

    # Override
    def reloadProperty(self) -> None:
        pass

    def reconfProperty(self) -> None:
        pass