"""The Tests for the Order class.

This file contains a number of unit tests
used to verify that the Order class is
working correctly.

Author: Dustin Hayes djhayes@ksu.edu
Version 0.1
"""
from src.thatsawrap.data.order.Order import Order
from src.thatsawrap.data.order.OrderNumberSingleton import OrderNumberSingleton
import pytest
from unittest.mock import patch, PropertyMock
from src.thatsawrap.data.drinks.ForrestGump import ForrestGump
from src.thatsawrap.data.wraps.TheGodFather import TheGodFather
from src.thatsawrap.data.sides.Side import Side


class TestOrder:
    """Order class test class.

    This class contains all of the unit
    tests for Order.
    """
    def test_order_is_empty_when_initialized(self):
        """Test that order is empty.

        This test verifies that an
        Order object is empty at
        initialization.
        """
        ord = Order()
        assert len(ord) == 0
        assert ord.tax == 0
        assert ord.subtotal == 0
        assert ord.total == 0
        assert ord.calories == 0

    def test_bad_tax_rate_throws_exception(self):
        """Test bad rate throws exception.

        This test verifies that
        attempting to set the tax rate
        to a number that is not in (0,1)
        raises an exception.
        """
        ord = Order()
        with pytest.raises(Exception):
            ord.tax_rate = -.5
        with pytest.raises(Exception):
            ord.tax_rate = 1.5

    @patch('src.thatsawrap.data.wraps.TheGodFather', spec=TheGodFather)
    @patch('src.thatsawrap.data.drinks.ForrestGump', spec=ForrestGump)
    @patch('src.thatsawrap.data.sides.Side', spec=Side)
    def test_adding_removing_changes_order(self, mock_wrap,
                                           mock_drink, mock_side) -> None:
        """Test adding and removing items.

        This test verifies that
        adding and removing items
        to the order correctly updates
        the state of the instance.

        Args:
            mock_wrap: A fake wrap.
            mock_drink: A fake drink.
            mock_side: A fake side.
        """
        ord = Order()
        type(mock_wrap).calories = PropertyMock(return_value=1)
        type(mock_drink).calories = PropertyMock(return_value=1)
        type(mock_side).calories = PropertyMock(return_value=2)
        type(mock_wrap).price = PropertyMock(return_value=5.5)
        type(mock_drink).price = PropertyMock(return_value=4.5)
        type(mock_side).price = PropertyMock(return_value=3.5)
        before_cal = ord.calories
        before_tax = ord.tax
        before_subtotal = ord.subtotal
        before_total = ord.total
        before_len = len(ord)
        ord.add_item(mock_wrap)
        ord.add_item(mock_side)
        ord.add_item(mock_drink)
        assert len(ord) != before_len
        assert ord.calories != before_cal
        assert ord.total != before_total
        assert ord.subtotal != before_subtotal
        assert ord.tax != before_tax
        next_cal = ord.calories
        next_tax = ord.tax
        next_subtotal = ord.subtotal
        next_total = ord.total
        next_len = len(ord)
        ord.remove_item(mock_drink)
        assert len(ord) != next_len
        assert ord.calories != next_cal
        assert ord.total != next_total
        assert ord.subtotal != next_subtotal
        assert ord.tax != next_tax

    def test_order_contains_uses_instance_comp_not_eq(self):
        """Test uses instance comparison.

        This test verifies that
        the program uses instance comparison
        to see if an item is in the order.
        """
        ord = Order()
        god = TheGodFather()
        god2 = TheGodFather()
        ord.add_item(god)
        assert god in ord
        assert god2 not in ord

    def test_order_used_instance_comp_for_removal(self):
        """Test add/remove uses instance comparison.

        This test verifies that
        the program uses instance comparison
        to add and remove items.
        """
        ord = Order()
        god = TheGodFather()
        god2 = TheGodFather()
        ord.add_item(god)
        with pytest.raises(Exception):
            ord.remove_item(god2)
        assert god in ord

    @patch('src.thatsawrap.data.order.OrderNumberSingleton',
           spec=OrderNumberSingleton)
    def test_creation_uses_ordernumbersingleton(self, mock_order_single):
        """Test Order correctly gets order number.

        This test verifies that Order will
        correstly get the value for order_number
        from the order number singleton.

        Args:
            mock_order_single: Fake OrderNumberSingleton
            set to return a specific value for
            order number
        """
        type(mock_order_single).get_next_order_number = PropertyMock(return_value=5)
        assert Order().order_number == 6

    def test_tax_rate_is_global(self):
        """Test tax rate is global.

        This test verifies that changing the
        tax rate will affect all instances of
        Order.
        """
        ord1 = Order()
        ord2 = Order()
        ord1.set_tax_rate(.15)
        assert ord2.tax_rate == .15
        assert ord1.tax_rate == .15

    @patch('src.thatsawrap.data.wraps.TheGodFather', spec=TheGodFather)
    @patch('src.thatsawrap.data.drinks.ForrestGump', spec=ForrestGump)
    @patch('src.thatsawrap.data.sides.Side', spec=Side)
    def test_fake_items_can_be_accessed_by_index(self, mock_wrap,
                                                 mock_drink, mock_side):
        """Test items can be accessed by index.

        This test verifies that
        objects in the order can be accessed
        by their index.

        Args:
            mock_wrap: A fake wrap.
            mock_drink: A fake drink.
            mock_side: A fake side.
        """
        ord = Order()
        ord.add_item(mock_wrap)
        ord.add_item(mock_drink)
        ord.add_item(mock_side)
        assert ord[0] == mock_wrap
        assert ord[1] == mock_drink
        assert ord[2] == mock_side

    @patch('src.thatsawrap.data.wraps.TheGodFather', spec=TheGodFather)
    @patch('src.thatsawrap.data.drinks.ForrestGump', spec=ForrestGump)
    @patch('src.thatsawrap.data.sides.Side', spec=Side)
    def test_fake_items_are_returned_in_order(self, mock_wrap,
                                              mock_drink, mock_side):
        """Test iterator.

        This test verifies that the iterator
        functions properly.

        Args:
            mock_wrap: A fake wrap.
            mock_drink: A fake drink.
            mock_side: A fake side.
        """
        ord = Order()
        ord.add_item(mock_wrap)
        ord.add_item(mock_drink)
        ord.add_item(mock_side)
        test_list = []
        for item in ord:
            test_list.append(item)
        assert test_list[0] == mock_wrap
        assert test_list[1] == mock_drink
        assert test_list[2] == mock_side
