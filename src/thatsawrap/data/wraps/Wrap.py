"""Wrap superclass.

This file contains the code that defines an
instance of a wrap item according to their
shared characteristics.

Author: Dustin Hayes djhayes@ksu.edu
Version 0.1
"""
from typing import List, Set
from src.thatsawrap.data.enums.Shell import Shell
from src.thatsawrap.data.enums.Addin import Addin
import abc


class Wrap:
    """The Wrap class.

    This class contains the methods that all wrap objects
    have in common.  It will behave as a superclass that
    all wrap classes will inherit from.
    """
    @property
    def shell(self) -> Shell:
        """Getter for shell.

        This getter retrieves what type of shell the wrap
        is in.

        Returns:
            A Shell type object indicating either Stromboli
            Spinach or Whole Grain.
        """
        return self._shell

    @shell.setter
    def shell(self, value: Shell) -> None:
        """Setter for shell.

        This setter is used to change the shell that
        the wrap is in.

        Args:
            value: A Shell type object indicating either Stromboli
            Spinach or Whole Grain.
        """
        self._shell = value

    @property
    def addins(self) -> Set[Addin]:
        """Getter for addins.

        This getter retrieves a list of the addins
        in the wrap.

        Returns:
            A list of Addin type objects.
        """
        return self._addins.copy()

    def add_addin(self, value: Addin) -> None:
        """Adds an addin.

        This method adds a Addin type object
        to the list of addins in the wrap.

        Args:
            value: An Addin type object.
        """
        self._addins.add(value)

    def remove_addin(self, value: Addin) -> None:
        """Removes an addin.

        This method removes a Addin type object
        to the list of addins in the wrap.

        Args:
            value: An Addin type object.
        """
        self._addins.discard(value)

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

        Called from the subclass to include
        the addins in the instructions.

        Returns:
            A list of extra instructions
            regarding the addins.
        """
        extra_instructions = []
        for add in self._addins:
            extra_instructions.append("Add {}".format(add))
        return extra_instructions

    @property
    @abc.abstractmethod
    def name(self) -> str:
        """Getter for name.

        Abstract method.
        """
        raise NotImplementedError
