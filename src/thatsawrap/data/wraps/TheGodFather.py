"""The Godfather wrap.

This file contains the code required to instantiate a TheGodFather
type object.

Author: Dustin Hayes djhayes@ksu.edu
Version 0.3
"""
from src.thatsawrap.data.enums.Shell import Shell
from src.thatsawrap.data.enums.Addin import Addin
from typing import List, Set
from src.thatsawrap.data.menu.Item import Item
from src.thatsawrap.data.wraps.Wrap import Wrap


class TheGodFather(Wrap, Item):
    """The Godfather class.

    This class contains all of the attributes that define
    the state of the wrap, as well as the functions that
    it can perform.
    """
    def __init__(self) -> None:
        """The constructor for The Godfather wrap."""
        self._shell: Shell = Shell.STROMBOLI
        self._addins: Set[Addin] = {Addin.PEPPERS, Addin.ONIONS}
        self.__pepperoni: bool = True
        self.__sausage: bool = True
        self.__marinara: bool = True
        self.__cheese: bool = True

    @property
    def price(self) -> float:
        """Getter for the price of the wrap.

        The wrap could have 3 different prices depending
        on its shell.

        Returns:
            A float value indicating the price of the wrap.
        """
        if self._shell == Shell.STROMBOLI:
            return 9.65
        elif self._shell == Shell.SPINACH:
            return 9.15
        else:
            return 8.90

    @property
    def calories(self) -> int:
        """Getter for the calories the wrap has.

        Returns:
            An int indicating how many calories the wrap has.
        """
        return 1268

    @property
    def instructions(self) -> List[str]:
        """Getter for the instructions.

        The customer can choose to either remove
        or add certain ingredients.  If the customer
        removes a default ingredient or adds a non-default
        ingredient, special instructions regarding the change
        are added to a list this getter retrieves.

        Returns:
            A list of strings containing the instructions.
        """
        specials: List[str] = []
        if not self.__pepperoni:
            specials.append("Hold Pepperoni")
        if not self.__sausage:
            specials.append("Hold Sausage")
        if not self.__marinara:
            specials.append("Hold Marinara")
        if not self.__cheese:
            specials.append("Hold Cheese")
        for instr in super().instructions:
            specials.append(instr)
        return specials

    @property
    def pepperoni(self) -> bool:
        """Getter for pepperoni.

        This getter retrieves whether or not the object
        has pepperoni.

        Returns:
            True if the wrap has pepperoni, otherwise False.
        """
        return self.__pepperoni

    @pepperoni.setter
    def pepperoni(self, value: bool) -> None:
        """Setter for pepperoni.

        This setter is used to change the state of
        pepperoni.

        Args:
            value: True if we wish to include pepperoni,
            False otherwise.
        """
        self.__pepperoni = value

    @property
    def sausage(self) -> bool:
        """Getter for sausage.

        This getter retrieves whether or not the object
        has sausage.

        Returns:
            True if the wrap has sausage, otherwise False.
        """
        return self.__sausage

    @sausage.setter
    def sausage(self, value: bool) -> None:
        """Setter for sausage.

        This setter is used to change the state of
        sausage.

        Args:
            value: True if we wish to include sausage,
            False otherwise.
        """
        self.__sausage = value

    @property
    def marinara(self) -> bool:
        """Getter for marinara.

        This getter retrieves whether or not the object
        has marinara.

        Returns:
            True if the wrap has marinara, otherwise False.
        """
        return self.__marinara

    @marinara.setter
    def marinara(self, value: bool) -> None:
        """Setter for marinara.

        This setter is used to change the state of
        marinara.

        Args:
            value: True if we wish to include marinara,
            False otherwise.
        """
        self.__marinara = value

    @property
    def cheese(self) -> bool:
        """Getter for cheese.

        This getter retrieves whether or not the object
        has cheese.

        Returns:
            True if the wrap has cheese, otherwise False.
        """
        return self.__cheese

    @cheese.setter
    def cheese(self, value: bool) -> None:
        """Setter for cheese.

        This setter is used to change the state of
        cheese.

        Args:
            value: True if we wish to include cheese,
            False otherwise.
        """
        self.__cheese = value

    def __str__(self) -> str:
        """String representation.

        This method specifes the form of the
        string representation of the wrap and returns
        it.

        Returns:
            The string representation of the wrap.
        """
        return "The Godfather in a {} Shell".format(self._shell)

    def __eq__(self, value: object) -> bool:
        """Sets conditions for equality.

        This method overwrites the default
        __eq__ function in python such that two
        objects are equal if they are of the same type
        and all attributes are equal.

        Args:
            value: Object with which our wrap will be
            compared.

        Returns:
            True if the two objects are of the same
            type and all of their attributes are equal,
            False otherwise
        """
        if isinstance(value, TheGodFather):
            return (self._shell == value.shell and
                    self._addins == value.addins and
                    self.__pepperoni == value.pepperoni and
                    self.__sausage == value.sausage and
                    self.__marinara == value.marinara and
                    self.__cheese == value.cheese)
        else:
            return False

    @property
    def name(self) -> str:
        """Getter for name.

        Gets the name of the wrap.

        Returns: A string value representing
        the name of the wrap.
        """
        return "The Godfather"
