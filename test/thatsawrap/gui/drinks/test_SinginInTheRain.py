"""The Tests for the Singin' in the Rain Panel.

This file contains a number of unit tests
used to verify that the Singin' in the Rain panel is
working correctly.

Author: Dustin Hayes djhayes@ksu.edu
Version 0.1
"""
import pytest
from src.thatsawrap.data.enums.Size import Size
from src.thatsawrap.data.drinks.SinginInTheRain import SinginInTheRain
from src.thatsawrap.gui.drinks.SinginInTheRainPanel import SinginInTheRainPanel
from src.thatsawrap.gui.PrimaryWindow import PrimaryWindow


class TestSinginInTheRainPanel:
    """Singin' in the Rain panel test class.

    This class contains all of the unit
    tests for the Singin' in the Rain Panel.
    """
    def test_new_panel_without_item(self):
        """New Panel test.

        Verifies that a new Singin' in the Rain
        panel that is given no arguments
        contains an instance of the King
        sing.
        """
        master = PrimaryWindow()
        sing_p = SinginInTheRainPanel(master)
        assert isinstance(sing_p._item, SinginInTheRain)

    def test_invalid_action_does_not_throw_exception(self):
        """Invalid action test.

        Verifies that the action_performed
        method does not throw and Exception
        if provided with bad input.
        """
        master = PrimaryWindow()
        sing_p = SinginInTheRainPanel(master)
        try:
            sing_p.action_performed("bad")
        except Exception:
            assert False
   
    @pytest.mark.parametrize("t_size", [Size.INDIE, Size.STUDIO,
                                        Size.BLOCKBUSTER])
    def test_panel_with_item_provided_has_correct_size_combobox(self, t_size):
        """Correct size test.

        Verifies that the Singin' in the Rain
        panel correctly sets the size
        in the combobox.

        Args:
            t_size: Used to parameterize the test
            for each size.
        """
        sing = SinginInTheRain()
        sing.size = t_size
        master = PrimaryWindow()
        sing_p = SinginInTheRainPanel(master, item=sing)
        assert sing_p._size.get() == t_size

    def test_panel_sets_cherry_according_to_item_provided(self):
        """Correct ingredient test.

        Verifies that the Singin' in the Rain
        panel correctly sets cherry.
        """
        sing = SinginInTheRain()
        master = PrimaryWindow()
        sing_p = SinginInTheRainPanel(master, item=sing)
        assert sing_p._cherry.get()
        sing.cherry = False
        sing_p = SinginInTheRainPanel(master, item=sing)
        assert not sing_p._cherry.get()

    def test_panel_sets_cola_according_to_item_provided(self):
        """Correct ingredient test.

        Verifies that the Singin' in the Rain
        panel correctly sets cola.
        """
        sing = SinginInTheRain()
        master = PrimaryWindow()
        sing_p = SinginInTheRainPanel(master, item=sing)
        assert not sing_p._cola.get()
        sing.cola = True
        sing_p = SinginInTheRainPanel(master, item=sing)
        assert sing_p._cherry.get()

    def test_panel_sets_grape_according_to_item_provided(self):
        """Correct ingredient test.

        Verifies that the Singin' in the Rain
        panel correctly sets grape.
        """
        sing = SinginInTheRain()
        master = PrimaryWindow()
        sing_p = SinginInTheRainPanel(master, item=sing)
        assert not sing_p._grape.get()
        sing.grape = True
        sing_p = SinginInTheRainPanel(master, item=sing)
        assert sing_p._grape.get()

    def test_panel_sets_strawberry_according_to_item_provided(self):
        """Correct ingredient test.

        Verifies that the Singin' in the Rain
        panel correctly sets strawberry.
        """
        sing = SinginInTheRain()
        master = PrimaryWindow()
        sing_p = SinginInTheRainPanel(master, item=sing)
        assert not sing_p._strawberry.get()
        sing.strawberry = True
        sing_p = SinginInTheRainPanel(master, item=sing)
        assert sing_p._strawberry.get()

    @pytest.mark.parametrize("t_size", [Size.INDIE, Size.STUDIO,
                                        Size.BLOCKBUSTER])
    def test_saved_item_has_correct_size(self, t_size):
        """Correct size of saved item test.

        Verifies that the Singin' in the Rain
        panel correctly sets the size
        of an item once it has been saved.

        Args:
            t_size: Used to parameterize the test
            for each size.
        """
        sing = SinginInTheRain()
        sing.size = t_size
        master = PrimaryWindow()
        sing_p = SinginInTheRainPanel(master, item=sing)
        sing_p.action_performed("save")
        assert sing_p._item.size == t_size
        sing_p2 = SinginInTheRainPanel(master)
        sing_p2._size.set(t_size)
        assert sing_p._item.size == t_size

    def test_saved_item_has_correct_cherry(self):
        """Correct ingredient test.

        Verifies that the Singin' in the Rain
        panel correctly sets cherry
        when saved.
        """
        master = PrimaryWindow()
        sing_p = SinginInTheRainPanel(master)
        sing_p.action_performed("save")
        assert sing_p._item.cherry
        sing_p._cherry.set(False)
        sing_p.action_performed("save")
        assert not sing_p._item.cherry

    def test_saved_item_has_correct_cola(self):
        """Correct ingredient test.

        Verifies that the Singin' in the Rain
        panel correctly sets cola
        when saved.
        """
        master = PrimaryWindow()
        sing_p = SinginInTheRainPanel(master)
        sing_p.action_performed("save")
        assert not sing_p._item.cola
        sing_p._cherry.set(True)
        sing_p.action_performed("save")
        assert sing_p._item.cherry

    def test_saved_item_has_correct_grape(self):
        """Correct ingredient test.

        Verifies that the Singin' in the Rain
        panel correctly sets grape
        when saved.
        """
        master = PrimaryWindow()
        sing_p = SinginInTheRainPanel(master)
        sing_p.action_performed("save")
        assert not sing_p._item.grape
        sing_p._grape.set(True)
        sing_p.action_performed("save")
        assert sing_p._item.grape

    def test_saved_item_has_correct_strawberry(self):
        """Correct ingredient test.

        Verifies that the Singin' in the Rain
        panel correctly sets strawberry
        when saved.
        """
        master = PrimaryWindow()
        sing_p = SinginInTheRainPanel(master)
        sing_p.action_performed("save")
        assert not sing_p._item.strawberry
        sing_p._strawberry.set(True)
        sing_p.action_performed("save")
        assert sing_p._item.strawberry

    def test_canceled_item_does_not_change(self):
        """Cancle button test.

        Verifies that changes are not
        saved when the cancel button is
        hit.
        """
        sing = SinginInTheRain()
        master = PrimaryWindow()
        sing_p = SinginInTheRainPanel(master, item=sing)
        sing_p._strawberry.set(True)
        sing_p._size.set(Size.BLOCKBUSTER)
        sing_p.action_performed("cancel")
        assert sing_p._item == sing
