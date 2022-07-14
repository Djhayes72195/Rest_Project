"""The Spartacus wrap.

This file contains the code required to instantiate a Spartacus
type object.

Author: Dustin Hayes djhayes@ksu.edu
Version 0.3
"""
from src.thatsawrap.data.enums.Shell import Shell
from src.thatsawrap.data.enums.Addin import Addin
from typing import List, Set
from src.thatsawrap.data.menu.Item import Item
from src.thatsawrap.data.wraps.Wrap import Wrap


class Spartacus(Wrap, Item):
    """The Spartacus class.

    This class contains all of the attributes that define
    the state of the wrap, as well as the functions that
    it can perform.
    """
    def __init__(self) -> None:
        """The constructor for the Spartacus wrap."""
        self._shell: Shell = Shell.SPINACH
        self._addins: Set[Addin] = {Addin.ONIONS, Addin.PEPPERS,
                                    Addin.TOMATOES, Addin.PICKLES,
                                    Addin.BUFFALO_SAUCE,
                                    Addin.DRESSING}
        self.__chicken = True
        self.__cheese = True
        self.__corned_beef = True
        self.__pepperoni = True
        self.__sausage = True

    @property
    def price(self) -> float:
        """Getter for the price of the wrap.

        The wrap could have 3 different prices depending
        on its shell.

        Returns:
            A float value indicating the price of the wrap.
        """
        if self._shell == Shell.WHOLE_GRAIN:
            return 16.30
        elif self._shell == Shell.SPINACH:
            return 16.55
        else:
            return 17.05

    @property
    def calories(self) -> int:
        """Getter for the calories the wrap has.

        Returns:
            An int indicating how many calories the wrap has.
        """
        return 1874

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
        if not self.__chicken:
            specials.append("Hold Chicken")
        if not self.__cheese:
            specials.append("Hold Cheese")
        if not self.__corned_beef:
            specials.append("Hold Corned Beef")
        if not self.__sausage:
            specials.append("Hold Sausage")
        if not self.__pepperoni:
            specials.append("Hold Pepperoni")
        for instr in super().instructions:
            specials.append(instr)
        return specials

    @property
    def chicken(self) -> bool:
        """Getter for chicken.

        This getter retrieves whether or not the object
        has chicken.

        Returns:
            True if the wrap has chicken, otherwise False.
        """
        return self.__chicken

    @chicken.setter
    def chicken(self, value: bool) -> None:
        """Setter for chicken.

        This setter is used to change the state of
        chicken.

        Args:
            value: True if we wish to include chicken,
            False otherwise.
        """
        self.__chicken = value

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

    @property
    def corned_beef(self) -> bool:
        """Getter for corned beef.

        This getter retrieves whether or not the object
        has corned beef.

        Returns:
            True if the wrap has corned beef, otherwise False.
        """
        return self.__corned_beef

    @corned_beef.setter
    def corned_beef(self, value: bool) -> None:
        """Setter for corned beef.

        This setter is used to change the state of
        corned beef.

        Args:
            value: True if we wish to include corned beef,
            False otherwise.
        """
        self.__corned_beef = value

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

    def __str__(self) -> str:
        """String representation.

        This method specifes the form of the
        string representation of the wrap and returns
        it.

        Returns:
            The string representation of the wrap.
        """
        return "Spartacus in a {} Shell".format(self._shell)

    def __eq__(self, value: object) -> bool:
        """Sets conditions for equality.

        This method overwrites the default
        __eq__ function in python such that two
        objects are equal if they are of the same type
        and all attributes are equal.

        Args:
            value: Object with which our wrap will be
            compared

        Returns:
            True if the two objects are of the same
            type and all of their attributes are equal,
            False otherwise
        """
        if isinstance(value, Spartacus):
            return (self._shell == value.shell and
                    self._addins == value.addins and
                    self.__chicken == value.chicken and
                    self.__cheese == value.cheese and
                    self.__corned_beef == value.corned_beef and
                    self.__sausage == value.sausage and
                    self.__pepperoni == value.pepperoni)
        else:
            return False

    @property
    def name(self) -> str:
        """Getter for name.

        Gets the name of the wrap.

        Returns: A string value representing
        the name of the wrap.
        """
        return "Spartacus"
