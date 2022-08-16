"""
Author: Ian, TheLittleDoc, Fisk, Dan, Glenn
"""

import os, sys
import window
from PyQt6.QtWidgets import QApplication

PATH = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
if PATH not in sys.path:
    sys.path.append(PATH)

from window.mainwindow import MainWindow

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    with open(PATH + "\\Cooliguay Kawaii Edition.qss", 'r') as stream:
        style = stream.read()
        window.setStyleSheet(style)

    sys.exit(app.exec())