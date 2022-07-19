"""
Author: Ian, TheLittleDoc, Fisk, Dan, Glenn
"""

from PyQt6.QtWidgets import QFrame
from PyQt6.QtCore import QSize, QPoint, Qt, QEvent, QObject
from PyQt6.QtGui import QMouseEvent
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
        self.propertyMap = {}
        self.firstPoint = QPoint(1, 1)
        self.parentSize = QSize(1, 1)
        self.updatedSize = QSize(1, 1)
        self.mousePressed = False
        self.resizeRadius = 5

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
        if (self.x() <= 0):
            self.move(1, self.y())
        if (self.y() <= 0):
            self.move(self.x(), 1)

        self.xratio = size.width() / self.x()
        self.yratio = size.height() / self.y()
        self.wratio = size.width() / self.width()
        self.hratio = size.height() / self.height()

        self.parentSize = size
        self.updatedSize = size

    def parentResizeEvent(self, size: QSize) -> None:
        """
        When parent widget's size is changed, this
        must be called for the component to resize respectively
        to the adjusted size.

        :param: size of the parent widget
        :return: none
        """
        self.updatedSize = size
        if (self.xratio != 0 and self.yratio != 0):
            self.move(int(size.width()/self.xratio), int(size.height()/self.yratio))
            self.setFixedSize(int(size.width()/self.wratio), int(size.height()/self.hratio))

    def resizeFromOrg(self, modSize: QSize):
        self.updatedSize = modSize
        self.relocateFromOrg(modSize)
        self.setFixedSize(int(modSize.width()/self.wratio), int(modSize.height()/self.hratio))

    def relocateFromOrg(self, size: QSize):
        self.xratio = size.width() / self.x()
        self.yratio = size.height() / self.y()

    # Override
    def mouseMoveEvent(self, evt: QMouseEvent) -> None:
        if (self.mousePressed == True):
            #self.cornerResizeCheck(evt.pos())
            pos = self.mapToParent(evt.pos())
            self.move(pos.x()-self.firstPoint.x(), pos.y()-self.firstPoint.y())

    # Override
    def mousePressEvent(self, evt: QMouseEvent) -> None:
        self.setCursor(Qt.CursorShape.SizeAllCursor)
        self.firstPoint = evt.pos()
        self.mousePressed = True

    # Override
    def mouseReleaseEvent(self, evt: QMouseEvent) -> None:
        self.setCursor(Qt.CursorShape.ArrowCursor)
        self.relocateFromOrg(self.updatedSize)
        self.mousePressed = False

    def eventFilter(self, obj: QObject, evt: QEvent) -> bool:
        if (evt.type() == QEvent.Type.MouseMove):
            self.mouseMoveEvent(evt)
        elif (evt.type() == QEvent.Type.MouseButtonPress):
            self.mousePressEvent(evt)
        elif (evt.type() == QEvent.Type.MouseButtonRelease):
            self.mouseReleaseEvent(evt)
        return False

    def cornerResizeCheck(self, pos) -> bool:
        """
        Method for resizing by drag. 
        """
        if (pos.x() <= self.resizeRadius and pos.y() <= self.resizeRadius): # Top Left
            self.setCursor(Qt.CursorShape.SizeFDiagCursor)
        elif (pos.x() >= self.size().width()-self.resizeRadius and pos.y() <= self.resizeRadius): # Top right
            self.setCursor(Qt.CursorShape.SizeBDiagCursor)
        elif (pos.x() <= self.resizeRadius and pos.y() >= self.size().height()-self.resizeRadius): # Bottom right
            self.setCursor(Qt.CursorShape.SizeBDiagCursor)
        elif (pos.x() >= self.size().width()-self.resizeRadius and 
                pos.y() >= self.size().height()-self.resizeRadius): # Bottom left

                newPos = QPoint(pos.x()-self.firstPoint.x(), pos.y()-self.firstPoint.y())
                self.setFixedSize(self.width() + newPos.x(), self.height() + newPos.y())
                self.setCursor(Qt.CursorShape.SizeFDiagCursor)
        else:
            self.setCursor(Qt.CursorShape.ArrowCursor)

