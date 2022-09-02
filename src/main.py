"""
Author: Ian, TheLittleDoc, Fisk, Dan, Glenn
"""

import sys
from PyQt6.QtWidgets import QApplication

try:
    from gm_resources import resourcePath
    from window.mainwindow import MainWindow
except:
    import src
    sys.path.append(src.CURR_PATH)
    from gm_resources import resourcePath
    from window.mainwindow import MainWindow


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    with open(resourcePath("src/theme/fisk.qss"), 'r') as stream:
        style = stream.read()
        window.setStyleSheet(style)

    sys.exit(app.exec())
    