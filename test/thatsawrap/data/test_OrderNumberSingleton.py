"""The Tests for the OrderNumberSingleton file.

This file contains a number of unit tests
used to verify that the OrderNumberSingleton class is
working correctly.

Author: Dustin Hayes djhayes@ksu.edu
Version 0.1
"""
from src.thatsawrap.data.order.OrderNumberSingleton import OrderNumberSingleton


class TestOrderNumberSingleton:
    """The Tests for the OrderNumberSingleton class.

    This class contains the unit tests
    used to verify that the OrderNumberSingleton class is
    working correctly.
    """
    def test_order_number_is_sequential(self):
        """test order number goes up by 1.

        This test verifies that the OrderNumberSingleton
        goes up by one each time get_next_order_number
        is called.
        """
        ord_num_1 = OrderNumberSingleton().get_next_order_number()
        ord_num_2 = OrderNumberSingleton().get_next_order_number()
        assert ord_num_1 + 1 == ord_num_2
        ord_num_3 = OrderNumberSingleton().get_next_order_number()
        ord_num_4 = OrderNumberSingleton().get_next_order_number()
        assert ord_num_3 + 1 == ord_num_4
        ord_num_5 = OrderNumberSingleton().get_next_order_number()
        ord_num_6 = OrderNumberSingleton().get_next_order_number()
        assert ord_num_5 + 1 == ord_num_6
