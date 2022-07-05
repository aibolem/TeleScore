from PyQt6.QtWidgets import QFrame
from abc import ABC, abstractmethod

class AbstractComp(ABC, QFrame):
    """
    Abstract class for components. All component classes should inherit this class

    Contains implmentation requirements for a component, also contains functions that
    are required for the editor
    """

    def __init__(self, *args):
        """
        Contruct a new 'AbstractComp' object

        :param 
        """
        super().__init__(self)

    @abstractmethod
    def getName():
        return "Name"

    @abstractmethod
    def disableWidget():
        pass

    
    def contextMenuEvent(self):
        pass

    def mouseMoveEvent(self, a0: QtGui.QMouseEvent) -> None:
        return super().mouseMoveEvent(a0)

    def mousePressEvent(self, a0: QtGui.QMouseEvent) -> None:
        return super().mousePressEvent(a0)

    def mouseReleaseEvent(self, a0: QtGui.QMouseEvent) -> None:
        return super().mouseReleaseEvent(a0)



