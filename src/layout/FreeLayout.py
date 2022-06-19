# This Python file uses the following encoding: utf-8
from PyQt6.QtWidgets import QLayout

class FreeLayout(QLayout):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.items = [] # QLayoutItem List
        self.space = -1

    #Override
    def addItem(self, item):
        self.items.append(item)

    #Override
    def count(self):
        return len(self.items)

    #Override
    def indexOf(self, item):
        return self.items.index(item)

    #Override
    def itemAt(self, index):
        if (index < self.count()):
            return self.items[index]

    #Override
    def replaceWidget(self, fr, to, option = None): # This should only change one widget
        for item in self.items:
            if (item.widget() == fr):
                self.items[self.indexOf(item)] = to
                return item
            else:
                replacedItem = item.widget().layout().replaceWidget(fr, to)
                if (replacedItem != None):
                    return replacedItem

    #Override
    def setSpacing(self, value): # Check documentation
        self.space = value

    def spacing(self):
        return self.space

    def takeAt(self, index):
        self.items.remove(index)
