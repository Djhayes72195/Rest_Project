"""Addin Enumeration.

This file contains the code required to enumerate the different
Addins a wrap can have.

Author: Dustin Hayes djhayes@ksu.edu
Version 0.2
"""
from enum import Enum


class Addin(str, Enum):
    """The Addin class.

    This class is an enumeration that contains the all the addins
    a wrap might have.

    Args:
        str: A string representing one of the addins.
    """
    PEPPERS = "Peppers"
    ONIONS = "Onions"
    TOMATOES = "Tomatoes"
    PICKLES = "Pickles"
    DRESSING = "Dressing"
    BUFFALO_SAUCE = "Buffalo Sauce"
    MUSTARD = "Mustard"

    def __str__(self) -> str:
        """The string representation.

        This method defines and returns the string
        that is printed when the print function is
        run on the object.

        Returns:
            A string representation of the object.
        """
        return str(self.value)
