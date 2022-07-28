"""
Author: Ian, TheLittleDoc, Fisk, Dan, Glenn
"""

from PyQt6.QtWidgets import QWidget, QLineEdit, QSpinBox
from PyQt6.QtGui import QFont, QStandardItem, QColor
from PyQt6.QtCore import Qt, pyqtSignal, pyqtSlot, QObject
from .propwidgethead import PropWidgetHead
from gm_resources import *

PATH = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
if PATH not in sys.path:
    sys.path.append(PATH)

from component.compattr import CompAttr

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
        self.setBackground(QColor(255, 255, 255))
        self.editWidget = self._createProp(propType, propValue)

    def getWidget(self) -> QWidget:
        return self.editWidget

    def setCallBack(self, changed):
        self.callBack = changed

    def _spinBoxChanged(self, value: int):
        self.callBack(self)

    def _lineEditChanged(self, text: str):
        pass

    def _createProp(self, text: str, value) -> QWidget:
        wid = None
        match text:
            case CompAttr.TEXTEDIT:
                wid = self._createTextEdit(value)
            case CompAttr.NUMEDIT:
                wid = self._createNumEdit(value)
        return wid

    def _createTextEdit(self, value) -> None:
        """
        Creates a new QLineEdit widget to insert
        to the treeview

        :param: none (might change in the future for some attribute changes)
        :return: none
        """
        lineEdit = QLineEdit(value)
        return lineEdit

    def _createFontEdit(self, value):
        """
        Creates a new QPushButton widget to insert
        to the treeview, this pushbutton will open a font dialog

        :param: none (might change in the future for some attribute changes)
        :return: none
        """
        pass

    def _createNumEdit(self, value) -> QSpinBox:
        """
        Creates a new QSpinbox widget to insert
        to the treeview. Restricted to only numbers

        :param: none (might change in the future for some attribute changes)
        :return: none
        """
        spinBox = QSpinBox()
        spinBox.setMinimum(1)
        spinBox.setMaximum(9999999)
        try:
            spinBox.setValue(int(value))
        except ValueError:
            spinBox.setValue(1)
            
        spinBox.valueChanged.connect(self._spinBoxChanged)
        return spinBox
