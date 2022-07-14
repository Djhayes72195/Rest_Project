"""The King Kong drink.

This file contains the code required to instantiate a KingKong
type object.

Author: Dustin Hayes djhayes@ksu.edu
Version 0.3
"""
from src.thatsawrap.data.enums.Size import Size
from typing import List
from src.thatsawrap.data.menu.Item import Item
from src.thatsawrap.data.drinks.Drink import Drink


class KingKong(Drink, Item):
    """The King Kong class.

    This class contains all of the attributes that define
    the state of the drink, as well as the functions that
    it can perform.
    """
    def __init__(self) -> None:
        """Constructor for the King Kong class."""
        self._size: Size = Size.INDIE
        self.__banana = True
        self.__strawberry = False
        self.__peach = False
        self.__mango = False

    @property
    def price(self) -> float:
        """Getter for the price of the drink.

        The drink could have 3 different prices depending
        on its size.

        Returns:
            A float value indicating the price of the drink.
        """
        if self._size == Size.INDIE:
            return 4.85
        elif self._size == Size.STUDIO:
            return 5.95
        else:
            return 7.45

    @property
    def calories(self) -> int:
        """Getter for the calories the drink has.

        Returns:
            An int indicating how many calories the drink has.
        """
        if self._size == Size.INDIE:
            return 465
        elif self._size == Size.STUDIO:
            return 625
        else:
            return 860

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
        if not self.__banana:
            specials.append("Hold Banana")
        if self.__strawberry:
            specials.append("Add Strawberry")
        if self.__peach:
            specials.append("Add Peach")
        if self.__mango:
            specials.append("Add Mango")
        return specials

    @property
    def banana(self) -> bool:
        """Getter for banana.

        This getter retrieves whether or not the object
        has banana.

        Returns:
            True if the drink has banana, otherwise False.
        """
        return self.__banana

    @banana.setter
    def banana(self, value: bool) -> None:
        """Setter for banana.

        This setter is used to change the state of
        banana.

        Args:
            value: True if we wish to include banana,
            False otherwise.
        """
        self.__banana = value

    @property
    def peach(self) -> bool:
        """Getter for peach.

        This getter retrieves whether or not the object
        has peach.

        Returns:
            True if the drink has peach, otherwise False.
        """
        return self.__peach

    @peach.setter
    def peach(self, value: bool) -> None:
        """Setter for peach.

        This setter is used to change the state of
        peach.

        Args:
            value: True if we wish to include peach,
            False otherwise.
        """
        self.__peach = value

    @property
    def mango(self) -> bool:
        """Getter for mango.

        This getter retrieves whether or not the object
        has mango.

        Returns:
            True if the drink has mango, otherwise False.
        """
        return self.__mango

    @mango.setter
    def mango(self, value: bool) -> None:
        """Setter for mango.

        This setter is used to change the state of
        mango.

        Args:
            value: True if we wish to include mango,
            False otherwise.
        """
        self.__mango = value

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
        return "{} King Kong".format(self._size)

    def __eq__(self, value: object) -> bool:
        """Sets conditions for equality.

        This method overwrites the default
        __eq__ function in python such that two
        objects are equal if they are of the same type
        and all attributes are equal.

        Args:
            value: Object with which our drink will be
            compared.

        Returns:
            True if the two objects are of the same
            type and all of their attributes are equal,
            False otherwise.
        """
        if isinstance(value, KingKong):
            return (self.__banana == value.banana and
                    self.__strawberry == value.strawberry and
                    self.__peach == value.peach and
                    self.__mango == value.mango and
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
        return "King Kong"
