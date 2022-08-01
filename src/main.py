"""
Author: Ian, TheLittleDoc, Fisk, Dan, Glenn
"""

import sys

from PyQt6.QtWidgets import QApplication
from PyQt6.QtCore import QTimer
from window.mainwindow import MainWindow

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    
    sys.exit(app.exec())