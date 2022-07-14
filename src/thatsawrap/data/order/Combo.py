
"""Combo class file.

Represents a combination of Items, sold
as a combo.

Author: Dustin hayes djhayes@ksu.edu
Version: 0.1
"""
from typing import List
from src.thatsawrap.data.menu.Item import Item
from src.thatsawrap.data.wraps.Wrap import Wrap
from src.thatsawrap.data.drinks.Drink import Drink
from src.thatsawrap.data.sides.Side import Side


class Combo(Item):
    """Combo class.

    This class represents a combo
    including a drink, wrap and
    side.
    """
    __discount: float = .95

    def __init__(self, name: str = None) -> None:
        """Constructor for combo class.

        Contains the state of the combo.

        Args:
            name: An optional string value
            representing the name of the combo.
        """
        self.__name: str = name
        self.__wrap: Wrap = None
        self.__side: Side = None
        self.__drink: Drink = None

    @classmethod
    def get_discount(cls) -> float:
        """Static getter for discount.

        Gets the discount.

        Returns:
            A float representing the
            discount a customer gets by
            buying a combo.
        """
        return cls._Combo__discount

    @classmethod
    def set_discount(cls, discount: float) -> None:
        """Static setter for discount.

        Sets the discount.

        Args:
            discount: A float representing the
            discount a customer gets by
            buying a combo.
        """
        if discount < 0.0:
            raise ValueError
        else:
            cls._Combo__discount = discount

    @property
    def name(self) -> str:
        """Getter for name.

        Gets the name of the combo.

        Returns:
            The name of the combo.
        """
        return self.__name

    @name.setter
    def name(self, n: str) -> None:
        """Setter for name.

        Sets the name of the combo.

        Args:
            n: A string representing
            the name to set the combo to.
        """
        self.__name = n

    @property
    def wrap(self) -> Wrap:
        """Getter for wrap.

        Gets the wrap in the combo.

        Returns:
            The Wrap type object in the
            combo.
        """
        return self.__wrap

    @wrap.setter
    def wrap(self, w: Wrap) -> None:
        """Setter for wrap.

        Sets the wrap in the combo.

        Args:
            w: The Wrap type object to be
            stored in the combo.
        """
        if isinstance(w, Wrap) or w is None:
            self.__wrap = w
        else:
            raise ValueError

    @property
    def drink(self) -> Drink:
        """Getter for drink.

        Gets the drink in the combo.

        Returns:
            The Drink type object in the
            combo.
        """
        return self.__drink

    @drink.setter
    def drink(self, d: Drink) -> None:
        """Setter for drink.

        Sets the drink in the combo.

        Args:
            d: The Drink type object to be
            stored in the combo.
        """
        if isinstance(d, Drink) or d is None:
            self.__drink = d
        else:
            raise ValueError

    @property
    def side(self) -> Side:
        """Getter for side.

        Gets the side in the combo.

        Returns:
            The Side type object in the
            combo.
        """
        return self.__side

    @side.setter
    def side(self, s: side) -> None:
        """Setter for side.

        Sets the side in the combo.

        Args:
            s: The Side type object to be
            stored in the combo.
        """
        if isinstance(s, Side) or s is None:
            self.__side = s
        else:
            raise ValueError

    def clear(self) -> None:
        """Clearing method.

        Sets all attributes to None.
        """
        self.__wrap = None
        self.__drink = None
        self.__side = None
        self.__name = None

    @property
    def price(self) -> float:
        """Getter for price.

        Gets the price of all items,
        including discount if applicable.

        Returns:
            A float representing the
            price of the combo.
        """
        if (self.__wrap is not None and
                self.__drink is not None and
                self.__side is not None):
            return (self.__wrap.price +
                    self.__drink.price +
                    self.__side.price - self._Combo__discount)
        else:
            total_price = 0
            if self.__wrap is not None:
                total_price = total_price + self.__wrap.price
            if self.__drink is not None:
                total_price = total_price + self.__drink.price
            if self.__side is not None:
                total_price = total_price + self.__side.price
            return total_price

    @property
    def calories(self) -> int:
        """Getter for calories.

        Gets the calories of all items.

        Returns:
            A int representing the
            calories in the combo.
        """
        total_calories = 0
        if self.__wrap is not None:
            total_calories = total_calories + self.__wrap.calories
        if self.__drink is not None:
            total_calories = total_calories + self.__drink.calories
        if self.__side is not None:
            total_calories = total_calories + self.__side.calories
        return total_calories

    @property
    def instructions(self) -> List[str]:
        """Getter for instructions.

        Gets the instructions.

        Returns:
            A list of strings representing the
            instructions for the combo.
        """
        instructions = list()
        if self.__name is not None:
            instructions.append(self.__name)
        else:
            instructions.append("Custom Combo")
        if (self.__wrap is not None and
            self.__drink is not None and
            self.__side is not None):
            instructions.append("${} Discount Applied".format(
                               self._Combo__discount))
        return instructions

    @property
    def items_in_combo(self) -> List[Item]:
        """Getter for list of items.

        Gets a list of items in the combo,
        omitting None type objects.

        Returns:
            A list of Item objects representing
            the items in the combo.
        """
        item_list: List[Item] = list()
        if self.__wrap is not None:
            item_list.append(self.__wrap)
        if self.__drink is not None:
            item_list.append(self.__drink)
        if self.__side is not None:
            item_list.append(self.__side)
        return item_list

    def __eq__(self, c: object) -> bool:
        """Equals method.

        Overwrites native __eq__ such that
        two combos are equal if all attributes
        are equal.

        Args:
            c: The object to compare to.
        
        Returns:
            True if the two objects are
            equal, False otherwise.
        """
        if not isinstance(c, Combo):
            return False
        else:
            return (self.__wrap == c.wrap and
                    self.__drink == c.drink and
                    self.__side == c.side and
                    self.__name == c.name)       
