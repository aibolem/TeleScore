# Form implementation generated from reading ui file 'c:\Users\Ian\OneDrive - ualberta.ca\Documents\Scoreboard\src\editor\complist.ui'
#
# Created by: PyQt6 UI code generator 6.3.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(592, 440)
        self.gridLayout = QtWidgets.QGridLayout(Form)
        self.gridLayout.setObjectName("gridLayout")
        self.categoryTab = QtWidgets.QTabWidget(Form)
        self.categoryTab.setTabPosition(QtWidgets.QTabWidget.TabPosition.West)
        self.categoryTab.setTabShape(QtWidgets.QTabWidget.TabShape.Rounded)
        self.categoryTab.setElideMode(QtCore.Qt.TextElideMode.ElideNone)
        self.categoryTab.setObjectName("categoryTab")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.categoryTab.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.categoryTab.addTab(self.tab_2, "")
        self.gridLayout.addWidget(self.categoryTab, 0, 1, 1, 1)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.categoryTab.setTabText(self.categoryTab.indexOf(self.tab), _translate("Form", "Tab 1"))
        self.categoryTab.setTabText(self.categoryTab.indexOf(self.tab_2), _translate("Form", "Tab 2"))
