import sys
from pynput import keyboard
from PyQt6.QtCore import pyqtSignal
from PyQt6.QtCore import QObject

class HotKey(QObject):
    keys = ["Ctrl", "Alt", "Shift", "Space"]
    signal = pyqtSignal()

    def __init__(self, hotKey):
        super().__init__(None)
        if (sys.platform == "win32"):
            # PUT A TRY AND CATCH STATEMENT FOR HOTKEYS THAT DOESN'T WORK
            try:
                hotKey = keyboard.HotKey.parse(self.translateKey(hotKey))
            except Exception:
                return

            key = keyboard.HotKey(
                hotKey,
                self.onPress
            )
            self.listener = keyboard.Listener(
                on_press=self.for_canonical(key.press),
                on_release=self.for_canonical(key.release)
            )
            self.listener.start()

    def for_canonical(self, f):
        return lambda k: f(self.listener.canonical(k))

    def translateKey(self, key: str) -> str:
        for modKey in self.keys:
            if (modKey in key):
                newKey = "<{}>".format(modKey.lower())
                key = key.replace(modKey, newKey)
        return key

    def stopThread(self):
        if (sys.platform == "win32"):
            self.listener.stop()

    def onPress(self):
        self.signal.emit()

    def onRelease(self):
        pass