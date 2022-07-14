"""The Tests for the The Godfather Panel.

This file contains a number of unit tests
used to verify that the The Godfather panel is
working correctly.

Author: Dustin Hayes djhayes@ksu.edu
Version 0.1
"""
import pytest
from src.thatsawrap.data.enums.Shell import Shell
from src.thatsawrap.data.enums.Addin import Addin
from src.thatsawrap.data.wraps.TheGodFather import TheGodFather
from src.thatsawrap.gui.wraps.TheGodFatherPanel import TheGodFatherPanel
from src.thatsawrap.gui.PrimaryWindow import PrimaryWindow


class TestTheGodFatherPanel:
    """The Godfather panel test class.

    This class contains all of the unit
    tests for the The Godfather Panel.
    """
    def test_new_panel_without_item(self):
        """New Panel test.

        Verifies that a new The Godfather
        panel that is given no arguments
        contains an instance of TheGodFather.
        """
        master = PrimaryWindow()
        god_p = TheGodFatherPanel(master)
        assert isinstance(god_p._item, TheGodFather)

    def test_invalid_action_does_not_throw_exception(self):
        """Invalid action test.

        Verifies that the action_performed
        method does not throw and Exception
        if provided with bad input.
        """
        master = PrimaryWindow()
        god_p = TheGodFatherPanel(master)
        try:
            god_p.action_performed("bad")
        except Exception:
            assert False

    @pytest.mark.parametrize("t_shell", [Shell.STROMBOLI, Shell.SPINACH,
                                         Shell.WHOLE_GRAIN])
    def test_panel_with_item_provided_correct_shell_combobox(self, t_shell):
        """Correct shell test.

        Verifies that the The Godfather
        panel correctly sets the shell
        in the combobox.

        Args:
            t_shell: Used to parameterize the test
            for each shell.
        """
        god = TheGodFather()
        god.shell = t_shell
        master = PrimaryWindow()
        god_p = TheGodFatherPanel(master, item=god)
        assert god_p._shell.get() == t_shell

    def test_panel_sets_pepperoni_according_to_item_provided(self):
        """Correct ingredient test.

        Verifies that the The Godfather
        panel correctly sets pepperoni.
        """
        master = PrimaryWindow()
        god = TheGodFather()
        god.pepperoni = True
        god_p = TheGodFatherPanel(master, item=god)
        assert god_p._pepperoni.get()
        god.pepperoni = False
        god_p = TheGodFatherPanel(master, item=god)
        assert not god_p._pepperoni.get()

    def test_panel_sets_cheese_according_to_item_provided(self):
        """Correct ingredient test.

        Verifies that the The Godfather
        panel correctly sets cheese.
        """
        master = PrimaryWindow()
        god = TheGodFather()
        god_p = TheGodFatherPanel(master, item=god)
        assert god_p._cheese.get()
        god.cheese = False
        god_p = TheGodFatherPanel(master, item=god)
        assert not god_p._cheese.get()

    def test_panel_sets_marinara_according_to_item_provided(self):
        """Correct ingredient test.

        Verifies that the The Godfather
        panel correctly sets marinara.
        """
        master = PrimaryWindow()
        god = TheGodFather()
        god_p = TheGodFatherPanel(master, item=god)
        assert god_p._marinara.get()
        god.marinara = False
        god_p = TheGodFatherPanel(master, item=god)
        assert not god_p._marinara.get()

    def test_panel_sets_sausage_according_to_item_provided(self):
        """Correct ingredient test.

        Verifies that the The Godfather
        panel correctly sets sausage.
        """
        master = PrimaryWindow()
        god = TheGodFather()
        god_p = TheGodFatherPanel(master, item=god)
        assert god_p._sausage.get()
        god.sausage = False
        god_p = TheGodFatherPanel(master, item=god)
        assert not god_p._sausage.get()

    def test_panel_saves_pepperoni_correctly(self):
        """Correct ingredient test.

        Verifies that the The Godfather
        panel correctly saves pepperoni.
        """
        master = PrimaryWindow()
        god = TheGodFather()
        god_p = TheGodFatherPanel(master, item=god)
        god_p.action_performed("save")
        assert god_p._item.pepperoni
        god_p._pepperoni.set(False)
        god_p.action_performed("save")
        assert not god_p._item.pepperoni

    def test_panel_saves_cheese_correctly(self):
        """Correct ingredient test.

        Verifies that the The Godfather
        panel correctly saves cheese.
        """
        master = PrimaryWindow()
        god = TheGodFather()
        god_p = TheGodFatherPanel(master, item=god)
        god_p.action_performed("save")
        assert god_p._item.cheese
        god_p._cheese.set(False)
        god_p.action_performed("save")
        assert not god_p._item.cheese

    def test_panel_saves_marinara_correctly(self):
        """Correct ingredient test.

        Verifies that the The Godfather
        panel correctly saves marinara.
        """
        master = PrimaryWindow()
        god = TheGodFather()
        god_p = TheGodFatherPanel(master, item=god)
        god_p.action_performed("save")
        assert god_p._item.marinara
        god_p._marinara.set(False)
        god_p.action_performed("save")
        assert not god_p._item.marinara

    def test_panel_saves_sausage_correctly(self):
        """Correct ingredient test.

        Verifies that the The Godfather
        panel correctly saves sausage.
        """
        master = PrimaryWindow()
        god = TheGodFather()
        god_p = TheGodFatherPanel(master, item=god)
        god_p.action_performed("save")
        assert god_p._item.sausage
        god_p._sausage.set(False)
        god_p.action_performed("save")
        assert not god_p._item.sausage

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
        god = TheGodFather()
        god.add_addin(t_addin)
        god_p = TheGodFatherPanel(master, item=god)
        assert god_p._addins[t_addin].get()

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
        god = TheGodFather()
        god.remove_addin(t_addin)
        god_p = TheGodFatherPanel(master, item=god)
        assert not god_p._addins[t_addin].get()

    @pytest.mark.parametrize("t_shell", [Shell.STROMBOLI, Shell.SPINACH,
                                         Shell.WHOLE_GRAIN])
    def test_panel_with_item_provided_saves_correct_shell(self, t_shell):
        """Correct shell test.

        Verifies that the The Godfather
        panel correctly saves the shell.

        Args:
            t_shell: Used to parameterize the test
            for each shell.
        """
        god = TheGodFather()
        god.shell = t_shell
        master = PrimaryWindow()
        god_p = TheGodFatherPanel(master, item=god)
        god_p.action_performed("save")
        assert god_p._item.shell == t_shell

    @pytest.mark.parametrize("t_addin", [Addin.PEPPERS, Addin.TOMATOES,
                                         Addin.ONIONS, Addin.PICKLES,
                                         Addin.BUFFALO_SAUCE, Addin.DRESSING,
                                         Addin.MUSTARD])
    def test_addin_checkboxes_save_correctly_true(self, t_addin):
        """Addin checkbox test.

        Verifies that the Godfather
        panel correctly saves the addins
        (true).

        Args:
            t_addin: Used to parameterize
            for all addins.
        """
        master = PrimaryWindow()
        god = TheGodFather()
        god.add_addin(t_addin)
        god_p = TheGodFatherPanel(master, item=god)
        god_p.action_performed("save")
        assert t_addin in god_p._item.addins

    @pytest.mark.parametrize("t_addin", [Addin.PEPPERS, Addin.TOMATOES,
                                         Addin.ONIONS, Addin.PICKLES,
                                         Addin.BUFFALO_SAUCE, Addin.DRESSING,
                                         Addin.MUSTARD])
    def test_addin_checkboxes_save_correctly_false(self, t_addin):
        """Addin checkbox test.

        Verifies that the Godfather
        panel correctly saves the addins
        (false).

        Args:
            t_addin: Used to parameterize
            for all addins.
        """
        master = PrimaryWindow()
        god = TheGodFather()
        god.remove_addin(t_addin)
        god_p = TheGodFatherPanel(master, item=god)
        god_p.action_performed("save")
        assert t_addin not in god_p._item.addins

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
        god = TheGodFather()
        god_p = TheGodFatherPanel(master, item=god)
        god_p._addins[t_addin].set(False)
        god_p._cheese.set(False)
        god_p._shell.set(Shell.SPINACH)
        god_p.action_performed("cancel")
        assert god == god_p._item
