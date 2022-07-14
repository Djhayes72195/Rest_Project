"""Custom Item List.

This file contains the code required to build
an iterable list of custom items for our web application.

Author: Dustin Hayes djhayes@ksu.edu
Version 0.1
"""
from src.thatsawrap.data.custom.CustomItem import CustomItem
from typing import Iterable, Iterator
import json


class CustomItemList(Iterable[CustomItem]):
    """Custom Item List class.

    This class contains the code required to represent
    a list of CustomItems.
    """
    _instance = None
    _CustomItemList__custom_items = list()

    def __init__(self) -> None:
        """Empty constructor"""
        pass

    def __new__(cls) -> 'CustomItemList':
        """New instance method overide.

        Overides default __new__ method
        to alwayu return the same instance
        of our CustomItemList.  Implements
        singleton design pattern.

        Returns: A reference to this class.
        """
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            try:
                with open("customitems.json") as my_file:
                    item_list = json.load(my_file)
                    for item_dict in item_list:
                        c_item = CustomItem(name=item_dict['name'],
                                            price=item_dict['price'],
                                            calories=item_dict['calories'])
                        cls.__custom_items.append(c_item)
            except Exception as e:
                print(e)
        return cls._instance

    def __setitem__(self, item: CustomItem) -> None:
        """Set item.

        Allows us to append new items to
        the list.

        Args:
            item: A CustomItem type object.
        """
        self.__custom_items.append(item)

    def __getitem__(self, index: int) -> CustomItem:
        """Get item.

        Retrieves an item in the list based of
        of its index.

        Args:
            index: An int representing the
            place of the desired item in the list.
  
        Returns: The CustomItem type object found at the
        index.
        """
        return self.__custom_items[index]

    def update_item(self, index: int, item: CustomItem) -> None:
        """Update item.

        Updates the item at the index passed in as an argument
        to the item passed in as an argument.

        Args:
            index: An int representing the
            place of the desired item in the list.
            item: The item to replace the old item
            at the index.
        """
        self.__custom_items[index] = item

    def __delitem__(self, index: int) -> None:
        """Delete item.

        Deletes the item found at the
        index.

        Args:
            index: An int representing the
            place of the desired item in the list.
        """
        del self.__custom_items[index]

    def __iter__(self) -> Iterator[CustomItem]:
        """returns iterator"""
        return iter(self.__custom_items)

    def __len__(self) -> int:
        """returns length of the list."""
        return len(self.__custom_items)

    def save(self) -> None:
        """Saves list of custom items"""
        json_list = list()
        for item in self.__custom_items:
            item_dict = dict()
            item_dict['name'] = item.name
            item_dict['calories'] = int(item.calories)
            item_dict['price'] = float(item.price)
            json_list.append(item_dict)
        try:
            with open("customitems.json", "w") as my_file:
                json.dump(json_list, my_file)
        except Exception as e:
            print(e)
            