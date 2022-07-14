"""The Wizard of Oz wrap.

This file contains the code required to instantiate a TheWizardOfOz
type object.

Author: Dustin Hayes djhayes@ksu.edu
Version 0.3
"""
from src.thatsawrap.data.enums.Shell import Shell
from src.thatsawrap.data.enums.Addin import Addin
from typing import List, Set
from src.thatsawrap.data.menu.Item import Item
from src.thatsawrap.data.wraps.Wrap import Wrap


class TheWizardOfOz(Wrap, Item):
    """The Wizard of Oz class.

    This class contains all of the attributes that define
    the state of the wrap, as well as the functions that
    it can perform.
    """
    def __init__(self) -> None:
        """The constructor for The Wizard Of Oz wrap."""
        self._shell: Shell = Shell.SPINACH
        self._addins: Set[Addin] = {Addin.TOMATOES, Addin.DRESSING}
        self.__chicken = True
        self.__spinach = True
        self.__cheese = True

    @property
    def price(self) -> float:
        """Getter for the price of the wrap.

        The wrap could have 3 different prices depending
        on its shell.

        Returns:
            A float value indicating the price of the wrap.
        """
        if self._shell == Shell.STROMBOLI:
            return 10.85
        elif self._shell == Shell.SPINACH:
            return 10.35
        else:
            return 10.10

    @property
    def calories(self) -> int:
        """Getter for the calories the wrap has.

        Returns:
            An int indicating how many calories the wrap has.
        """
        return 1085

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
        if not self.__spinach:
            specials.append("Hold Spinach")
        if not self.__chicken:
            specials.append("Hold Chicken")
        if not self.__cheese:
            specials.append("Hold Cheese")
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
    def spinach(self) -> bool:
        """Getter for spinach.

        This getter retrieves whether or not the object
        has spinach.

        Returns:
            True if the wrap has spinach, otherwise False.
        """
        return self.__spinach

    @spinach.setter
    def spinach(self, value: bool) -> None:
        """Setter for spinach.

        This setter is used to change the state of
        spinach.

        Args:
            value: True if we wish to include spinach,
            False otherwise.
        """
        self.__spinach = value

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
        return "The Wizard Of Oz in a {} Shell".format(self._shell)

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
        if isinstance(value, TheWizardOfOz):
            return (self._shell == value.shell and
                    self._addins == value.addins and
                    self.__chicken == value.chicken and
                    self.__spinach == value.spinach and
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
        return "The Wizard of Oz"
