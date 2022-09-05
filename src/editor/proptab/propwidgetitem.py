"""
Developed By: JumpShot Team
Written by: riscyseven
"""

from PyQt6.QtWidgets import QWidget, QLineEdit, QSpinBox, QFontComboBox, QCheckBox, QPushButton
from PyQt6.QtGui import QFont, QStandardItem
from PyQt6.QtCore import Qt

from attr import CompAttr
from editor.connection.connman import ConnMan
from editor.proptab.propwidgethead import PropWidgetHead
from editor.proptab.fileseldialog import FileSelDialog
from editor.connection.hotkeyman import HotkeyMan

class PropWidgetItem(QStandardItem):
    """
    Each component listed in the component list is made from 
    this class object. This widget item will standardize attributes
    such as the fonts, icon image size, etc.
    """

    def __init__(self, parent: PropWidgetHead, propName: str, propType: str,
     propValue: str):
        """
        Consturctor for a component list item

        :param icon: Icon for the component
        :param parent: Header/category of the item
        :param treeWidget: Main component list widget
        :param text: Description of the component

        :return: none
        """
        super().__init__(parent) # This sets this component to be the subcomponent of the header
        self.role = Qt.ItemDataRole.DisplayRole; # All the items are for displaying
        self.setText(propName)
        self.setTextAlignment(Qt.AlignmentFlag.AlignCenter | Qt.AlignmentFlag.AlignVCenter)
        self.setFont(QFont("Open Sans Bold", 11))
        self.editWidget = self._createProp(propType, propValue)
        self.extraInfo = None

    def getWidget(self) -> QWidget:
        return self.editWidget

    def setCallBack(self, changed):
        self.callBack = changed

    def _spinBoxChanged(self, value: int):
        self.callBack(self, value)

    def _lineEditChanged(self):
        self.callBack(self, self.editWidget.text())

    def _fontEditChanged(self, font: QFont) -> None:
        self.callBack(self, font.family())

    def _checkBoxChanged(self, checked):
        self.callBack(self, checked)

    def _fileSctClicked(self, fileName):
        self.callBack(self, fileName)

    def _hotKeyFinished(self, hotKey):
        self.callBack(self, hotKey)

    def _createProp(self, text: object, value) -> QWidget:
        wid = None
        match text:
            case CompAttr.TEXTEDIT:
                wid = self._createTextEdit(value)
            case CompAttr.NUMEDIT:
                wid = self._createNumEdit(value)
            case CompAttr.FONTEDIT:
                wid = self._createFontEdit(value)
            case CompAttr.CONNEDIT:
                wid = self._createConnMan(value)
            case CompAttr.CHECKBOX:
                wid = self._createCheckBox(value)
            case CompAttr.FLSAVE | CompAttr.FLOPEN:
                wid = self._createFileSct(text, value)
            case CompAttr.HOTEDIT:
                wid = self._createHotKeyMan(value)
        return wid

    def extraInfo(self, value):
        self.extraInfo = value

    def _createTextEdit(self, value) -> None:
        """
        Creates a new QLineEdit widget to insert
        to the treeview

        :param: none (might change in the future for some attribute changes)
        :return: none
        """
        lineEdit = QLineEdit(value)
        lineEdit.editingFinished.connect(self._lineEditChanged)
        return lineEdit

    def _createFontEdit(self, value):
        """
        Creates a new QPushButton widget to insert
        to the treeview, this pushbutton will open a font dialog

        :param: none (might change in the future for some attribute changes)
        :return: none
        """
        edit = QFontComboBox()
        edit.setDisplayFont(value, edit.currentFont())
        edit.currentFontChanged.connect(self._fontEditChanged)
        return edit

    def _createNumEdit(self, value) -> QSpinBox:
        """
        Creates a new QSpinbox widget to insert
        to the treeview. Restricted to only numbers

        :param: none (might change in the future for some attribute changes)
        :return: none
        """
        spinBox = QSpinBox()
        spinBox.setMinimum(0)
        spinBox.setMaximum(9999999)

        spinBox.setValue(value)
            
        spinBox.valueChanged.connect(self._spinBoxChanged)
        return spinBox

    def _createCheckBox(self, value) -> QCheckBox:
        wid = QCheckBox()
        wid.setChecked(value)
        wid.stateChanged.connect(self._checkBoxChanged)
        return wid

    def _createFileSct(self, mode, value) -> QPushButton:
        wid = FileSelDialog(mode, self._fileSctClicked, value)
        self.fileName = value
        return wid

    def _createConnMan(self, value):
        name = value[0]
        data = value[1]
        wid = ConnMan(name, data)
        return wid

    def _createHotKeyMan(self, value):
        wid = HotkeyMan(value, self._hotKeyFinished)
        return wid