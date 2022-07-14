"""The Tests for the Side Panel.

This file contains a number of unit tests
used to verify that the Side panel is
working correctly.

Author: Dustin Hayes djhayes@ksu.edu
Version 0.1
"""
import pytest
from src.thatsawrap.data.enums.Size import Size
from src.thatsawrap.gui.sides.SidePanel import SidePanel
from src.thatsawrap.gui.PrimaryWindow import PrimaryWindow
from src.thatsawrap.data.sides.YankeeDoodleDandy import YankeeDoodleDandy
from src.thatsawrap.data.sides.TheFrenchConnection import TheFrenchConnection
from src.thatsawrap.data.sides.SnowWhite import SnowWhite


class TestSidePanel:
    """Side panel test class.

    This class contains all of the unit
    tests for the Side Panel.
    """
    @pytest.mark.parametrize("t_side", [YankeeDoodleDandy(),
                                        SnowWhite(),
                                        TheFrenchConnection()])
    def test_menu_side_list_has_all_sides(self, t_side):
        """Test instance of side in panel.

        This test verifies that the Side
        panel instantiates a side of the
        correct type.

        Args:
            t_side: Used to parameterize the
            test for each side.
        """
        master = PrimaryWindow()
        side_p = SidePanel(master, t_side.name, t_side)
        t_side.size = Size.STUDIO
        assert isinstance(side_p._item, type(t_side))

    def test_that_exception_is_thrown_if_no_name_given(self):
        """Test no name of side throws exception.

        This test verifies that attempting to
        instantiate the side panel without
        specifying which side throws an
        exception.
        """
        master = PrimaryWindow()
        with pytest.raises(Exception):
            SidePanel(master, item=SnowWhite())

    def test_invalid_action_does_not_throw_exception(self):
        """Invalid action test.

        Verifies that the action_performed
        method does not throw and Exception
        if provided with bad input.
        """
        master = PrimaryWindow()
        yank = YankeeDoodleDandy()
        side_p = SidePanel(master, yank.name, yank)
        try:
            side_p.action_performed("bad")
        except Exception:
            assert False

    @pytest.mark.parametrize("t_size", [Size.INDIE,
                                        Size.STUDIO,
                                        Size.BLOCKBUSTER])
    def test_setting_size_changes_combobox(self, t_size):
        """Test combobox.

        This test verifies that changing
        the size of the item changes the
        combobox.

        Args:
            t_size: Used to parameterize the
            test for each size.
        """
        master = PrimaryWindow()
        yank = YankeeDoodleDandy()
        yank.size = t_size
        side_p = SidePanel(master, yank.name, yank)
        assert side_p._size.get() == t_size
        snow = SnowWhite()
        snow.size = t_size
        side_p = SidePanel(master, snow.name, snow)
        assert side_p._size.get() == t_size
        french = TheFrenchConnection()
        french.size = t_size
        side_p = SidePanel(master, french.name, french)
        assert side_p._size.get() == t_size

    @pytest.mark.parametrize("t_size", [Size.INDIE,
                                        Size.STUDIO,
                                        Size.BLOCKBUSTER])
    def test_pressing_cancel_cancels_changes(self, t_size):
        """Test combobox.

        This test verifies that changing
        the size of the item changes the
        combobox.

        Args:
            t_size: Used to parameterize the
            test for each size.
        """
        master = PrimaryWindow()
        yank = YankeeDoodleDandy()
        side_p = SidePanel(master, yank.name, yank)
        side_p._size.set(t_size)
        side_p.action_performed("cancel")
        assert side_p._item.size == Size.INDIE
        snow = SnowWhite()
        side_p = SidePanel(master, snow.name, snow)
        side_p._size.set(t_size)
        side_p.action_performed("cancel")
        assert side_p._item.size == Size.INDIE
        french = TheFrenchConnection()
        side_p = SidePanel(master, french.name, french)
        side_p._size.set(t_size)
        side_p.action_performed("cancel")
        assert side_p._item.size == Size.INDIE
