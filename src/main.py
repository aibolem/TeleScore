"""
Developed by: JumpShot Team
Written by: riscyseven, TheLittleDoc
Designed by: Fisk31, TheLittleDoc
"""

import sys
from PyQt6.QtWidgets import QApplication

try:
    from gm_resources import resourcePath, GMessageBox
    from window.mainwindow import MainWindow
except:
    import src
    sys.path.append(src.CURR_PATH)
    from gm_resources import resourcePath
    from window.mainwindow import MainWindow

class Application:
    def __init__(self):
        self.app = QApplication(sys.argv)
        self.window = MainWindow()
        with open(resourcePath("src/theme/fisk.qss"), 'r') as stream:
            style = stream.read()
            self.window.setStyleSheet(style)

    def raise_error(Self):
        assert False


def excepthook(eType, eValue, eTb):
    msg = GMessageBox("Unhandled Exception", "Uh Oh!\nUnhandled Exception Caught!\nReason:\n{}\n{}".format(eType, eValue), "Info")
    msg.exec()
    QApplication.exit(0)

if __name__ == "__main__":
    sys.excepthook = excepthook
    exception = Application()
    ret = exception.app.exec()
    sys.exit(ret)
    
