"""The Tests for the SomeLikeItHot Panel.

This file contains a number of unit tests
used to verify that the SomeLikeItHot panel is
working correctly.

Author: Dustin Hayes djhayes@ksu.edu
Version 0.1
"""
import pytest
from src.thatsawrap.data.enums.Shell import Shell
from src.thatsawrap.data.enums.Addin import Addin
from src.thatsawrap.data.wraps.SomeLikeItHot import SomeLikeItHot
from src.thatsawrap.gui.wraps.SomeLikeItHotPanel import SomeLikeItHotPanel
from src.thatsawrap.gui.PrimaryWindow import PrimaryWindow


class TestSomeLikeItHotPanel:
    """SomeLikeItHot panel test class.

    This class contains all of the unit
    tests for the SomeLikeItHot Panel.
    """
    def test_new_panel_without_item(self):
        """New Panel test.

        Verifies that a new SomeLikeItHot
        panel that is given no arguments
        contains an instance of SomeLikeItHot.
        """
        master = PrimaryWindow()
        somelike_p = SomeLikeItHotPanel(master)
        assert isinstance(somelike_p._item, SomeLikeItHot)

    def test_invalid_action_does_not_throw_exception(self):
        """Invalid action test.

        Verifies that the action_performed
        method does not throw and Exception
        if provided with bad input.
        """
        master = PrimaryWindow()
        somelike_p = SomeLikeItHotPanel(master)
        try:
            somelike_p.action_performed("bad")
        except Exception:
            assert False

    @pytest.mark.parametrize("t_shell", [Shell.STROMBOLI, Shell.SPINACH,
                                         Shell.WHOLE_GRAIN])
    def test_panel_with_item_provided_correct_shell_combobox(self, t_shell):
        """Correct shell test.

        Verifies that the SomeLikeItHot
        panel correctly sets the shell
        in the combobox.

        Args:
            t_shell: Used to parameterize the test
            for each shell.
        """
        somelike = SomeLikeItHot()
        somelike.shell = t_shell
        master = PrimaryWindow()
        somelike_p = SomeLikeItHotPanel(master, item=somelike)
        assert somelike_p._shell.get() == t_shell

    def test_panel_sets_cheese_according_to_item_provided(self):
        """Correct ingredient test.

        Verifies that the SomeLikeItHot
        panel correctly sets cheese.
        """
        master = PrimaryWindow()
        somelike = SomeLikeItHot()
        somelike_p = SomeLikeItHotPanel(master, item=somelike)
        assert somelike_p._cheese.get()
        somelike.cheese = False
        somelike_p = SomeLikeItHotPanel(master, item=somelike)
        assert not somelike_p._cheese.get()

    def test_panel_sets_chicken_according_to_item_provided(self):
        """Correct ingredient test.

        Verifies that the SomeLikeItHot
        panel correctly sets chicken.
        """
        master = PrimaryWindow()
        somelike = SomeLikeItHot()
        somelike_p = SomeLikeItHotPanel(master, item=somelike)
        assert somelike_p._chicken.get()
        somelike.chicken = False
        somelike_p = SomeLikeItHotPanel(master, item=somelike)
        assert not somelike_p._chicken.get()

    def test_panel_saves_cheese_correctly(self):
        """Correct ingredient test.

        Verifies that the SomeLikeItHot
        panel correctly saves cheese.
        """
        master = PrimaryWindow()
        somelike = SomeLikeItHot()
        somelike_p = SomeLikeItHotPanel(master, item=somelike)
        somelike_p.action_performed("save")
        assert somelike_p._item.cheese
        somelike_p._cheese.set(False)
        somelike_p.action_performed("save")
        assert not somelike_p._item.cheese

    def test_panel_saves_chicken_correctly(self):
        """Correct ingredient test.

        Verifies that the SomeLikeItHot
        panel correctly saves chicken.
        """
        master = PrimaryWindow()
        somelike = SomeLikeItHot()
        somelike_p = SomeLikeItHotPanel(master, item=somelike)
        somelike_p.action_performed("save")
        assert somelike_p._item.chicken
        somelike_p._chicken.set(False)
        somelike_p.action_performed("save")
        assert not somelike_p._item.chicken

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
        somelike = SomeLikeItHot()
        somelike.add_addin(t_addin)
        somelike_p = SomeLikeItHotPanel(master, item=somelike)
        assert somelike_p._addins[t_addin].get()

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
        somelike = SomeLikeItHot()
        somelike.remove_addin(t_addin)
        somelike_p = SomeLikeItHotPanel(master, item=somelike)
        assert not somelike_p._addins[t_addin].get()

    @pytest.mark.parametrize("t_shell", [Shell.STROMBOLI, Shell.SPINACH,
                                         Shell.WHOLE_GRAIN])
    def test_panel_with_item_provided_saves_correct_shell(self, t_shell):
        """Correct shell test.

        Verifies that the SomeLikeItHot
        panel correctly saves the shell.

        Args:
            t_shell: Used to parameterize the test
            for each shell.
        """
        somelike = SomeLikeItHot()
        somelike.shell = t_shell
        master = PrimaryWindow()
        somelike_p = SomeLikeItHotPanel(master, item=somelike)
        somelike_p.action_performed("save")
        assert somelike_p._item.shell == t_shell

    @pytest.mark.parametrize("t_addin", [Addin.PEPPERS, Addin.TOMATOES,
                                         Addin.ONIONS, Addin.PICKLES,
                                         Addin.BUFFALO_SAUCE, Addin.DRESSING,
                                         Addin.MUSTARD])
    def test_addin_checkboxes_save_correctly_true(self, t_addin):
        """Addin checkbox test.

        Verifies that SomeLikeItHot
        panel correctly saves the addins
        (true).

        Args:
            t_addin: Used to parameterize
            for all addins.
        """
        master = PrimaryWindow()
        somelike = SomeLikeItHot()
        somelike.add_addin(t_addin)
        somelike_p = SomeLikeItHotPanel(master, item=somelike)
        somelike_p.action_performed("save")
        assert t_addin in somelike_p._item.addins

    @pytest.mark.parametrize("t_addin", [Addin.PEPPERS, Addin.TOMATOES,
                                         Addin.ONIONS, Addin.PICKLES,
                                         Addin.BUFFALO_SAUCE, Addin.DRESSING,
                                         Addin.MUSTARD])
    def test_addin_checkboxes_save_correctly_false(self, t_addin):
        """Addin checkbox test.

        Verifies that SomeLikeItHot
        panel correctly saves the addins
        (false).

        Args:
            t_addin: Used to parameterize
            for all addins.
        """
        master = PrimaryWindow()
        somelike = SomeLikeItHot()
        somelike.remove_addin(t_addin)
        somelike_p = SomeLikeItHotPanel(master, item=somelike)
        somelike_p.action_performed("save")
        assert t_addin not in somelike_p._item.addins

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
        somelike = SomeLikeItHot()
        somelike_p = SomeLikeItHotPanel(master, item=somelike)
        somelike_p._addins[t_addin].set(False)
        somelike_p._cheese.set(False)
        somelike_p._shell.set(Shell.SPINACH)
        somelike_p.action_performed("cancel")
        assert somelike == somelike_p._item
