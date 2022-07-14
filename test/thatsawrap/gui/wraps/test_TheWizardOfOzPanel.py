"""The Tests for the TheWizardOfOz Panel.

This file contains a number of unit tests
used to verify that the TheWizardOfOz panel is
working correctly.

Author: Dustin Hayes djhayes@ksu.edu
Version 0.1
"""
import pytest
from src.thatsawrap.data.enums.Shell import Shell
from src.thatsawrap.data.enums.Addin import Addin
from src.thatsawrap.data.wraps.TheWizardOfOz import TheWizardOfOz
from src.thatsawrap.gui.wraps.TheWizardOfOzPanel import TheWizardOfOzPanel
from src.thatsawrap.gui.PrimaryWindow import PrimaryWindow


class TestTheWizardOfOzPanel:
    """TheWizardOfOz panel test class.

    This class contains all of the unit
    tests for the TheWizardOfOz Panel.
    """
    def test_new_panel_without_item(self):
        """New Panel test.

        Verifies that a new TheWizardOfOz
        panel that is given no arguments
        contains an instance of TheWizardOfOz.
        """
        master = PrimaryWindow()
        wizzy_p = TheWizardOfOzPanel(master)
        assert isinstance(wizzy_p._item, TheWizardOfOz)

    def test_invalid_action_does_not_throw_exception(self):
        """Invalid action test.

        Verifies that the action_performed
        method does not throw and Exception
        if provided with bad input.
        """
        master = PrimaryWindow()
        wizzy_p = TheWizardOfOzPanel(master)
        try:
            wizzy_p.action_performed("bad")
        except Exception:
            assert False

    @pytest.mark.parametrize("t_shell", [Shell.STROMBOLI, Shell.SPINACH,
                                         Shell.WHOLE_GRAIN])
    def test_panel_with_item_provided_correct_shell_combobox(self, t_shell):
        """Correct shell test.

        Verifies that the TheWizardOfOz
        panel correctly sets the shell
        in the combobox.

        Args:
            t_shell: Used to parameterize the test
            for each shell.
        """
        wizzy = TheWizardOfOz()
        wizzy.shell = t_shell
        master = PrimaryWindow()
        wizzy_p = TheWizardOfOzPanel(master, item=wizzy)
        assert wizzy_p._shell.get() == t_shell

    def test_panel_sets_cheese_according_to_item_provided(self):
        """Correct ingredient test.

        Verifies that the TheWizardOfOz
        panel correctly sets cheese.
        """
        master = PrimaryWindow()
        wizzy = TheWizardOfOz()
        wizzy_p = TheWizardOfOzPanel(master, item=wizzy)
        assert wizzy_p._cheese.get()
        wizzy.cheese = False
        wizzy_p = TheWizardOfOzPanel(master, item=wizzy)
        assert not wizzy_p._cheese.get()

    def test_panel_sets_spinach_according_to_item_provided(self):
        """Correct ingredient test.

        Verifies that the TheWizardOfOz
        panel correctly sets spinach.
        """
        master = PrimaryWindow()
        wizzy = TheWizardOfOz()
        wizzy_p = TheWizardOfOzPanel(master, item=wizzy)
        assert wizzy_p._spinach.get()
        wizzy.spinach = False
        wizzy_p = TheWizardOfOzPanel(master, item=wizzy)
        assert not wizzy_p._spinach.get()

    def test_panel_sets_chicken_according_to_item_provided(self):
        """Correct ingredient test.

        Verifies that the TheWizardOfOz
        panel correctly sets chicken.
        """
        master = PrimaryWindow()
        wizzy = TheWizardOfOz()
        wizzy_p = TheWizardOfOzPanel(master, item=wizzy)
        assert wizzy_p._chicken.get()
        wizzy.chicken = False
        wizzy_p = TheWizardOfOzPanel(master, item=wizzy)
        assert not wizzy_p._chicken.get()

    def test_panel_saves_cheese_correctly(self):
        """Correct ingredient test.

        Verifies that the TheWizardOfOz
        panel correctly saves cheese.
        """
        master = PrimaryWindow()
        wizzy = TheWizardOfOz()
        wizzy_p = TheWizardOfOzPanel(master, item=wizzy)
        wizzy_p.action_performed("save")
        assert wizzy_p._item.cheese
        wizzy_p._cheese.set(False)
        wizzy_p.action_performed("save")
        assert not wizzy_p._item.cheese

    def test_panel_saves_chicken_correctly(self):
        """Correct ingredient test.

        Verifies that the TheWizardOfOz
        panel correctly saves chicken.
        """
        master = PrimaryWindow()
        wizzy = TheWizardOfOz()
        wizzy_p = TheWizardOfOzPanel(master, item=wizzy)
        wizzy_p.action_performed("save")
        assert wizzy_p._item.chicken
        wizzy_p._chicken.set(False)
        wizzy_p.action_performed("save")
        assert not wizzy_p._item.chicken

    def test_panel_saves_spinach_correctly(self):
        """Correct ingredient test.

        Verifies that the TheWizardOfOz
        panel correctly saves spinach.
        """
        master = PrimaryWindow()
        wizzy = TheWizardOfOz()
        wizzy_p = TheWizardOfOzPanel(master, item=wizzy)
        wizzy_p.action_performed("save")
        assert wizzy_p._item.spinach
        wizzy_p._spinach.set(False)
        wizzy_p.action_performed("save")
        assert not wizzy_p._item.spinach

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
        wizzy = TheWizardOfOz()
        wizzy.add_addin(t_addin)
        wizzy_p = TheWizardOfOzPanel(master, item=wizzy)
        assert wizzy_p._addins[t_addin].get()

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
        wizzy = TheWizardOfOz()
        wizzy.remove_addin(t_addin)
        wizzy_p = TheWizardOfOzPanel(master, item=wizzy)
        assert not wizzy_p._addins[t_addin].get()

    @pytest.mark.parametrize("t_shell", [Shell.STROMBOLI, Shell.SPINACH,
                                         Shell.WHOLE_GRAIN])
    def test_panel_with_item_provided_saves_correct_shell(self, t_shell):
        """Correct shell test.

        Verifies that the TheWizardOfOz
        panel correctly saves the shell.

        Args:
            t_shell: Used to parameterize the test
            for each shell.
        """
        wizzy = TheWizardOfOz()
        wizzy.shell = t_shell
        master = PrimaryWindow()
        wizzy_p = TheWizardOfOzPanel(master, item=wizzy)
        wizzy_p.action_performed("save")
        assert wizzy_p._item.shell == t_shell

    @pytest.mark.parametrize("t_addin", [Addin.PEPPERS, Addin.TOMATOES,
                                         Addin.ONIONS, Addin.PICKLES,
                                         Addin.BUFFALO_SAUCE, Addin.DRESSING,
                                         Addin.MUSTARD])
    def test_addin_checkboxes_correctly_true(self, t_addin):
        """Addin checkbox test.

        Verifies that TheWizardOfOz
        panel correctly saves the addins
        (true).

        Args:
            t_addin: Used to parameterize
            for all addins.
        """
        master = PrimaryWindow()
        wizzy = TheWizardOfOz()
        wizzy.add_addin(t_addin)
        wizzy_p = TheWizardOfOzPanel(master, item=wizzy)
        wizzy_p.action_performed("save")
        assert t_addin in wizzy_p._item.addins

    @pytest.mark.parametrize("t_addin", [Addin.PEPPERS, Addin.TOMATOES,
                                         Addin.ONIONS, Addin.PICKLES,
                                         Addin.BUFFALO_SAUCE, Addin.DRESSING,
                                         Addin.MUSTARD])
    def test_addin_checkboxes_correctly_false(self, t_addin):
        """Addin checkbox test.

        Verifies that TheWizardOfOz
        panel correctly saves the addins
        (false).

        Args:
            t_addin: Used to parameterize
            for all addins.
        """
        master = PrimaryWindow()
        wizzy = TheWizardOfOz()
        wizzy.remove_addin(t_addin)
        wizzy_p = TheWizardOfOzPanel(master, item=wizzy)
        wizzy_p.action_performed("save")
        assert t_addin not in wizzy_p._item.addins

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
        wizzy = TheWizardOfOz()
        wizzy_p = TheWizardOfOzPanel(master, item=wizzy)
        wizzy_p._addins[t_addin].set(False)
        wizzy_p._cheese.set(False)
        wizzy_p._shell.set(Shell.WHOLE_GRAIN)
        wizzy_p.action_performed("cancel")
        assert wizzy == wizzy_p._item
