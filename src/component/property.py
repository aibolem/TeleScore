"""
Developed by: JumpShot Team
Written by: riscyseven
"""

from copy import deepcopy
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
        """
        Get the value of the property, this value can be any type of object
        NOTE: Developers can use "[]" instead

        :param attr: 
        """
        if (attr not in self.allProp):
            return None
        return self.allProp[attr][CompAttr.VALUE]

    def getAllPropDict(self) -> dict:
        """
        Returns a dictionary that contains each property name as key
        and the property value

        :param: None
        :return: Dictionary that contains all properties
        """
        return self.allProp

    def getFormPropDict(self) -> dict:
        """
        Returns a formatted dictionary that contains the property header, it's
        content, and the value of each property. This should be mostly used for
        the property tab. 

        :param: None
        :return: Dictionary that contains formatted properties
        """
        return self.formattedProp
