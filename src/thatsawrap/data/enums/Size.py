"""Size Enumeration.

This file contains the code required to enumerate the different
Sizes a drink or side can come in.

Author: Dustin Hayes djhayes@ksu.edu
Version 0.2
"""
from enum import Enum


class Size(str, Enum):
    """The Size class.

    This class is an enumeration that contains the all the sizes
    a drink or side can come in.

    Args:
        str: A string representing one of the sizes.
    """
    INDIE = "Indie"
    STUDIO = "Studio"
    BLOCKBUSTER = "Blockbuster"

    def __str__(self) -> str:
        """The string representation.

        This method defines and returns the string
        that is printed when the print function is
        run on the object.

        Returns:
            A string representation of the object.
        """
        return str(self.value)
