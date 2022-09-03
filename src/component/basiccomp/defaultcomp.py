"""
Developed by: JumpShot Team
Written by: riscyseven
Designed by: Fisk31
"""

from component.abstractcomp import AbstractComp

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