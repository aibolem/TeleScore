# Form implementation generated from reading ui file 'c:\Users\Ian\OneDrive - ualberta.ca\Documents\Scoreboard\src\editor\complisttab.ui'
#
# Created by: PyQt6 UI code generator 6.3.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(243, 204)
        self.gridLayout = QtWidgets.QGridLayout(Form)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName("gridLayout")
        self.treeView = QtWidgets.QTreeView(Form)
        self.treeView.setDragEnabled(True)
        self.treeView.setDragDropMode(QtWidgets.QAbstractItemView.DragDropMode.DragOnly)
        self.treeView.setIconSize(QtCore.QSize(50, 50))
        self.treeView.setIndentation(0)
        self.treeView.setObjectName("treeView")
        self.treeView.header().setVisible(False)
        self.gridLayout.addWidget(self.treeView, 0, 0, 1, 1)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
