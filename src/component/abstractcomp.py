from PyQt6.QtWidgets import QFrame
from abc import ABC, abstractmethod

class AbstractComp(ABC, QFrame):
    def __init__(self, *args):
        super().__init__(self)

