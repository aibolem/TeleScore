"""
Developed by: JumpShot Team
Written by: riscyseven
UI designed by: Fisk31
"""

from PyQt6.QtGui import QColor

from attr import CompAttr
from component.abstractcomp import AbstractComp
from component.hotkey import HotKey

class ButtonComp(AbstractComp):
    """
    Button widget for scoreboard.
    """
    
    def __init__(self, type, text, signal: str, objectName, edit=False, parent=None):
        super().__init__(objectName, "src/component/basiccomp/buttoncomp.ui", edit, parent)

        self.signal = signal
        self.buttonType = type
        self.text = text
        self.hotKey = None
        self.setStyleSheet("QPushButton {border: none; color: white; \
         font-size: 17px; border-radius: 4px;}")
        self.pushButton.setText(text)
        self.pushButton.clicked.connect(self._onClick)
        self.connection.appendConnType(self.signal)

        if (edit == True):
            self.pushButton.installEventFilter(self)

    # Override
    def _firstTimeProp(self):
        self.properties.appendProperty("Appearance Properties", CompAttr.appearProperty)
        self.properties.appendProperty("Hotkey Properties", CompAttr.hotkeyProperty)
        self.properties.appendProperty("Connection Properties", CompAttr.connProperty)

    # Override
    def _reloadProperty(self):
        self.properties["Display Text"] = self.pushButton.text()
        self.properties["Display Font"] = self.pushButton.font().family()
        self.properties["Font Size"] = self.pushButton.font().pixelSize()

    # Override
    def _reconfProperty(self):
        self.pushButton.setStyleSheet("font-size: {}px;\
            font-family: {}".format(self.properties["Font Size"], self.properties["Display Font"]))
        self.pushButton.setText(self.properties["Display Text"])

        if (self.hotKey != None):
            self.hotKey.signal.disconnect(self._onClick)
            self.hotKey.stopThread()
            self.hotKey = None
        if (self.properties["Hotkey"] != ""):    
            self.hotKey = HotKey(self.properties["Hotkey"])
            self.hotKey.signal.connect(self._onClick)

    # Override
    def getName(self) -> str:
        return self.buttonType

    # Override
    def setFileDir(self, dirName):
        pass

    def _onClick(self):
        self.connection.emitSignal(self.signal)

    def setButtonColor(self, hexval: str):
        """
        Method that automatically determines the button colour for hover
        and press actions.

        :param hexval: String hex value "#ffffff"
        :return: None
        """
        dimmed = QColor(hexval)
        dimmed.setRgb(dimmed.red() // 2, dimmed.green() // 2, dimmed.blue() // 2)
        self.setStyleSheet(self.styleSheet() +
                             "QPushButton {background-color: " +
                            hexval + ";}" + 
                            "QPushButton:pressed{background-color: " + 
                             dimmed.name(QColor.NameFormat.HexRgb) + ";}" +
                            "QPushButton:hover{color: #e8e8e8;}")
