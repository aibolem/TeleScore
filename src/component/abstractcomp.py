"""
Developed by: JumpShot Team
Written by: riscyseven
"""

from PyQt6.QtWidgets import QFrame, QMenu
from PyQt6 import uic
from PyQt6.QtCore import QPoint, Qt, QEvent, QObject, pyqtSignal, QSize
from PyQt6.QtGui import QMouseEvent, QContextMenuEvent
from abc import ABC, abstractmethod

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
        super().__init__()
        self.layout = ctrlLayout
        self.properties = Property()
        self.properties.appendProperty("General Properties", CompAttr.genProperty)
        self.connection = Connection(self)
        self.firstPoint = QPoint(1, 1)
        self.parentSize = QSize(1, 1)
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
    def _firstTimeProp(self):
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
    def contextMenuEvent(self, evt: QContextMenuEvent):
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
        self.properties["Width"] = self.origSize.width()
        self.properties["Height"] = self.origSize.height()
        self.properties["X"] = self.x()
        self.properties["Y"] = self.y()
        if (self.connection != None):
            self.properties["Connection"] = self.connection
        self._reloadProperty()
        return self.properties.getFormPropDict()

    def propChanged(self):
        self.move(self.properties["X"], self.properties["Y"])
        self.setFixedSize(self.properties["Width"], self.properties["Height"])
        self.origSize = QSize(self.properties["Width"], self.properties["Height"])

        self.setModLoc(self.currParSize)
        self.setModSize(self.origParSize, self.currParSize)

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

    # Scenario 1
    def initRatio(self, origSize: QSize, currSize: QSize):
        """
        When the component is first dropped to the layout, we must calculate
        the ratio for location and size to the ctrl layout in order for resizing to work.

        :param origSize: QGeometry object that contains location and size
        """
        self.origSize = self.size()
        self.origParSize = origSize
        self.currParSize = currSize
        self.setLocRatio(currSize)
        self.setSizeRatio(origSize)
        
        self.setModSize(origSize, currSize)

    def setModSize(self, origSize: QSize, currSize: QSize):
        self.setSizeRatio(origSize)

        self.setFixedSize(int(currSize.width() * self.wratio),
         int(currSize.height() * self.hratio))

    def setModLoc(self, currSize: QSize):
        self.setLocRatio(currSize)

    def setLocRatio(self, parentGeo: QSize):
        """
        Anytime location is changed, this must be called
        """
        self.xratio = self.x() / parentGeo.width()
        self.yratio = self.y() / parentGeo.height()

    def setSizeRatio(self, parentGeo: QSize):
        """
        Anytime size is changed, this must be called
        """
        self.wratio = self.width() / parentGeo.width()
        self.hratio = self.height() / parentGeo.height()

    def parentResized(self, currSize: QSize):
        aWidth = int(currSize.width() * self.wratio)
        aHeight = int(currSize.height() * self.hratio)
        aX = int(currSize.width() * self.xratio)
        aY = int(currSize.height() * self.yratio)

        self.setFixedSize(aWidth, aHeight)
        self.move(aX, aY)

        self.currParSize = currSize

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
            self.boundaryCheck(self.pos())
            self.properties["X"] = self.x()
            self.properties["Y"] = self.y()
            self.setModLoc(self.currParSize)
            self.attrChanged.emit()
            self.mousePressed = False

    def boundaryCheck(self, pos):
        if (pos.x() <= 0):
            self.move(1, pos.y())

        if (pos.y() <= 0):
            self.move(self.x(), 1)

        if (pos.x() + self.width() >= self.currParSize.width()):
            self.move(self.currParSize.width()-self.width(), pos.y())

        if (pos.y() + self.height() >= self.currParSize.height()):
            self.move(self.x(), self.currParSize.height()-self.height())

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
