"""
Developed By: JumpShot Team
Written by: riscyseven
"""

from PyQt6.QtWidgets import QMainWindow, QFrame, QFileDialog, QPushButton
from PyQt6 import uic, QtGui
from PyQt6.QtCore import QPoint, pyqtSlot, QSize, Qt
from gm_resources import resourcePath

from component.abstractcomp import AbstractComp
from editor.complisttab import CompListTab
from editor.propertytab import PropertyTab
from editor.command.insertcmd import InsertCmd
from editor.globaldirectory import GlobalDirectory
from layout.ctrllayout import CtrlLayout
from fileio.layoutfile import LayoutFile
from proginterface import ProgInterface

class Editor(QMainWindow):
    def __init__(self, layout=None, file=None, parent=None):
        super().__init__(parent) # Call the inherited classes __init__ method

        self.cmdStack = QtGui.QUndoStack(self) # Command stack used for undo/redo
        self.currComp = None
        
        # Check to see if we are creating or loading a layout
        self.layoutFile = file
        if (layout == None):
            self.ctrl = CtrlLayout(QSize(1000, 600), self._remCallBack, self)
        else:
            self.ctrl = layout
            self.ctrl.setRemoveCallBack(self._remCallBack)
            self._loadExistingComp()

        self.ctrl.dropSignal.connect(self._dropSlot)

        self._initUI()

    def _loadExistingComp(self):
        for comp in self.ctrl.getComponents().values():
            comp.compClicked.connect(self._compClicked)
            comp.setEditMode(True)

    def _initUI(self) -> None:
        """
        Initializes the editor UI.

        :param: none
        :return: none
        """
        path = resourcePath("src/window/ui/editor.ui")
        uic.loadUi(path, self) # Load the .ui file

        self.comp = CompListTab(self)
        self.compDock.setWidget(self.comp)

        self.prop = PropertyTab(self)
        self.propDock.setWidget(self.prop)

        self.ctrl.setFrameShape(QFrame.Shape.Box)
        self.setCentralWidget(self.ctrl)

        # Setting up the toolbar

        # This is a bit redundant. If there is a simpler way of doing this, please change it.
        self.toolBar.addWidget(QPushButton(QtGui.QIcon(resourcePath("src/resources/icon.ico")),
         " TeleScore v1.0"))
        self.toolBar.addSeparator()
        self.globalPushButton = QPushButton("Set Component File Output Folder")
        self.toolBar.addWidget(self.globalPushButton)
        self.globalPushButton.clicked.connect(self._setGlobalFolder)

    @pyqtSlot(object)
    def _compClicked(self, comp: AbstractComp) -> None:
        """
        If any of the component is clicked, this
        slot gets called. This should process the property
        tab initiation. Get the property of the component
        and pass it onto the property tab.

        :param comp: Component that has been clicked
        :return: none
        """
        if (self.currComp != comp):
            self.clearCurrComp()
            self.prop.propChanged.connect(comp.propChanged)
            self.prop.loadProperties(comp.getPropertyTab())
            comp.attrChanged.connect(self.prop.externalChange)
            comp.setFrameShape(QFrame.Shape.Box)
            comp.setLineWidth(3)

        self.currComp = comp

    def clearCurrComp(self):
        self.prop.clearTree()
        if (self.currComp != None):
            self.prop.propChanged.disconnect(self.currComp.propChanged)
            self.currComp.attrChanged.disconnect(self.prop.externalChange)
            self.currComp.setFrameShape(QFrame.Shape.NoFrame)
            self.currComp = None

    @pyqtSlot(QtGui.QDropEvent)
    def _dropSlot(self, evt: QtGui.QDropEvent) -> None:
        """
        When component is dropped from the components list, 
        this is called and adds the right component to the layout

        :param evt: event information
        :return: none
        """
        type = evt.mimeData().data("application/x-comp").data().decode()
        point = QPoint(int(evt.position().x()), int(evt.position().y()))
        insert = InsertCmd(self.ctrl, type, point)
        self.cmdStack.push(insert)

        comp = insert.getComponent()
        comp.compClicked.connect(self._compClicked)

    def _remCallBack(self, component: AbstractComp):
        if (self.currComp == component):
            self.prop.propChanged.disconnect(self.currComp.propChanged)
            self.currComp.attrChanged.disconnect(self.prop.externalChange)
            self.currComp = None
            self.prop.clearTree()
        component.compClicked.disconnect(self._compClicked)

    def saveAction(self):
        if (self.layoutFile != None):
            self.layoutFile.save()
        else:
            self.saveAsAction()
        
    def saveAsAction(self):
        file = QFileDialog.getSaveFileName(self, "Save Layout File As", ".", "JSON File (*.json)")
        if (file[0] != '' and file[1] != ''): 
            self.layoutFile = LayoutFile(file[0], self.ctrl)
            self.layoutFile.save()

    # Override
    def keyPressEvent(self, evt: QtGui.QKeyEvent) -> None:
        '''if (evt.modifiers() & Qt.KeyboardModifier.ControlModifier):
            match evt.key():
                case Qt.Key.Key_Z:
                    self.cmdStack.undo()'''
        if (evt.modifiers() & Qt.KeyboardModifier.ControlModifier):
            match evt.key():
                case Qt.Key.Key_S:
                    self.saveAction()

        evt.accept()

    def _setGlobalFolder(self):
        progInt = ProgInterface()
        directory = GlobalDirectory(progInt.getDefaultFileDir().replace("/{}", ""), self)
        directory.exec()

        dirName = directory.getDirectory()
        
        if (dirName != ""):
            progInt.setDefaultFileDir(dirName + "/{}")
            # Check for valid directory
            components = self.ctrl.getComponents()
            for comp in components.values():
                comp.setFileDir(dirName + "/{}")

        self.clearCurrComp()