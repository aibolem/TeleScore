# This Python file uses the following encoding: utf-8
from PyQt6.QtWidgets import QLayout

class FreeLayout(QLayout):
    def __init__(self):
        super(self)
        self.item = []

    def addItem(self, arg__1):
        raise NotImplementedError;

    def count(self):
        raise NotImplementedError;

    def indexOf(self, arg__1):
        raise NotImplementedError;

    def itemAt(index):
        raise NotImplementedError;

    def replaceWidget(fr, to):
        raise NotImplementedError;

    def setSpacing(arg__1):
        raise NotImplementedError;

    def spacing():
        raise NotImplementedError;

    def takeAt(index):
        raise NotImplementedError;
