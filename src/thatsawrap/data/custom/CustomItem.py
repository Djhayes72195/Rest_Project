"""Custom Item.

This file contains the code required to build
custom items for our web application.

Author: Dustin Hayes djhayes@ksu.edu
Version 0.1
"""
from src.thatsawrap.data.menu.Item import Item
from typing import List


class CustomItem(Item):
    """Custom Item Class.

    Contains the code required to represent
    A custom item.  Implements the Item interface.
    """
    def __init__(self, name: str, price: float, calories: int) -> None:
        """Custom Item constructor.

        Sets and stores the state of a
        Custom Item object.

        Args:
            name: The name of the item.
            price: The price of the item
            calories: The number of calories in
            the item.
        """
        self.__name: str = name
        self.__price: float = price
        self.__calories: int = calories

    @property
    def name(self) -> str:
        """Getter for name.

        Returns:
            A string representing the
            name.
        """
        return self.__name

    @name.setter
    def name(self, name: str) -> None:
        """Setter for name.

        Args:
            name: The name to be set
        """
        self.__name = name

    @property
    def price(self) -> float:
        """Getter for price.
        
        Returns: The price as a float.
        """
        return self.__price

    @price.setter
    def price(self, price: float) -> None:
        """Setter for price.
        
        Args:
            price: The price to be set.
        """
        self.__price = round(price, 2)

    @property
    def calories(self) -> int:
        """Getter for calories.
        
        Returns: The calories as an int.
        """
        return self.__calories

    @calories.setter
    def calories(self, calories: int) -> None:
        """Setter for calories.
        
        Args: 
            calories: The calories as an int.
        """
        self.__calories = calories
    
    @property
    def instructions(self) -> List[str]:
        """Getter for instructions.
        
        Returns: An empty list of strings,
        as custom items do not get special
        instructions at this point.
        """
        return list()
