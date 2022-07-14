"""The Tests for the WestSideStory Panel.

This file contains a number of unit tests
used to verify that the WestSideStory panel is
working correctly.

Author: Dustin Hayes djhayes@ksu.edu
Version 0.1
"""
import pytest
from src.thatsawrap.data.enums.Shell import Shell
from src.thatsawrap.data.enums.Addin import Addin
from src.thatsawrap.data.wraps.WestSideStory import WestSideStory
from src.thatsawrap.gui.wraps.WestSideStoryPanel import WestSideStoryPanel
from src.thatsawrap.gui.PrimaryWindow import PrimaryWindow


class TestWestSideStoryPanel:
    """WestSideStory panel test class.

    This class contains all of the unit
    tests for the WestSideStory Panel.
    """
    def test_new_panel_without_item(self):
        """New Panel test.

        Verifies that a new WestSideStory
        panel that is given no arguments
        contains an instance of WestSideStory.
        """
        master = PrimaryWindow()
        westy_p = WestSideStoryPanel(master)
        assert isinstance(westy_p._item, WestSideStory)

    def test_invalid_action_does_not_throw_exception(self):
        """Invalid action test.

        Verifies that the action_performed
        method does not throw and Exception
        if provided with bad input.
        """
        master = PrimaryWindow()
        westy_p = WestSideStoryPanel(master)
        try:
            westy_p.action_performed("bad")
        except Exception:
            assert False

    @pytest.mark.parametrize("t_shell", [Shell.STROMBOLI, Shell.SPINACH,
                                         Shell.WHOLE_GRAIN])
    def test_panel_with_item_provided_correct_shell_combobox(self, t_shell):
        """Correct shell test.

        Verifies that the WestSideStory
        panel correctly sets the shell
        in the combobox.

        Args:
            t_shell: Used to parameterize the test
            for each shell.
        """
        westy = WestSideStory()
        westy.shell = t_shell
        master = PrimaryWindow()
        westy_p = WestSideStoryPanel(master, item=westy)
        assert westy_p._shell.get() == t_shell

    def test_panel_sets_cheese_according_to_item_provided(self):
        """Correct ingredient test.

        Verifies that the WestSideStory
        panel correctly sets cheese.
        """
        master = PrimaryWindow()
        westy = WestSideStory()
        westy_p = WestSideStoryPanel(master, item=westy)
        assert westy_p._cheese.get()
        westy.cheese = False
        westy_p = WestSideStoryPanel(master, item=westy)
        assert not westy_p._cheese.get()

    def test_panel_sets_cabbage_according_to_item_provided(self):
        """Correct ingredient test.

        Verifies that the WestSideStory
        panel correctly sets cabbage.
        """
        master = PrimaryWindow()
        westy = WestSideStory()
        westy_p = WestSideStoryPanel(master, item=westy)
        assert westy_p._cabbage.get()
        westy.cabbage = False
        westy_p = WestSideStoryPanel(master, item=westy)
        assert not westy_p._cabbage.get()

    def test_panel_sets_corned_beef_according_to_item_provided(self):
        """Correct ingredient test.

        Verifies that the WestSideStory
        panel correctly sets corned
        beef.
        """
        master = PrimaryWindow()
        westy = WestSideStory()
        westy_p = WestSideStoryPanel(master, item=westy)
        assert westy_p._corned_beef.get()
        westy.corned_beef = False
        westy_p = WestSideStoryPanel(master, item=westy)
        assert not westy_p._corned_beef.get()

    def test_panel_saves_cheese_correctly(self):
        """Correct ingredient test.

        Verifies that the WestSideStory
        panel correctly saves cheese.
        """
        master = PrimaryWindow()
        westy = WestSideStory()
        westy_p = WestSideStoryPanel(master, item=westy)
        westy_p.action_performed("save")
        assert westy_p._item.cheese
        westy_p._cheese.set(False)
        westy_p.action_performed("save")
        assert not westy_p._item.cheese

    def test_panel_saves_corned_beef_correctly(self):
        """Correct ingredient test.

        Verifies that the WestSideStory
        panel correctly saves marinara.
        """
        master = PrimaryWindow()
        westy = WestSideStory()
        westy_p = WestSideStoryPanel(master, item=westy)
        westy_p.action_performed("save")
        assert westy_p._item.corned_beef
        westy_p._corned_beef.set(False)
        westy_p.action_performed("save")
        assert not westy_p._item.corned_beef

    def test_panel_saves_cabbage_correctly(self):
        """Correct ingredient test.

        Verifies that the WestSideStory
        panel correctly saves cabbage.
        """
        master = PrimaryWindow()
        westy = WestSideStory()
        westy_p = WestSideStoryPanel(master, item=westy)
        westy_p.action_performed("save")
        assert westy_p._item.cabbage
        westy_p._cabbage.set(False)
        westy_p.action_performed("save")
        assert not westy_p._item.cabbage

    @pytest.mark.parametrize("t_addin", [Addin.PEPPERS, Addin.TOMATOES,
                                         Addin.ONIONS, Addin.PICKLES,
                                         Addin.BUFFALO_SAUCE, Addin.DRESSING,
                                         Addin.MUSTARD])
    def test_addin_checkboxes_set_correctly_true(self, t_addin):
        """Addin checkbox test.

        Verifies that the addin checkboxes
        are set correctly (true).

        Args:
            t_addin: Used to parameterize
            for all addins.
        """
        master = PrimaryWindow()
        westy = WestSideStory()
        westy.add_addin(t_addin)
        westy_p = WestSideStoryPanel(master, item=westy)
        assert westy_p._addins[t_addin].get()

    @pytest.mark.parametrize("t_addin", [Addin.PEPPERS, Addin.TOMATOES,
                                         Addin.ONIONS, Addin.PICKLES,
                                         Addin.BUFFALO_SAUCE, Addin.DRESSING,
                                         Addin.MUSTARD])
    def test_addin_checkboxes_set_correctly_false(self, t_addin):
        """Addin checkbox test.

        Verifies that the addin checkboxes
        are set correctly (false).

        Args:
            t_addin: Used to parameterize
            for all addins.
        """
        master = PrimaryWindow()
        westy = WestSideStory()
        westy.remove_addin(t_addin)
        westy_p = WestSideStoryPanel(master, item=westy)
        assert not westy_p._addins[t_addin].get()

    @pytest.mark.parametrize("t_shell", [Shell.STROMBOLI, Shell.SPINACH,
                                         Shell.WHOLE_GRAIN])
    def test_panel_with_item_provided_saves_correct_shell(self, t_shell):
        """Correct shell test.

        Verifies that the WestSideStory
        panel correctly saves the shell.

        Args:
            t_shell: Used to parameterize the test
            for each shell.
        """
        westy = WestSideStory()
        westy.shell = t_shell
        master = PrimaryWindow()
        westy_p = WestSideStoryPanel(master, item=westy)
        westy_p.action_performed("save")
        assert westy_p._item.shell == t_shell

    @pytest.mark.parametrize("t_addin", [Addin.PEPPERS, Addin.TOMATOES,
                                         Addin.ONIONS, Addin.PICKLES,
                                         Addin.BUFFALO_SAUCE, Addin.DRESSING,
                                         Addin.MUSTARD])
    def test_addin_checkboxes_save_correctly_true(self, t_addin):
        """Addin checkbox test.

        Verifies that WestSideStory
        panel correctly saves the addins
        (true).

        Args:
            t_addin: Used to parameterize
            for all addins.
        """
        master = PrimaryWindow()
        westy = WestSideStory()
        westy.add_addin(t_addin)
        westy_p = WestSideStoryPanel(master, item=westy)
        westy_p.action_performed("save")
        assert t_addin in westy_p._item.addins

    @pytest.mark.parametrize("t_addin", [Addin.PEPPERS, Addin.TOMATOES,
                                         Addin.ONIONS, Addin.PICKLES,
                                         Addin.BUFFALO_SAUCE, Addin.DRESSING,
                                         Addin.MUSTARD])
    def test_addin_checkboxes_save_correctly_false(self, t_addin):
        """Addin checkbox test.

        Verifies that WestSideStory
        panel correctly saves the addins
        (false).

        Args:
            t_addin: Used to parameterize
            for all addins.
        """
        master = PrimaryWindow()
        westy = WestSideStory()
        westy.remove_addin(t_addin)
        westy_p = WestSideStoryPanel(master, item=westy)
        westy_p.action_performed("save")
        assert t_addin not in westy_p._item.addins

    @pytest.mark.parametrize("t_addin", [Addin.PEPPERS, Addin.TOMATOES,
                                         Addin.ONIONS, Addin.PICKLES,
                                         Addin.BUFFALO_SAUCE, Addin.DRESSING,
                                         Addin.MUSTARD])
    def test_cancel_does_not_change_item(self, t_addin):
        """Cancle button test.

        Verifies that the cancel button
        discards changes.

        Args:
            t_addin: Used to parameterize
            for all addins.
        """
        master = PrimaryWindow()
        westy = WestSideStory()
        westy_p = WestSideStoryPanel(master, item=westy)
        westy_p._addins[t_addin].set(False)
        westy_p._cheese.set(False)
        westy_p._shell.set(Shell.SPINACH)
        westy_p.action_performed("cancel")
        assert westy == westy_p._item
