"""The Tests for the King Kong Panel.

This file contains a number of unit tests
used to verify that the King Kong panel is
working correctly.

Author: Dustin Hayes djhayes@ksu.edu
Version 0.1
"""
import pytest
from src.thatsawrap.data.enums.Size import Size
from src.thatsawrap.data.drinks.KingKong import KingKong
from src.thatsawrap.gui.drinks.KingKongPanel import KingKongPanel
from src.thatsawrap.gui.PrimaryWindow import PrimaryWindow


class TestKingKongPanel:
    """King Kong panel test class.

    This class contains all of the unit
    tests for the King Kong Panel.
    """
    def test_new_panel_without_item(self):
        """New Panel test.

        Verifies that a new King Kong
        panel that is given no arguments
        contains an instance of the King
        Kong.
        """
        master = PrimaryWindow()
        kong_p = KingKongPanel(master)
        assert isinstance(kong_p._item, KingKong)

    def test_invalid_action_does_not_throw_exception(self):
        """Invalid action test.

        Verifies that the action_performed
        method does not throw and Exception
        if provided with bad input.
        """
        master = PrimaryWindow()
        kong_p = KingKongPanel(master)
        try:
            kong_p.action_performed("bad")
        except Exception:
            assert False

    @pytest.mark.parametrize("t_size", [Size.INDIE, Size.STUDIO,
                                        Size.BLOCKBUSTER])
    def test_panel_with_item_provided_has_correct_size_combobox(self, t_size):
        """Correct size test.

        Verifies that the King Kong
        panel correctly sets the size
        in the combobox.

        Args:
            t_size: Used to parameterize the test
            for each size.
        """
        kong = KingKong()
        kong.size = t_size
        master = PrimaryWindow()
        kong_p = KingKongPanel(master, item=kong)
        assert kong_p._size.get() == t_size

    def test_panel_sets_banana_according_to_item_provided(self):
        """Correct ingredient test.

        Verifies that the King Kong
        panel correctly sets banana.
        """
        kong = KingKong()
        master = PrimaryWindow()
        kong_p = KingKongPanel(master, item=kong)
        assert kong_p._banana.get()
        kong.banana = False
        kong_p = KingKongPanel(master, item=kong)
        assert not kong_p._banana.get()

    def test_panel_sets_strawberry_according_to_item_provided(self):
        """Correct ingredient test.

        Verifies that the King Kong
        panel correctly sets strawberry.
        """
        kong = KingKong()
        master = PrimaryWindow()
        kong_p = KingKongPanel(master, item=kong)
        assert not kong_p._strawberry.get()
        kong.strawberry = True
        kong_p = KingKongPanel(master, item=kong)
        assert kong_p._banana.get()

    def test_panel_sets_mango_according_to_item_provided(self):
        """Correct ingredient test.

        Verifies that the King Kong
        panel correctly sets mango.
        """
        kong = KingKong()
        master = PrimaryWindow()
        kong_p = KingKongPanel(master, item=kong)
        assert not kong_p._mango.get()
        kong.mango = True
        kong_p = KingKongPanel(master, item=kong)
        assert kong_p._mango.get()

    def test_panel_sets_peach_according_to_item_provided(self):
        """Correct ingredient test.

        Verifies that the King Kong
        panel correctly sets peach.
        """
        kong = KingKong()
        master = PrimaryWindow()
        kong_p = KingKongPanel(master, item=kong)
        assert not kong_p._peach.get()
        kong.peach = True
        kong_p = KingKongPanel(master, item=kong)
        assert kong_p._peach.get()

    @pytest.mark.parametrize("t_size", [Size.INDIE, Size.STUDIO,
                                        Size.BLOCKBUSTER])
    def test_saved_item_has_correct_size(self, t_size):
        """Correct size of saved item test.

        Verifies that the King Kong
        panel correctly sets the size
        of an item once it has been saved.

        Args:
            t_size: Used to parameterize the test
            for each size.
        """
        kong = KingKong()
        kong.size = t_size
        master = PrimaryWindow()
        kong_p = KingKongPanel(master, item=kong)
        kong_p.action_performed("save")
        assert kong_p._item.size == t_size
        kong_p2 = KingKongPanel(master)
        kong_p2._size.set(t_size)
        assert kong_p._item.size == t_size

    def test_saved_item_has_correct_banana(self):
        """Correct ingredient test.

        Verifies that the King Kong
        panel correctly sets banana
        when saved.
        """
        master = PrimaryWindow()
        kong_p = KingKongPanel(master)
        kong_p.action_performed("save")
        assert kong_p._item.banana
        kong_p._banana.set(False)
        kong_p.action_performed("save")
        assert not kong_p._item.banana

    def test_saved_item_has_correct_strawberry(self):
        """Correct ingredient test.

        Verifies that the King Kong
        panel correctly sets strawberry
        when saved.
        """
        master = PrimaryWindow()
        kong_p = KingKongPanel(master)
        kong_p.action_performed("save")
        assert not kong_p._item.strawberry
        kong_p._banana.set(True)
        kong_p.action_performed("save")
        assert kong_p._item.banana

    def test_saved_item_has_correct_mango(self):
        """Correct ingredient test.

        Verifies that the King Kong
        panel correctly sets mango
        when saved.
        """
        master = PrimaryWindow()
        kong_p = KingKongPanel(master)
        kong_p.action_performed("save")
        assert not kong_p._item.mango
        kong_p._mango.set(True)
        kong_p.action_performed("save")
        assert kong_p._item.mango

    def test_saved_item_has_correct_peach(self):
        """Correct ingredient test.

        Verifies that the King Kong
        panel correctly sets peach
        when saved.
        """
        master = PrimaryWindow()
        kong_p = KingKongPanel(master)
        kong_p.action_performed("save")
        assert not kong_p._item.peach
        kong_p._peach.set(True)
        kong_p.action_performed("save")
        assert kong_p._item.peach

    def test_canceled_item_does_not_change(self):
        """Cancle button test.

        Verifies that changes are not
        saved when the cancel button is
        hit.
        """
        kong = KingKong()
        master = PrimaryWindow()
        kong_p = KingKongPanel(master, item=kong)
        kong_p._peach.set(True)
        kong_p._size.set(Size.BLOCKBUSTER)
        kong_p.action_performed("cancel")
        assert kong_p._item == kong
