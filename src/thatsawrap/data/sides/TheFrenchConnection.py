"""The French Connection side.

This file contains the code required to
instantiate a TheFrenchConnection type object.

Author: Dustin Hayes djhayes@ksu.edu
Version 0.3
"""
from src.thatsawrap.data.enums.Size import Size
from src.thatsawrap.data.sides.Side import Side
from src.thatsawrap.data.menu.Item import Item


class TheFrenchConnection(Side, Item):
    """The French Connection class.

    This class contains all of the attributes that define
    the state of the side, as well as the functions that
    it can perform.
    """
    def __init__(self) -> None:
        """The constructor for The French Connection side."""
        self._size: Size = Size.INDIE

    @property
    def price(self) -> float:
        """Getter for the price of the side.

        The side could have 3 different prices depending
        on its size.

        Returns:
            A float value indicating the price of the side.
        """
        if self._size == Size.INDIE:
            return 2.75
        elif self._size == Size.STUDIO:
            return 4.85
        else:
            return 5.25

    @property
    def calories(self) -> int:
        """Getter for the calories the side has.

        Three different calorie amounts are possible depending on
        the size of the side.

        Returns:
            An int indicating how many calories the wrap has.
        """
        if self._size == Size.INDIE:
            return 550
        elif self._size == Size.STUDIO:
            return 700
        else:
            return 950

    def __str__(self) -> str:
        """String representation.

        This method specifes the form of the
        string representation of the side and returns
        it.

        Returns:
            The string representation of the side.
        """
        return "{} The French Connection".format(self._size)

    def __eq__(self, value: object) -> bool:
        """Sets conditions for equality.

        This method overwrites the default
        __eq__ function in python such that two
        objects are equal if they are of the same type
        and all attributes are equal.

        Args:
            value: Object with which our side will be
            compared

        Returns:
            True if the two objects are of the same
            type and all of their attributes are equal,
            False otherwise
        """
        if isinstance(value, TheFrenchConnection):
            return (self._size == value.size)
        else:
            return False

    @property
    def name(self) -> str:
        """Getter for name.

        Gets the name of the side.

        Returns:
            A string value representing
            the name of the side.
        """
        return "The French Connection"
