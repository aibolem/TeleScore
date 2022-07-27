"""
Author: Ian, TheLittleDoc, Fisk, Dan, Glenn
"""

from abc import ABC, abstractmethod

class AbstractCmd(ABC):
    """
    Interface used by the invoker.
    Every command should inherit this abstract class
    """

    @abstractmethod
    def execute() -> None:
        pass
