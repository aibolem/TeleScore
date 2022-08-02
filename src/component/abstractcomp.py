"""
Author: Ian, TheLittleDoc, Fisk, Dan, Glenn
"""
import os, sys

from PyQt6.QtWidgets import QFrame, QMenu
from PyQt6.QtCore import QSize, QPoint, Qt, QEvent, QObject, pyqtSignal, pyqtSlot
from PyQt6.QtGui import QMouseEvent, QContextMenuEvent
from abc import ABC, abstractmethod, ABCMeta
from gm_resources import GMessageBox

PATH = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
if PATH not in sys.path:
    sys.path.append(PATH)

from .property import Property
from .connection import Connection
from .compattr import CompAttr

class Meta(type(ABC), type(QFrame)): pass

class AbstractComp(ABC, QFrame, metaclass=Meta):
    """
    Abstract class for components. All component classes should inherit this class

    Contains implmentation requirements for a component, also contains functions that
    are required for the editor
    """

    compClicked = pyqtSignal(object) # Object should be AbstractComp

    def __init__(self, parent=None):
        """
        Contruct a new 'AbstractComp' object

        :param 
        """
        super().__init__(parent)
        self.parent = parent
        self.properties = Property()
        self.properties.appendProperty("General Properties", CompAttr.genProperty)
        self.connection = Connection(parent)
        self.firstPoint = QPoint(1, 1)
        self.parentSize = QSize(1, 1)
        self.updatedSize = QSize(1, 1)
        self.mousePressed = False
        self.resizeRadius = 5

    def getConnection(self) -> Connection:
        return self.connection

    @abstractmethod
    def getName() -> str:
        pass

    @abstractmethod
    def disableWidget() -> None:
        pass
    
    # Override
    def contextMenuEvent(self, evt: QContextMenuEvent) -> None:
        menu = QMenu(self)
        menu.addAction("Copy")
        menu.addAction("Delete")
        menu.move(evt.globalX(), evt.globalY())
        menu.show()

    @abstractmethod
    def firstTimeProp(self) -> None:
        pass

    def getPropertyTab(self) -> list:
        """
        Method that returns how the property tab should
        be setup for this instance of a button

        :param: none
        :return: list containing the layout info
        """
        self.properties["Component Name"] = self.objectName()
        self.properties["Width"] = self.width()
        self.properties["Height"] = self.height()
        self.properties["X"] = self.x()
        self.properties["Y"] = self.y()
        self.reloadProperty()
        return self.properties.getList()

    def propChanged(self) -> None:
        self.move(self.properties["X"], self.properties["Y"])
        self.setFixedSize(self.properties["Width"], self.properties["Height"])
        if (self.objectName() != self.properties["Component Name"]):
            if (not self.parent.compContains(self.objectName())):
                self.setObjectName(self.properties["Component Name"])
            else:
                msgBox = GMessageBox("Cannot Change Component Name", "This name is already taken by another component!", "Info")
                msgBox.exec()
        self.changedGeo()
        self.reconfProperty()

    def setNameChangeCallback(self, callback):
        self.nameChanged = callback

    @abstractmethod
    def reconfProperty(self):
        pass

    @abstractmethod
    def reloadProperty(self):
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

    # TODO
    def insertCalc(self, modSize):
        """
        If a component gets created with layout size different to
        the original size, this gets called to calculate the 
        resized component
        """
        self.updatedSize = modSize
        self.calcLocFromOrg(modSize)
        self.setFixedSize(int(modSize.width()/self.wratio), int(modSize.height()/self.hratio))

    # TODO
    def calcSizeFromOrg(self, size: QSize):
        self.wratio = size.width() / self.width()
        self.hratio = size.height() / self.height()

    # TODO
    def calcLocFromOrg(self, size: QSize):
        self.xratio = size.width() / self.x()
        self.yratio = size.height() / self.y()

    # TODO
    def changedGeo(self):
        if (self.parentSize != self.updatedSize):
            self.calcSizeFromOrg(self.parentSize)
            self.insertCalc(self.updatedSize)
        else:
            self.calcSizeFromOrg(self.parentSize)
            self.calcLocFromOrg(self.parentSize)

    # Override
    def mouseMoveEvent(self, evt: QMouseEvent) -> None:
        if (self.mousePressed == True):
            #self.cornerResizeCheck(evt.pos())
            pos = self.mapToParent(evt.pos())
            self.move(pos.x()-self.firstPoint.x(), pos.y()-self.firstPoint.y())

    # Override
    def mousePressEvent(self, evt: QMouseEvent) -> None:
        self.compClicked.emit(self)
        self.setCursor(Qt.CursorShape.SizeAllCursor)
        self.firstPoint = evt.pos()
        self.mousePressed = True

    # Override
    def mouseReleaseEvent(self, evt: QMouseEvent) -> None:
        self.setCursor(Qt.CursorShape.ArrowCursor)
        self.insertCalc(self.updatedSize)
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

