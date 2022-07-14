"""Order class.

Represents a set of Item type objects,
constituting an order.

Author: Dustin hayes djhayes@ksu.edu
Version: 0.1
"""
from typing import Iterator, Iterable, List
from src.thatsawrap.data.menu.Item import Item
from src.thatsawrap.data.order.OrderNumberSingleton import OrderNumberSingleton


class Order(Iterable[Item]):
    """Order class.

    This class represents the order
    and implements standard collection
    methods.
    """
    __tax_rate = 0.125

    def __init__(self) -> None:
        """Constructor for order class.

        Contains the state of the order.
        """
        self.__order: List[Item] = list()
        self.__order_number: int = (OrderNumberSingleton().
                                    get_next_order_number())

    @classmethod
    def set_tax_rate(cls, new_rate: float) -> None:
        """Set tax rate.

        Allows the tax rate to be set
        in the interval (0,1).

        Args:
            new_rate: A float between 0 and
            1.
        """
        if new_rate < 0.0 or new_rate > 1.0:
            raise ValueError
        else:
            cls._Order__tax_rate = new_rate

    @classmethod
    def get_tax_rate(cls) -> float:
        """Get tax rate.

        Gets the tax rate.

        Returns:
            A float between 0 and
            1 corresponding to the tax rate.
        """
        return cls._Order__tax_rate

    def add_item(self, item: Item) -> None:
        """Adds item method.

        Adds an item to the set.

        Args:
            item: The Item type object
            that will be added to the set.
        """
        self.__order.append(item)

    def remove_item(self, item: Item) -> None:
        """Remove item method.

        Removes an item to the set.

        Args:
            item: The Item type object
            that will be removed.
        """
        count = 0
        for i in self.__order:
            if i is item:
                self.__order.remove(item)
                count += 1
        if count != 1:
            raise ValueError

    def __iter__(self) -> Iterator[Item]:
        """Iterator method.

        Mandatory iterator method.

        Returns:
            The iterator object.
        """
        return iter(self.__order)

    def __len__(self) -> int:
        """Iterator method.

        Gives the lenth of the
        iterable object.

        Returns:
            An int representing the
            number of Items in
            the order.
        """
        return len(self.__order)

    def __getitem__(self, position: int) -> Item:
        """Iterator method.

        Takes a position and gives the
        Item stored in that position.

        Args:
            position: An int representing
            the position of the Item object.

        Returns:
            The Item stored at that
            position.
        """
        return self.__order[position]

    def __contains__(self, item: Item) -> bool:
        """Iterator method.

        Used to determine if a particular
        instance of an item is stored
        in the class.

        Args:
            item: The item we are looking
            for.
 
        Returns:
            True if a parituclar instance
            of an item is stored in the class,
            False otherwise.
        """
        ret = False
        for i in self.__order:
            if item is i:
                ret = True
        return ret

    @property
    def tax_rate(self) -> float:
        """Tax rate getter.

        Used for getting the tax rate.

        Returns:
            A float representing
            the tax rate.
        """
        return self.__tax_rate

    @tax_rate.setter
    def tax_rate(self, t_rate: float) -> None:
        """Tax rate setter.

        Used for setting the tax rate.

        Args:
            t_rate: A float representing
            the tax rate.
        """
        if t_rate >= 0.0 and t_rate <= 1.0:
            self.__tax_rate = t_rate
        else:
            raise ValueError

    @property
    def subtotal(self) -> float:
        """Subtotal getter.

        Used for getting the total
        before tax.

        Returns:
            A float representing
            the subtotal.
        """
        sub_t = 0
        for i in self.__order:
            sub_t = sub_t + i.price
        return sub_t

    @property
    def tax(self) -> float:
        """Tax getter.

        Used for getting the tax
        on an order.

        Returns:
            A float representing the tax
            on an order.
        """
        return self.__tax_rate * self.subtotal

    @property
    def total(self) -> float:
        """Total getter.

        Used for getting the total
        for an order, including tax.

        Returns:
            A float representing the total
            price of an order.
        """
        return self.tax + self.subtotal

    @property
    def calories(self) -> float:
        """Calories getter.

        Used for getting the total
        calories of an order.

        Returns:
            A float representing the total
            calories in an order.
        """
        cal = 0
        for i in self.__order:
            cal = cal + i.calories
        return cal

    @property
    def order_number(self) -> int:
        """Order number getter.

        Getter for order number.

        Returns:
            An int representing the order number.
        """
        return self.__order_number
