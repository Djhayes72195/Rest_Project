"""Shell Enumeration.

This file contains the code required to enumerate the different
Shells a wrap can come in.

Author: Dustin Hayes djhayes@ksu.edu
Version 0.2
"""
from enum import Enum


class Shell(str, Enum):
    """The Shell class.

    This class is an enumeration that contains the all the shell
    a wrap can come in.

    Args:
        str: A string representing one of the shells.
    """
    WHOLE_GRAIN = "Whole Grain"
    SPINACH = "Spinach"
    STROMBOLI = "Stromboli"

    def __str__(self) -> str:
        """The string representation.

        This method defines and returns the string
        that is printed when the print function is
        run on the object.

        Returns:
            A string representation of the object.
        """
        return str(self.value)
