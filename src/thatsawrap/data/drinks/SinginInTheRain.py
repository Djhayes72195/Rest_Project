"""The Singin' in the Rain drink.

This file contains the code required to instantiate a
SinginInTheRain type object.

Author: Dustin Hayes djhayes@ksu.edu
Version 0.3
"""
from src.thatsawrap.data.enums.Size import Size
from typing import List
from src.thatsawrap.data.menu.Item import Item
from src.thatsawrap.data.drinks.Drink import Drink


class SinginInTheRain(Drink, Item):
    """The Singin' in the Rain class.

    This class contains all of the attributes that define
    the state of the wrap, as well as the functions that
    it can perform.
    """
    def __init__(self) -> None:
        """Constructor for the Singin' in the Rain class."""
        self._size: Size = Size.INDIE
        self.__cherry = True
        self.__strawberry = False
        self.__cola = False
        self.__grape = False

    @property
    def price(self) -> float:
        """Getter for the price of the drink.

        The drink could have 3 different prices depending
        on its size.

        Returns:
            A float value indicating the price of the drink.
        """
        if self._size == Size.INDIE:
            return 2.75
        elif self._size == Size.STUDIO:
            return 3.25
        else:
            return 4.00

    @property
    def calories(self) -> int:
        """Getter for the calories the drink has.

        Returns:
            An int indicating how many calories the wrap has.
        """
        if self._size == Size.INDIE:
            return 360
        elif self._size == Size.STUDIO:
            return 400
        else:
            return 550

    @property
    def instructions(self) -> List[str]:
        """Getter for the instructions.

        The customer can choose to either remove
        or add certain flavors.  If the customer
        removes a default flavor or adds a non-default
        flavor, special instructions regarding the change
        are added to a list this getter retrieves.

        Returns:
            A list of strings containing the instructions.
        """
        specials: List[str] = []
        if not self.__cherry:
            specials.append("Hold Cherry")
        if self.__strawberry:
            specials.append("Add Strawberry")
        if self.__cola:
            specials.append("Add Cola")
        if self.__grape:
            specials.append("Add Grape")
        return specials

    @property
    def cherry(self) -> bool:
        """Getter for cherry.

        This getter retrieves whether or not the object
        has cherry.

        Returns:
            True if the drink has cherry, otherwise False.
        """
        return self.__cherry

    @cherry.setter
    def cherry(self, value: bool) -> None:
        """Setter for cherry.

        This setter is used to change the state of
        cherry.

        Args:
            value: True if we wish to include cherry,
            False otherwise.
        """
        self.__cherry = value

    @property
    def cola(self) -> bool:
        """Getter for cola.

        This getter retrieves whether or not the object
        has cola.

        Returns:
            True if the drink has cola, otherwise False.
        """
        return self.__cola

    @cola.setter
    def cola(self, value: bool) -> None:
        """Setter for cola.

        This setter is used to change the state of
        cola.

        Args:
            value: True if we wish to include cola,
            False otherwise.
        """
        self.__cola = value

    @property
    def grape(self) -> bool:
        """Getter for grape.

        This getter retrieves whether or not the object
        has grape.

        Returns:
            True if the drink has cola, otherwise False.
        """
        return self.__grape

    @grape.setter
    def grape(self, value: bool) -> None:
        """Setter for grape.

        This setter is used to change the state of
        grape.

        Args:
            value: True if we wish to include grape,
            False otherwise.
        """
        self.__grape = value

    @property
    def strawberry(self) -> bool:
        """Getter for strawberry.

        This getter retrieves whether or not the object
        has strawberry.

        Returns:
            True if the drink has strawberry, otherwise False.
        """
        return self.__strawberry

    @strawberry.setter
    def strawberry(self, value: bool) -> None:
        """Setter for strawberry.

        This setter is used to change the state of
        strawberry.

        Args:
            value: True if we wish to include strawberry,
            False otherwise.
        """
        self.__strawberry = value

    def __str__(self) -> str:
        """String representation.

        This method specifes the form of the
        string representation of the drink and returns
        it.

        Returns:
            The string representation of the drink.
        """
        return "{} Singin' In The Rain".format(self._size)

    def __eq__(self, value: object) -> bool:
        """Sets conditions for equality.

        This method overwrites the default
        __eq__ function in python such that two
        objects are equal if they are of the same type
        and all attributes are equal.

        Args:
            value: Object with which our drink will be
            compared

        Returns:
            True if the two objects are of the same
            type and all of their attributes are equal,
            False otherwise
        """
        if isinstance(value, SinginInTheRain):
            return (self.__cherry == value.cherry and
                    self.__strawberry == value.strawberry and
                    self.__cola == value.cola and
                    self.__grape == value.grape and
                    self._size == value.size)
        else:
            return False

    @property
    def name(self) -> str:
        """Getter for name.

        Gets the name of the drink.

        Returns: A string value representing
        the name of the drink.
        """
        return "Singin' in the Rain"
