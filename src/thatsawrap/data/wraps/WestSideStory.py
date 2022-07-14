"""The West Side Story wrap.

This file contains the code required to instantiate a WestSideStory
type object.

Author: Dustin Hayes djhayes@ksu.edu
Version 0.3
"""
from src.thatsawrap.data.enums.Shell import Shell
from src.thatsawrap.data.enums.Addin import Addin
from typing import List, Set
from src.thatsawrap.data.menu.Item import Item
from src.thatsawrap.data.wraps.Wrap import Wrap


class WestSideStory(Wrap, Item):
    """The West Side Story class.

    This class contains all of the attributes that define
    the state of the wrap, as well as the functions that
    it can perform.
    """

    def __init__(self) -> None:
        """The constructor for The West Side Story wrap."""
        self._shell: Shell = Shell.WHOLE_GRAIN
        self._addins: Set[Addin] = {Addin.ONIONS, Addin.PICKLES, Addin.MUSTARD}
        self.__corned_beef = True
        self.__cabbage = True
        self.__cheese = True

    @property
    def price(self) -> float:
        """Getter for the price of the wrap.

        The wrap could have 3 different prices depending
        on its shell.

        Returns:
            A float value indicating the price of the wrap.
        """
        if self._shell == Shell.WHOLE_GRAIN:
            return 8.75
        elif self._shell == Shell.SPINACH:
            return 9.0
        else:
            return 9.50

    @property
    def calories(self) -> int:
        """Getter for the calories the wrap has.

        Returns:
            An int indicating how many calories the wrap has.
        """
        return 1240

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
        if not self.__corned_beef:
            specials.append("Hold Corned Beef")
        if not self.__cabbage:
            specials.append("Hold Cabbage")
        if not self.__cheese:
            specials.append("Hold Cheese")
        for instr in super().instructions:
            specials.append(instr)
        return specials

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
    def cabbage(self) -> bool:
        """Getter for cabbage.

        This getter retrieves whether or not the object
        has cabbage.

        Returns:
            True if the wrap has cabbage, otherwise False.
        """
        return self.__cabbage

    @cabbage.setter
    def cabbage(self, value: bool) -> None:
        """Setter for cabbage.

        This setter is used to change the state of
        cabbage.

        Args:
            value: True if we wish to include cabbage,
            False otherwise.
        """
        self.__cabbage = value

    def __str__(self) -> str:
        """String representation.

        This method specifes the form of the
        string representation of the wrap and returns
        it.

        Returns:
            The string representation of the wrap.
        """
        return "West Side Story in a {} Shell".format(self._shell)

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
        if isinstance(value, WestSideStory):
            return (self._shell == value.shell and
                    self._addins == value.addins and
                    self.__corned_beef == value.corned_beef and
                    self.__cheese == value.cheese and
                    self.__cabbage == value.cabbage)
        else:
            return False

    @property
    def name(self) -> str:
        """Getter for name.

        Gets the name of the wrap.

        Returns: A string value representing
        the name of the wrap.
        """
        return "West Side Story"
