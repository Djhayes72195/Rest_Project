"""The Tests for the Forrest Gump Panel.

This file contains a number of unit tests
used to verify that the Forrest Gump panel is
working correctly.

Author: Dustin Hayes djhayes@ksu.edu
Version 0.1
"""
import pytest
from src.thatsawrap.data.enums.Size import Size
from src.thatsawrap.data.drinks.ForrestGump import ForrestGump
from src.thatsawrap.gui.drinks.ForrestGumpPanel import ForrestGumpPanel
from src.thatsawrap.gui.PrimaryWindow import PrimaryWindow


class TestForrestGumpPanel:
    """Forrest Gump panel test class.

    This class contains all of the unit
    tests for the Forrest Gump Panel.
    """
    def test_new_panel_without_item(self):
        """New Panel test.

        Verifies that a new Forrest Gump
        panel that is given no arguments
        contains an instance of the Forrest
        Gump.
        """
        master = PrimaryWindow()
        forrest_p = ForrestGumpPanel(master)
        assert isinstance(forrest_p._item, ForrestGump)

    def test_invalid_action_does_not_throw_exception(self):
        """Invalid action test.

        Verifies that the action_performed
        method does not throw and Exception
        if provided with bad input.
        """
        master = PrimaryWindow()
        forrest_p = ForrestGumpPanel(master)
        try:
            forrest_p.action_performed("bad")
        except Exception:
            assert False

    @pytest.mark.parametrize("t_size", [Size.INDIE, Size.STUDIO,
                                        Size.BLOCKBUSTER])
    def test_panel_with_item_provided_has_correct_size_combobox(self, t_size):
        """Correct size test.

        Verifies that the Forrest Gump
        panel correctly sets the size
        in the combobox.

        Args:
            t_size: Used to parameterize the test
            for each size.
        """
        forrest = ForrestGump()
        forrest.size = t_size
        master = PrimaryWindow()
        forrest_p = ForrestGumpPanel(master, item=forrest)
        assert forrest_p._size.get() == t_size

    def test_panel_sets_chocolate_according_to_item_provided(self):
        """Correct ingredient test.

        Verifies that the Forrest Gump
        panel correctly sets chocolate.
        """
        forrest = ForrestGump()
        master = PrimaryWindow()
        forrest_p = ForrestGumpPanel(master, item=forrest)
        assert forrest_p._chocolate.get()
        forrest.chocolate = False
        forrest_p = ForrestGumpPanel(master, item=forrest)
        assert not forrest_p._chocolate.get()

    def test_panel_sets_vanilla_according_to_item_provided(self):
        """Correct ingredient test.

        Verifies that the Forrest Gump
        panel correctly sets vanilla.
        """
        forrest = ForrestGump()
        master = PrimaryWindow()
        forrest_p = ForrestGumpPanel(master, item=forrest)
        assert not forrest_p._vanilla.get()
        forrest.vanilla = True
        forrest_p = ForrestGumpPanel(master, item=forrest)
        assert forrest_p._chocolate.get()

    def test_panel_sets_coffee_according_to_item_provided(self):
        """Correct ingredient test.

        Verifies that the Forrest Gump
        panel correctly sets coffee.
        """
        forrest = ForrestGump()
        master = PrimaryWindow()
        forrest_p = ForrestGumpPanel(master, item=forrest)
        assert not forrest_p._coffee.get()
        forrest.coffee = True
        forrest_p = ForrestGumpPanel(master, item=forrest)
        assert forrest_p._coffee.get()

    def test_panel_sets_caramel_according_to_item_provided(self):
        """Correct ingredient test.

        Verifies that the Forrest Gump
        panel correctly sets caramel.
        """
        forrest = ForrestGump()
        master = PrimaryWindow()
        forrest_p = ForrestGumpPanel(master, item=forrest)
        assert not forrest_p._caramel.get()
        forrest.caramel = True
        forrest_p = ForrestGumpPanel(master, item=forrest)
        assert forrest_p._caramel.get()

    @pytest.mark.parametrize("t_size", [Size.INDIE, Size.STUDIO,
                                        Size.BLOCKBUSTER])
    def test_saved_item_has_correct_size(self, t_size):
        """Correct size of saved item test.

        Verifies that the Forrest Gump
        panel correctly sets the size
        of an item once it has been saved.

        Args:
            t_size: Used to parameterize the test
            for each size.
        """
        forrest = ForrestGump()
        forrest.size = t_size
        master = PrimaryWindow()
        forrest_p = ForrestGumpPanel(master, item=forrest)
        forrest_p.action_performed("save")
        assert forrest_p._item.size == t_size
        forrest_p2 = ForrestGumpPanel(master)
        forrest_p2._size.set(t_size)
        assert forrest_p._item.size == t_size

    def test_saved_item_has_correct_chocolate(self):
        """Correct ingredient test.

        Verifies that the Forrest Gump
        panel correctly sets chocolate
        when saved.
        """
        master = PrimaryWindow()
        forrest_p = ForrestGumpPanel(master)
        forrest_p.action_performed("save")
        assert forrest_p._item.chocolate
        forrest_p._chocolate.set(False)
        forrest_p.action_performed("save")
        assert not forrest_p._item.chocolate

    def test_saved_item_has_correct_vanilla(self):
        """Correct ingredient test.

        Verifies that the Forrest Gump
        panel correctly sets vanilla
        when saved.
        """
        master = PrimaryWindow()
        forrest_p = ForrestGumpPanel(master)
        forrest_p.action_performed("save")
        assert not forrest_p._item.vanilla
        forrest_p._chocolate.set(True)
        forrest_p.action_performed("save")
        assert forrest_p._item.chocolate

    def test_saved_item_has_correct_coffee(self):
        """Correct ingredient test.

        Verifies that the Forrest Gump
        panel correctly sets coffee
        when saved.
        """
        master = PrimaryWindow()
        forrest_p = ForrestGumpPanel(master)
        forrest_p.action_performed("save")
        assert not forrest_p._item.coffee
        forrest_p._coffee.set(True)
        forrest_p.action_performed("save")
        assert forrest_p._item.coffee

    def test_saved_item_has_correct_caramel(self):
        """Correct ingredient test.

        Verifies that the Forrest Gump
        panel correctly sets caramel
        when saved.
        """
        master = PrimaryWindow()
        forrest_p = ForrestGumpPanel(master)
        forrest_p.action_performed("save")
        assert not forrest_p._item.caramel
        forrest_p._caramel.set(True)
        forrest_p.action_performed("save")
        assert forrest_p._item.caramel

    def test_canceled_item_does_not_change(self):
        """Cancle button test.

        Verifies that changes are not
        saved when the cancel button is
        hit.
        """
        forrest = ForrestGump()
        master = PrimaryWindow()
        forrest_p = ForrestGumpPanel(master, item=forrest)
        forrest_p._caramel.set(True)
        forrest_p._size.set(Size.BLOCKBUSTER)
        forrest_p.action_performed("cancel")
        assert forrest_p._item == forrest
