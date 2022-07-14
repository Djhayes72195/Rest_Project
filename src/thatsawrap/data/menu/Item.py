"""The Item interface.

This file contains the code required to
create an interface which all drinks, sides,
and wraps will inherit from.

Author: Dustin Hayes djhayes@ksu.edu
Version 0.1
"""
import abc
from typing import List


class Item(metaclass=abc.ABCMeta):
    """Item class.

    This class defines the behaviors that
    each inheriting class should have.
    """
    @classmethod
    def __subclasshook__(cls, subclass: type) -> bool:
        """Checks that inheriting class is compatible.

        This method accepts the class itself and
        a subclass to check against.  This method
        requires that each inheriting class has
        attributes price, calories and instructions.

        Args:
            cls: a reference to the Item class
            subclass: a reference to the inheriting class

        Returns:
            True if the inheriting class has attributes
            functional attributes called price, calories
            and instructions, false otherwise.
        """
        if cls is Item:
            attrs: List[str] = ['price', 'calories', 'instructions']
            callables: List[str] = []
            ret = True
            for atr in attrs:
                ret = ret and (hasattr(subclass, atr) and
                               isinstance(getattr(subclass, atr), property))
            for call in callables:
                ret = ret and (hasattr(subclass, call)
                               and callable(getattr(subclass, call)))
            return ret
        else:
            return NotImplemented

    @property
    @abc.abstractmethod
    def price(self) -> float:
        """Abstract getter for price."""
        raise NotImplementedError

    @property
    @abc.abstractmethod
    def calories(self) -> int:
        """Abstract getter for calories."""
        raise NotImplementedError

    @property
    @abc.abstractmethod
    def instructions(self):
        """Abstract getter for instructions."""
        raise NotImplementedError
