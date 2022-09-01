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

    def __init__(self, objectName, parent=None):
        super().__init__(objectName, "src/component/basiccomp/defaultcomp.ui",
         False, parent)

    # Override
    def _firstTimeProp(self) -> None:
        pass

    # Override
    def getName(self) -> str:
        return ""

    # Override
    def _reloadProperty(self) -> None:
        pass

    # Override
    def _reconfProperty(self) -> None:
        pass