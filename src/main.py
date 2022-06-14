import sys

from PyQt6 import QtWidgets, uic
from window.mainwindow import MainWindow

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    app.exec()