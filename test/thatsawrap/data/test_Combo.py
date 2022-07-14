"""The Tests for the Combo file.

This file contains a number of unit tests
used to verify that the Combo class is
working correctly.

Author: Dustin Hayes djhayes@ksu.edu
Version 0.1
"""
from src.thatsawrap.data.drinks.ForrestGump import ForrestGump
from src.thatsawrap.data.wraps.TheGodFather import TheGodFather
from src.thatsawrap.data.wraps.Wrap import Wrap
from src.thatsawrap.data.drinks.Drink import Drink
from src.thatsawrap.data.sides.Side import Side
from src.thatsawrap.data.order.Combo import Combo
import pytest
from unittest.mock import patch, PropertyMock


class TestCombo:
    """The Tests for the Combo class.

    This file contains all the unit tests
    used to verify that the Combo class is
    working correctly.
    """
    def test_name_is_set_correctly(self):
        """Test name is set correctly.

        This test verifies that Combo
        will set a name if provided with one.
        """
        comb = Combo(name="test")
        assert comb.name == "test"

    def test_none_name_handled_property(self):
        """Test None name is set correctly.

        This test verifies that Combo
        will correctly handle name=None.
        """
        comb = Combo(name=None)
        assert comb.name is None

    def test_constructor_sets_attr_to_none(self):
        """Test attributes set to None.

        This test verifies that new Combo
        sets all atrributes to None.
        """
        comb = Combo()
        assert comb.wrap is None
        assert comb.drink is None
        assert comb.side is None

    def test_calories_total_set_to_zero(self):
        """Test price and calories are zero.

        This test verifies that new Combo
        has calories = 0 and total = 0.
        """
        comb = Combo()
        assert comb.calories == 0
        assert comb.price == 0

    def test_discount_can_be_positive_or_zero(self):
        """Test discount can be >= 0.

        This test verifies that discount
        can be set to zero or a positive
        number.
        """
        comb = Combo()
        with pytest.raises(ValueError):
            comb.set_discount(-.1)
        try:
            comb.set_discount(0)
        except Exception:
            assert False
        comb.set_discount(.95)

    @patch('src.thatsawrap.data.wraps.TheGodFather', spec=TheGodFather)
    @patch('src.thatsawrap.data.drinks.ForrestGump', spec=ForrestGump)
    @patch('src.thatsawrap.data.sides.Side', spec=Side)
    def test_adding_items_changes_price(self, mock_wrap, mock_drink, mock_side):
        """Test price changes with items.

        This test verifies that adding and removing
        items changes the price of the combo accordingly.

        Args:
            mock_wrap: A fake wrap.
            mock_drink: A fake drink.
            mock_side: A fake side.
        """
        combo = Combo()
        mock_wrap.__class__ = Wrap
        mock_drink.__class__ = Drink
        mock_side.__class__ = Side
        type(mock_wrap).price = PropertyMock(return_value=1)
        type(mock_drink).price = PropertyMock(return_value=2)
        type(mock_side).price = PropertyMock(return_value=3)
        combo.wrap = mock_wrap
        assert combo.price == 1
        combo.drink = mock_drink
        assert combo.price == 3
        combo.wrap = None
        combo.side = mock_side
        assert combo.price == 5

    @patch('src.thatsawrap.data.wraps.TheGodFather', spec=TheGodFather)
    @patch('src.thatsawrap.data.drinks.ForrestGump', spec=ForrestGump)
    @patch('src.thatsawrap.data.sides.Side', spec=Side)
    def test_adding_items_changes_calories(self, mock_wrap, mock_drink, mock_side):
        """Test calories changes with items.

        This test verifies that adding and removing
        items changes calories of the combo accordingly.

        Args:
            mock_wrap: A fake wrap.
            mock_drink: A fake drink.
            mock_side: A fake side.
        """
        combo = Combo()
        mock_wrap.__class__ = Wrap
        mock_drink.__class__ = Drink
        mock_side.__class__ = Side
        type(mock_wrap).calories = PropertyMock(return_value=1)
        type(mock_drink).calories = PropertyMock(return_value=2)
        type(mock_side).calories = PropertyMock(return_value=3)
        combo.wrap = mock_wrap
        assert combo.calories == 1
        combo.drink = mock_drink
        assert combo.calories == 3
        combo.wrap = None
        combo.side = mock_side
        assert combo.calories == 5

    @patch('src.thatsawrap.data.wraps.TheGodFather', spec=TheGodFather)
    @patch('src.thatsawrap.data.drinks.ForrestGump', spec=ForrestGump)
    @patch('src.thatsawrap.data.sides.Side', spec=Side)
    def test_having_all_items_gives_discount(self, mock_wrap, mock_drink, mock_side):
        """Test all items gives discount.

        This test verifies that combos
        with a wrap, drink and side
        gives a discount.

        Args:
            mock_wrap: A fake wrap.
            mock_drink: A fake drink.
            mock_side: A fake side.
        """
        combo = Combo()
        mock_wrap.__class__ = Wrap
        mock_drink.__class__ = Drink
        mock_side.__class__ = Side
        type(mock_wrap).price = PropertyMock(return_value=1)
        type(mock_drink).price = PropertyMock(return_value=2)
        type(mock_side).price = PropertyMock(return_value=3)
        combo.wrap = mock_wrap
        combo.drink = mock_drink
        combo.side = mock_side
        assert combo.wrap is not None
        assert combo.drink is not None
        assert combo.side is not None
        assert combo.price == 5.05

    @patch('src.thatsawrap.data.wraps.TheGodFather', spec=TheGodFather)
    @patch('src.thatsawrap.data.drinks.ForrestGump', spec=ForrestGump)
    def test_not_having_all_items_gives_no_discount(self, mock_wrap, mock_drink):
        """Test not having all items no discount.

        This test verifies that a combo without
        all three items does not come with
        a discount.

        Args:
            mock_wrap: A fake wrap.
            mock_drink: A fake drink.
        """
        combo = Combo()
        mock_wrap.__class__ = Wrap
        mock_drink.__class__ = Drink
        type(mock_wrap).price = PropertyMock(return_value=1)
        type(mock_drink).price = PropertyMock(return_value=2)
        combo.wrap = mock_wrap
        combo.drink = mock_drink
        assert combo.price == 3

    def test_discount_is_global(self):
        """Test discount is global.

        This test verifies that a changes
        in discount is global.
        """
        combo1 = Combo()
        combo2 = Combo()
        combo1.set_discount(.5)
        assert combo1.get_discount() == .5
        assert combo2.get_discount() == .5

    @patch('src.thatsawrap.data.wraps.TheGodFather', spec=TheGodFather)
    @patch('src.thatsawrap.data.drinks.ForrestGump', spec=ForrestGump)
    @patch('src.thatsawrap.data.sides.Side', spec=Side)
    def test_list_returned_by_combo_is_correct(self, mock_wrap, mock_drink, mock_side):
        """Test list of items in combo.

        This test verifies that the list of
        items in the combo is correct.

        Args:
            mock_wrap: A fake wrap.
            mock_drink: A fake drink.
            mock_side: A fake side.
        """
        combo = Combo()
        mock_wrap.__class__ = Wrap
        mock_drink.__class__ = Drink
        mock_side.__class__ = Side
        combo.wrap = mock_wrap
        combo.drink = mock_drink
        combo.side = mock_side
        assert mock_wrap in combo.items_in_combo
        assert mock_drink in combo.items_in_combo
        assert mock_side in combo.items_in_combo

    def test_combo_with_no_items_list_is_empty(self):
        """Test price changes with items.

        This test verifies that a combo
        with no items has an empty
        item_list.
        """
        combo = Combo()
        assert combo.items_in_combo == []

    def test_instructions_contain_combo_name(self):
        """Test instructions contain names.

        This test verifies that the combo instructions
        include the name of the combo.
        """
        combo = Combo()
        assert "Custom Combo" in combo.instructions
        combo = Combo(name="test")
        assert "test" in combo.instructions

    @patch('src.thatsawrap.data.wraps.TheGodFather', spec=TheGodFather)
    @patch('src.thatsawrap.data.drinks.ForrestGump', spec=ForrestGump)
    @patch('src.thatsawrap.data.sides.Side', spec=Side)
    def test_instructions_contain_discount_message_if_has_all(self, mock_wrap, mock_drink, mock_side):
        """Test instructions show if all items.

        This test verifies that the instructions
        contain a discount message if it has
        a wrap, side and drink.

        Args:
            mock_wrap: A fake wrap.
            mock_drink: A fake drink.
            mock_side: A fake side.
        """
        combo = Combo()
        mock_wrap.__class__ = Wrap
        mock_drink.__class__ = Drink
        mock_side.__class__ = Side
        combo.wrap = mock_wrap
        combo.drink = mock_drink
        combo.side = mock_side
        combo.set_discount(.95)
        assert "$0.95 Discount Applied" in combo.instructions

    def test_adding_wrong_type_of_item_throws_exception(self):
        """Test items must be correct object.

        This test verifies that attempting
        to assign an object to the incorrect
        attribute (saving a Wrap type item
        in self.__drink for example) will result
        in an exception.
        """
        combo = Combo()
        with pytest.raises(Exception):
            combo.wrap = Combo()

    @patch('src.thatsawrap.data.wraps.TheGodFather', spec=TheGodFather)
    @patch('src.thatsawrap.data.drinks.ForrestGump', spec=ForrestGump)
    @patch('src.thatsawrap.data.sides.Side', spec=Side)
    def test_two_combos_with_same_items_and_name_are_eq(self, mock_wrap, mock_drink, mock_side):
        """Test two combo equality.

        This test verifies two combos with
        the same wrap, drink, side and name
        are equal.

        Args:
            mock_wrap: A fake wrap.
            mock_drink: A fake drink.
            mock_side: A fake side.
        """
        combo = Combo(name="test")
        combo2 = Combo(name="test")
        mock_wrap.__class__ = Wrap
        mock_drink.__class__ = Drink
        mock_side.__class__ = Side
        combo.wrap = mock_wrap
        combo.drink = mock_drink
        combo.side = mock_side
        combo2.wrap = mock_wrap
        combo2.drink = mock_drink
        combo2.side = mock_side
        assert combo == combo2

    @patch('src.thatsawrap.data.wraps.TheGodFather', spec=TheGodFather)
    @patch('src.thatsawrap.data.drinks.ForrestGump', spec=ForrestGump)
    @patch('src.thatsawrap.data.sides.Side', spec=Side)
    def test_two_combos_with_same_items_and_different_name_not_eq(self, mock_wrap, mock_drink, mock_side):
        """Test two combo inequality.

        This test verifies that two combos
        that have a different name aren't equal.

        Args:
            mock_wrap: A fake wrap.
            mock_drink: A fake drink.
            mock_side: A fake side.
        """
        combo = Combo(name="test")
        combo2 = Combo(name="test2")
        mock_wrap.__class__ = Wrap
        mock_drink.__class__ = Drink
        mock_side.__class__ = Side
        combo.wrap = mock_wrap
        combo.drink = mock_drink
        combo.side = mock_side
        combo2.wrap = mock_wrap
        combo2.drink = mock_drink
        combo2.side = mock_side
        assert not combo == combo2

    @patch('src.thatsawrap.data.wraps.TheGodFather', spec=TheGodFather)
    @patch('src.thatsawrap.data.drinks.ForrestGump', spec=ForrestGump)
    @patch('src.thatsawrap.data.sides.Side', spec=Side)
    def test_two_combos_with_different_items_same_name_not_eq(self, mock_wrap, mock_drink, mock_side):
        """Test two combo inequality.

        This test verifies that two combos
        that have a different set of
        (drink, wrap, side) aren't equal.

        Args:
            mock_wrap: A fake wrap.
            mock_drink: A fake drink.
            mock_side: A fake side.
        """
        combo = Combo(name="test")
        combo2 = Combo(name="test")
        mock_wrap.__class__ = Wrap
        mock_drink.__class__ = Drink
        mock_side.__class__ = Side
        combo.drink = mock_drink
        combo.side = mock_side
        combo2.wrap = mock_wrap
        combo2.drink = mock_drink
        combo2.side = mock_side
        assert not combo == combo2

    def test_two_empty_combos_are_eq(self):
        """Test two combo equality.

        This test verifies that two combos
        that have the same set of
        (drink, wrap, side, name) are equal.
        """
        combo = Combo()
        combo2 = Combo()
        assert combo == combo2

    @patch('src.thatsawrap.data.wraps.TheGodFather', spec=TheGodFather)
    def test_two_combos_one_empty_are_not_eq(self, mock_wrap):
        """Test two combo inequality.

        This test verifies that two combos,
        only one of which being empty, are
        not equal.
        """
        combo = Combo()
        combo2 = Combo()
        mock_wrap.__class__ = Wrap
        combo.wrap = mock_wrap
        assert not combo == combo2

    def test_combo_is_not_equal_to_other_object(self):
        """Test combo inequality.

        This test verifies that a combo
        is not equal to an object of another
        type.
        """
        combo = Combo()
        god = TheGodFather()
        assert not god == combo
