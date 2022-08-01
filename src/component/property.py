from .compattr import CompAttr
from copy import deepcopy

class Property:
    """
    A wrapper class that wraps dictionary but
    includes more features for properties tab
    """

    def __init__(self):
        self.formattedProp = {}
        self.allProp = {}   # Contains all the properties, these values are referenced from formatted Prop

    def appendProperty(self, name:str, prop: dict):
        copied = deepcopy(prop) # This is done to avoid referencing issues
        self.formattedProp[name] = {CompAttr.PROPERTIES: copied}
        self._expandProp(copied)

    def _expandProp(self, prop):
        for i in prop:  # i is the key/name of each property
            self.allProp[i] = prop[i]

    def removeProperty(self, name) -> None:
        for i in self.formattedProp[name][CompAttr.PROPERTIES]:
            self.allProp.pop(i)
        self.formattedProp.pop(name)

    def changeValue(self, attr: str, value: object) -> None:
        self.allProp[attr][CompAttr.VALUE] = value

    def getValue(self, attr) -> object:
        if (attr not in self.allProp):
            return None
        return self.allProp[attr][CompAttr.VALUE]

    def getAll(self) -> dict:
        return self.allProp

    def getList(self) -> dict:
        return self.formattedProp
