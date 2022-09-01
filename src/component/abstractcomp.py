"""
Author: Ian, TheLittleDoc, Fisk, Dan, Glenn
"""
import os, sys

from PyQt6.QtWidgets import QFrame, QMenu
from PyQt6 import uic
from PyQt6.QtCore import QSize, QPoint, Qt, QEvent, QObject, pyqtSignal
from PyQt6.QtGui import QMouseEvent, QContextMenuEvent
from abc import ABC, abstractmethod

PATH = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
if PATH not in sys.path:
    sys.path.append(PATH)

from component.property import Property
from component.connection import Connection
from attr import CompAttr
from proginterface import ProgInterface
from gm_resources import GMessageBox, resourcePath

class Meta(type(ABC), type(QFrame)): pass

class AbstractComp(ABC, QFrame, metaclass=Meta):
    """
    Abstract class for components. All component classes should inherit this class

    Contains implmentation requirements for a component, also contains functions that
    are required for the editor
    """

    compClicked = pyqtSignal(object) # Object should be AbstractComp
    attrChanged = pyqtSignal()

    def __init__(self, objectName, uiFile, edit, ctrlLayout):
        """
        Contruct a new 'AbstractComp' object

        :param 
        """
        super().__init__()
        self.layout = ctrlLayout
        self.properties = Property()
        self.properties.appendProperty("General Properties", CompAttr.genProperty)
        self.connection = Connection(self)
        self.firstPoint = QPoint(1, 1)
        self.parentSize = QSize(1, 1)
        self.updatedSize = QSize(1, 1)
        self.mousePressed = False
        self.resizeRadius = 5
        self.edit = edit
        self.prog = ProgInterface()

        path = resourcePath(uiFile)
        uic.loadUi(path, self) # Load the .ui file
        self.setObjectName(objectName)

        self._firstTimeProp()

    def setEditMode(self, value):
        self.edit = value

    def getConnection(self) -> Connection:
        """
        """
        return self.connection

    @abstractmethod
    def getName() -> str:
        """
        Return the type of the component
        """
        pass

    @abstractmethod
    def _firstTimeProp(self) -> None:
        """
        When the component is initialized, this is called to make
        sure the subclasses insert correct properties. This method will be
        called automatially by the this base class.

        :param: None
        :return: None
        """
        pass

    @abstractmethod
    def _reconfProperty(self):
        pass

    @abstractmethod
    def _reloadProperty(self):
        pass

    # Override
    def contextMenuEvent(self, evt: QContextMenuEvent) -> None:
        """
        """
        menu = QMenu(self)
        #menu.addAction("Copy")
        menu.addAction("Delete")
        menu.move(evt.globalX(), evt.globalY())
        menu.triggered.connect(self.menuItemSelected)
        menu.show()

    def menuItemSelected(self, action):
        match action.text():
            case "Delete":
                self.layout.removeComponent(self)

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
        if (self.connection != None):
            self.properties["Connection"] = self.connection
        self._reloadProperty()
        return self.properties.getFormPropDict()

    def propChanged(self):
        self.move(self.properties["X"], self.properties["Y"])
        self.setFixedSize(self.properties["Width"], self.properties["Height"])
        if (self.objectName() != self.properties["Component Name"]):
            if (not self.prog.compContains(self.properties["Component Name"])):
                self.prog.nameChanged(self.objectName(), self.properties["Component Name"])
                self.setObjectName(self.properties["Component Name"])
                self.attrChanged.emit()
            else:
                msgBox = GMessageBox("Cannot Change Component Name",
                 "This name is already taken by another component!", "Info")
                msgBox.exec()
                self.properties["Component Name"] = self.objectName()
                self.attrChanged.emit()

        self._reconfProperty()

    def setNameChangeCallback(self, callback):
        self.nameChanged = callback

    def sizeInit(self, size: QSize) -> None:
        """
        When the size or position of either the component
        is initialized or changed, 
        this must be called in order to have a relative sizing
        when resized. Ratio is used for future calculation.

        :param: size of the parent widget
        :return: none
        """
        pass
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
            pos = self.mapToParent(evt.pos())
            self.move(pos.x()-self.firstPoint.x(), pos.y()-self.firstPoint.y())

    # Override
    def mousePressEvent(self, evt: QMouseEvent) -> None:
        if (self.edit):
            self.compClicked.emit(self)
            self.setCursor(Qt.CursorShape.SizeAllCursor)
            self.firstPoint = evt.pos()
            self.mousePressed = True

    # Override
    def mouseReleaseEvent(self, evt: QMouseEvent) -> None:
        if (self.edit):
            self.setCursor(Qt.CursorShape.ArrowCursor)
            #self.insertCalc(self.updatedSize) TODO
            self.boundaryCheck(self.pos())
            self.properties["Width"] = self.width()
            self.properties["Height"] = self.height()
            self.properties["X"] = self.x()
            self.properties["Y"] = self.y()
            self.attrChanged.emit()
            self.mousePressed = False

    def boundaryCheck(self, pos):
        if (pos.x() <= 0):
            self.move(1, pos.y())

        if (pos.y() <= 0):
            self.move(self.x(), 1)

        if (pos.x() + self.width() >= self.parentSize.width()):
            self.move(self.parentSize.width()-self.width(), pos.y())

        if (pos.y() + self.height() >= self.parentSize.height()):
            self.move(self.x(), self.parentSize.height()-self.height())

    # TODO
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

    def checkBoundary(self, pos) -> bool:
        pass

    def eventFilter(self, obj: QObject, evt: QEvent) -> bool:
        if (evt.type() == QEvent.Type.MouseMove):
            self.mouseMoveEvent(evt)
        elif (evt.type() == QEvent.Type.MouseButtonPress):
            self.mousePressEvent(evt)
        elif (evt.type() == QEvent.Type.MouseButtonRelease):
            self.mouseReleaseEvent(evt)
        return False 

    # MIGHT CHANGE IN THE FUTURE
    def getSaveProp(self) -> dict:
        self.getPropertyTab()
        return self.properties.getAllPropDict()

    # MIGHT CHANGE IN THE FUTURE
    def setOneProp(self, attr, value):
        self.properties[attr] = value
