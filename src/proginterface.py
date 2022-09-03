"""
Developed By: JumpShot Team
Written by: riscyseven
"""

class ProgInterface(object):
    """
    Class that contains all the current program information

    Might refractor/remove this in the future since this is a singleton class
    and me no like singleton :(. This might also limit only having one single
    control layout
    """
    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(ProgInterface, cls).__new__(cls)
        return cls.instance

    compDict = {}

    def setAllComponent(self, value) -> None:
        self.compDict = value

    def getAllComponent(self) -> list:
        return self.compDict

    def getComponent(self, name: str):
        return self.compDict[name]

    def nameChanged(self, oldName, newName):
        old = self.compDict[oldName]
        self.compDict[newName] = old
        del self.compDict[oldName]

    def compContains(self, name: str) -> bool:
        return name in self.compDict
