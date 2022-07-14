"""The Forrest Gump drink.

This file contains the code required to instantiate a ForrestGump
type object.

Author: Dustin Hayes djhayes@ksu.edu
Version 0.3
"""
from src.thatsawrap.data.enums.Size import Size
from typing import List
from src.thatsawrap.data.menu.Item import Item
from src.thatsawrap.data.drinks.Drink import Drink


class ForrestGump(Drink, Item):
    """The Forrest Gump class.

    This class contains all of the attributes that define
    the state of the drink, as well as the functions that
    it can perform.
    """
    def __init__(self) -> None:
        """Constructor for the Forrest Gump class."""
        self.__size: Size = Size.INDIE
        self.__chocolate = True
        self.__vanilla = False
        self.__caramel = False
        self.__coffee = False

    @property
    def price(self) -> float:
        """Getter for the price of the drink.

        The drink could have 3 different prices depending
        on its size.

        Returns:
            A float value indicating the price of the drink.
        """
        if self.__size == Size.INDIE:
            return 5.25
        elif self.__size == Size.STUDIO:
            return 7.50
        else:
            return 9.00

    @property
    def calories(self) -> int:
        """Getter for the calories the drink has.

        Returns:
            An int indicating how many calories the drink has.
        """
        if self.__size == Size.INDIE:
            return 980
        elif self.__size == Size.STUDIO:
            return 1365
        else:
            return 1875

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
        if not self.__chocolate:
            specials.append("Hold Chocolate")
        if self.__vanilla:
            specials.append("Add Vanilla")
        if self.__caramel:
            specials.append("Add Caramel")
        if self.__coffee:
            specials.append("Add Coffee")
        return specials

    @property
    def chocolate(self) -> bool:
        """Getter for chocolate.

        This getter retrieves whether or not the object
        has chocolate.

        Returns:
            True if the drink has chocolate, otherwise False.
        """
        return self.__chocolate

    @chocolate.setter
    def chocolate(self, value: bool) -> None:
        """Setter for chocolate.

        This setter is used to change the state of
        chocolate.

        Args:
            value: True if we wish to include chocolate,
            False otherwise.
        """
        self.__chocolate = value

    @property
    def vanilla(self) -> bool:
        """Getter for vanilla.

        This getter retrieves whether or not the object
        has vanilla.

        Returns:
            True if the drink has vanilla, otherwise False.
        """
        return self.__vanilla

    @vanilla.setter
    def vanilla(self, value: bool) -> None:
        """Setter for vanilla.

        This setter is used to change the state of
        vanilla.

        Args:
            value: True if we wish to include vanilla,
            False otherwise.
        """
        self.__vanilla = value

    @property
    def caramel(self) -> bool:
        """Getter for caramel.

        This getter retrieves whether or not the object
        has caramel.

        Returns:
            True if the drink has caramel, otherwise False.
        """
        return self.__caramel

    @caramel.setter
    def caramel(self, value: bool) -> None:
        """Setter for caramel.

        This setter is used to change the state of
        caramel.

        Args:
            value: True if we wish to include caramel,
            False otherwise.
        """
        self.__caramel = value

    @property
    def coffee(self) -> bool:
        """Getter for coffee.

        This getter retrieves whether or not the object
        has coffee.

        Returns:
            True if the drink has coffee, otherwise False.
        """
        return self.__coffee

    @coffee.setter
    def coffee(self, value: bool) -> None:
        """Setter for coffee.

        This setter is used to change the state of
        coffee.

        Args:
            value: True if we wish to include coffee,
            False otherwise.
        """
        self.__coffee = value

    @property
    def size(self) -> Size:
        """Getter for size.

        This getter returns a value indicating the
        size of the side: Either Indie (small),
        Studio (medium) or Blockbuster (large).

        Returns:
            A Size type object corresponding to size.
        """
        return self.__size

    @size.setter
    def size(self, value: Size) -> None:
        """Setter for size.

        This setter sets a value indicating the
        size of the drink: Either Indie (small),
        Studio (medium) or Blockbuster (large).

        Args:
            value: A Size type object indicating the size of the drink.
        """
        self.__size = value

    def __str__(self) -> str:
        """String representation.

        This method specifes the form of the
        string representation of the drink and returns
        it.

        Returns:
            The string representation of the drink.
        """
        return "{} Forrest Gump".format(self.__size)

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
        if isinstance(value, ForrestGump):
            return (self.__size == value.size and
                    self.__chocolate == value.chocolate and
                    self.__vanilla == value.vanilla and
                    self.__caramel == value.caramel and
                    self.__coffee == value.coffee)
        else:
            return False

    @property
    def name(self) -> str:
        """Getter for name.

        Gets the name of the drink.

        Returns: A string value representing
        the name of the drink.
        """
        return "Forrest Gump"
