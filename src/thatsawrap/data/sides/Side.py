"""Side superclass.

This file contains the code that defines an
instance of a side item according to their
shared characteristics and includes their
shared functionality.

Author: Dustin Hayes djhayes@ksu.edu
Version 0.1
"""
from typing import List
from src.thatsawrap.data.enums.Size import Size
import abc


class Side:
    """The Side class.

    This class contains the methods that all side objects
    have in common.  It will behave as a superclass that
    all side classes will inherit from.
    """
    @property
    def size(self) -> Size:
        """Getter for size.

        This getter retrieves the size of the
        side.

        Returns:
            A Size type object indicating either
            Indie (small), Studio (medium), or
            Blockbuster (large).
        """
        return self._size

    @size.setter
    def size(self, value: Size) -> None:
        """Setter for size.

        This setter is used to change the size
        of the side.

        Args:
            value: A Size type object indicating
            size.
        """
        self._size = value

    @property
    @abc.abstractmethod
    def price(self) -> float:
        """Abstract getter for price.

        Verifies that each subclass has
        price getting functionality. This method
        should not be called directly.

        Returns:
            Price when overwritten by subclass.
        """
        raise NotImplementedError

    @property
    @abc.abstractmethod
    def calories(self) -> int:
        """Abstract getter for calories.

        Verifies that each subclass has
        calorie getting functionality. This method
        should not be called directly.

        Returns:
            Calories when overwritten by subclass.
        """
        raise NotImplementedError

    @property
    def instructions(self) -> List:
        """Getter for instructions.

        There are no instructions associated
        with the sides, so this function returns
        an empty list.

        Returns:
            An empty list.
        """
        return []

    @property
    @abc.abstractmethod
    def name(self) -> str:
        """Getter for name.

        Gets the name of the side.

        Returns:
            A string value representing
            the name of the side.
        """
        return "Side"
