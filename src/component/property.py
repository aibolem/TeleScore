"""
Author: Ian, TheLittleDoc, Fisk, Dan, Glenn
"""

import os, sys

from copy import deepcopy

PATH = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
if PATH not in sys.path:
    sys.path.append(PATH)

from attr import CompAttr

class Property:
    """
    A wrapper class that wraps dictionary but
    includes more features for properties tab
    """

    def __init__(self):
        self.formattedProp = {}
        self.allProp = {}   # Contains all the properties, these values are referenced from formatted Prop

    def __getitem__(self, key):
        return self.getValue(key)

    def __setitem__(self, key, value):
        self.changeValue(key, value)

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

    def changeValue(self, key: str, value: object) -> None:
        if (key in self.allProp):
            self.allProp[key][CompAttr.VALUE] = value

    def getValue(self, attr) -> object:
        if (attr not in self.allProp):
            return None
        return self.allProp[attr][CompAttr.VALUE]

    def getAll(self) -> dict:
        return self.allProp

    def getList(self) -> dict:
        return self.formattedProp
