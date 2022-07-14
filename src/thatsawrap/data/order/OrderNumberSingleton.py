"""Order Number Singleton.

Follows builder pattern to generate
order numbers.

Author: Dustin hayes djhayes@ksu.edu
Version: 0.1
"""
import threading
from typing import Optional


class OrderNumberSingleton:
    """Order Number Singleton.

    Follows builder pattern to generate
    order numbers.
    """
    next_order_number: int = 0
    _instance: Optional["OrderNumberSingleton"] = None
    lock = threading.Lock()

    def __new__(cls) -> "OrderNumberSingleton":
        """Order Number Singleton.

        Overwites __new__ function such that
        a new instance will only be created if
        the Singleton does not exist yet.
        Otherwise, it will return the
        OrderNumberSingleton object that already
        exists.

        Returns:
            A string representation of the class.
        """
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def get_next_order_number(self) -> int:
        """Next order number function.

        Iterates the class variable indicating
        order number and returns it.  Locks
        thread.

        Returns:
            An int indicating order number.
        """
        with OrderNumberSingleton.lock:
            single_in = self._instance
            single_in.next_order_number += 1
            return single_in.next_order_number
