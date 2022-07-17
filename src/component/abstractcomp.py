from PyQt6.QtWidgets import QFrame
from PyQt6.QtCore import QSize, QRect
from abc import ABC, abstractmethod, ABCMeta

class Meta(type(ABC), type(QFrame)): pass

class AbstractComp(ABC, QFrame, metaclass=Meta):
    """
    Abstract class for components. All component classes should inherit this class

    Contains implmentation requirements for a component, also contains functions that
    are required for the editor
    """

    def __init__(self, parent=None):
        """
        Contruct a new 'AbstractComp' object

        :param 
        """
        super().__init__(parent)

    @abstractmethod
    def getName():
        pass

    @abstractmethod
    def disableWidget():
        pass
    
    # Override
    def contextMenuEvent(self):
        pass

    def sizeInit(self, size: QSize) -> None:
        """
        When the size or position of either the component
        is initialized or changed, 
        this must be called in order to have a relative sizing
        when resized. Ratio is used for future calculation.

        :param: size of the parent widget
        :return: none
        """
        self.xratio = size.width() / self.x()
        self.yratio = size.height() / self.y()
        self.wratio = size.width() / self.width()
        self.hratio = size.height() / self.height()

    def parentResizeEvent(self, size: QSize) -> None:
        """
        When parent widget's size is changed, this
        must be called for the component to resize respectively
        to the adjusted size.

        :param: size of the parent widget
        :return: none
        """
        if (self.xratio != 0 and self.yratio != 0):
            self.move(int(size.width()/self.xratio), int(size.height()/self.yratio))
            self.setFixedSize(int(size.width()/self.wratio), int(size.height()//self.hratio))


    '''# Override
    def mouseMoveEvent(self, a0: QtGui.QMouseEvent) -> None:
        return super().mouseMoveEvent(a0)

    # Override
    def mousePressEvent(self, a0: QtGui.QMouseEvent) -> None:
        return super().mousePressEvent(a0)

    # Override
    def mouseReleaseEvent(self, a0: QtGui.QMouseEvent) -> None:
        return super().mouseReleaseEvent(a0)'''



