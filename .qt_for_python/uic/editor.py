# Form implementation generated from reading ui file 'c:\Users\Ian\OneDrive - ualberta.ca\Documents\Scoreboard\src\window\ui\editor.ui'
#
# Created by: PyQt6 UI code generator 6.3.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(788, 481)
        MainWindow.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        MainWindow.setStyleSheet("")
        MainWindow.setTabShape(QtWidgets.QTabWidget.TabShape.Rounded)
        MainWindow.setDockNestingEnabled(False)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        MainWindow.setCentralWidget(self.centralwidget)
        self.compDock = QtWidgets.QDockWidget(MainWindow)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.MinimumExpanding, QtWidgets.QSizePolicy.Policy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.compDock.sizePolicy().hasHeightForWidth())
        self.compDock.setSizePolicy(sizePolicy)
        self.compDock.setMinimumSize(QtCore.QSize(278, 42))
        self.compDock.setStyleSheet("")
        self.compDock.setFeatures(QtWidgets.QDockWidget.DockWidgetFeature.DockWidgetFloatable|QtWidgets.QDockWidget.DockWidgetFeature.DockWidgetMovable)
        self.compDock.setObjectName("compDock")
        self.compDockContents = QtWidgets.QWidget()
        self.compDockContents.setObjectName("compDockContents")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.compDockContents)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.compDock.setWidget(self.compDockContents)
        MainWindow.addDockWidget(QtCore.Qt.DockWidgetArea(1), self.compDock)
        self.propDock = QtWidgets.QDockWidget(MainWindow)
        self.propDock.setMinimumSize(QtCore.QSize(318, 113))
        self.propDock.setStyleSheet("")
        self.propDock.setFeatures(QtWidgets.QDockWidget.DockWidgetFeature.DockWidgetFloatable|QtWidgets.QDockWidget.DockWidgetFeature.DockWidgetMovable)
        self.propDock.setObjectName("propDock")
        self.dockWidgetContents_8 = QtWidgets.QWidget()
        self.dockWidgetContents_8.setObjectName("dockWidgetContents_8")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.dockWidgetContents_8)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.tableWidget = QtWidgets.QTableWidget(self.dockWidgetContents_8)
        self.tableWidget.setMinimumSize(QtCore.QSize(250, 0))
        self.tableWidget.setBaseSize(QtCore.QSize(0, 0))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.gridLayout_3.addWidget(self.tableWidget, 0, 0, 1, 1)
        self.propDock.setWidget(self.dockWidgetContents_8)
        MainWindow.addDockWidget(QtCore.Qt.DockWidgetArea(2), self.propDock)
        self.actionNew = QtGui.QAction(MainWindow)
        self.actionNew.setObjectName("actionNew")
        self.actionOpen = QtGui.QAction(MainWindow)
        self.actionOpen.setObjectName("actionOpen")

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.compDock.setWindowTitle(_translate("MainWindow", "Components"))
        self.propDock.setWindowTitle(_translate("MainWindow", "Properties"))
        self.actionNew.setText(_translate("MainWindow", "New"))
        self.actionOpen.setText(_translate("MainWindow", "Open"))
