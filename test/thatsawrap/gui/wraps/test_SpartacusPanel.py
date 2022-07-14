"""The Tests for the Spartacus Panel.

This file contains a number of unit tests
used to verify that the Spartacus panel is
working correctly.

Author: Dustin Hayes djhayes@ksu.edu
Version 0.1
"""
import pytest
from src.thatsawrap.data.enums.Shell import Shell
from src.thatsawrap.data.enums.Addin import Addin
from src.thatsawrap.data.wraps.Spartacus import Spartacus
from src.thatsawrap.gui.wraps.SpartacusPanel import SpartacusPanel
from src.thatsawrap.gui.PrimaryWindow import PrimaryWindow


class TestSpartacusPanel:
    """Spartacus panel test class.

    This class contains all of the unit
    tests for the Spartacus Panel.
    """
    def test_new_panel_without_item(self):
        """New Panel test.

        Verifies that a new Spartacus
        panel that is given no arguments
        contains an instance of Spartacus.
        """
        master = PrimaryWindow()
        spart_p = SpartacusPanel(master)
        assert isinstance(spart_p._item, Spartacus)

    def test_invalid_action_does_not_throw_exception(self):
        """Invalid action test.

        Verifies that the action_performed
        method does not throw and Exception
        if provided with bad input.
        """
        master = PrimaryWindow()
        spart_p = SpartacusPanel(master)
        try:
            spart_p.action_performed("bad")
        except Exception:
            assert False

    @pytest.mark.parametrize("t_shell", [Shell.STROMBOLI, Shell.SPINACH,
                                         Shell.WHOLE_GRAIN])
    def test_panel_with_item_provided_correct_shell_combobox(self, t_shell):
        """Correct shell test.

        Verifies that the Spartacus
        panel correctly sets the shell
        in the combobox.

        Args:
            t_shell: Used to parameterize the test
            for each shell.
        """
        spart = Spartacus()
        spart.shell = t_shell
        master = PrimaryWindow()
        spart_p = SpartacusPanel(master, item=spart)
        assert spart_p._shell.get() == t_shell

    def test_panel_sets_pepperoni_according_to_item_provided(self):
        """Correct ingredient test.

        Verifies that the Spartacus
        panel correctly sets pepperoni.
        """
        master = PrimaryWindow()
        spart = Spartacus()
        spart.pepperoni = True
        spart_p = SpartacusPanel(master, item=spart)
        assert spart_p._pepperoni.get()
        spart.pepperoni = False
        spart_p = SpartacusPanel(master, item=spart)
        assert not spart_p._pepperoni.get()

    def test_panel_sets_cheese_according_to_item_provided(self):
        """Correct ingredient test.

        Verifies that the Spartacus
        panel correctly sets cheese.
        """
        master = PrimaryWindow()
        spart = Spartacus()
        spart_p = SpartacusPanel(master, item=spart)
        assert spart_p._cheese.get()
        spart.cheese = False
        spart_p = SpartacusPanel(master, item=spart)
        assert not spart_p._cheese.get()

    def test_panel_sets_chicken_according_to_item_provided(self):
        """Correct ingredient test.

        Verifies that the Spartacus
        panel correctly sets chicken.
        """
        master = PrimaryWindow()
        spart = Spartacus()
        spart_p = SpartacusPanel(master, item=spart)
        assert spart_p._chicken.get()
        spart.chicken = False
        spart_p = SpartacusPanel(master, item=spart)
        assert not spart_p._chicken.get()

    def test_panel_sets_corned_beef_according_to_item_provided(self):
        """Correct ingredient test.

        Verifies that the Spartacus
        panel correctly sets corned
        beef.
        """
        master = PrimaryWindow()
        spart = Spartacus()
        spart_p = SpartacusPanel(master, item=spart)
        assert spart_p._corned_beef.get()
        spart.corned_beef = False
        spart_p = SpartacusPanel(master, item=spart)
        assert not spart_p._corned_beef.get()

    def test_panel_sets_sausage_according_to_item_provided(self):
        """Correct ingredient test.

        Verifies that the Spartacus
        panel correctly sets sausage.
        """
        master = PrimaryWindow()
        spart = Spartacus()
        spart_p = SpartacusPanel(master, item=spart)
        assert spart_p._sausage.get()
        spart.sausage = False
        spart_p = SpartacusPanel(master, item=spart)
        assert not spart_p._sausage.get()

    def test_panel_saves_pepperoni_correctly(self):
        """Correct ingredient test.

        Verifies that the Spartacus
        panel correctly saves pepperoni.
        """
        master = PrimaryWindow()
        spart = Spartacus()
        spart_p = SpartacusPanel(master, item=spart)
        spart_p.action_performed("save")
        assert spart_p._item.pepperoni
        spart_p._pepperoni.set(False)
        spart_p.action_performed("save")
        assert not spart_p._item.pepperoni

    def test_panel_saves_cheese_correctly(self):
        """Correct ingredient test.

        Verifies that the Spartacus
        panel correctly saves cheese.
        """
        master = PrimaryWindow()
        spart = Spartacus()
        spart_p = SpartacusPanel(master, item=spart)
        spart_p.action_performed("save")
        assert spart_p._item.cheese
        spart_p._cheese.set(False)
        spart_p.action_performed("save")
        assert not spart_p._item.cheese

    def test_panel_saves_corned_beef_correctly(self):
        """Correct ingredient test.

        Verifies that the Spartacus
        panel correctly saves marinara.
        """
        master = PrimaryWindow()
        spart = Spartacus()
        spart_p = SpartacusPanel(master, item=spart)
        spart_p.action_performed("save")
        assert spart_p._item.corned_beef
        spart_p._corned_beef.set(False)
        spart_p.action_performed("save")
        assert not spart_p._item.corned_beef

    def test_panel_saves_sausage_correctly(self):
        """Correct ingredient test.

        Verifies that the Spartacus
        panel correctly saves sausage.
        """
        master = PrimaryWindow()
        spart = Spartacus()
        spart_p = SpartacusPanel(master, item=spart)
        spart_p.action_performed("save")
        assert spart_p._item.sausage
        spart_p._sausage.set(False)
        spart_p.action_performed("save")
        assert not spart_p._item.sausage

    def test_panel_saves_chicken_correctly(self):
        """Correct ingredient test.

        Verifies that the Spartacus
        panel correctly saves chicken.
        """
        master = PrimaryWindow()
        spart = Spartacus()
        spart_p = SpartacusPanel(master, item=spart)
        spart_p.action_performed("save")
        assert spart_p._item.chicken
        spart_p._chicken.set(False)
        spart_p.action_performed("save")
        assert not spart_p._item.chicken

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
        spart = Spartacus()
        spart.add_addin(t_addin)
        spart_p = SpartacusPanel(master, item=spart)
        assert spart_p._addins[t_addin].get()

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
        spart = Spartacus()
        spart.remove_addin(t_addin)
        spart_p = SpartacusPanel(master, item=spart)
        assert not spart_p._addins[t_addin].get()

    @pytest.mark.parametrize("t_shell", [Shell.STROMBOLI, Shell.SPINACH,
                                         Shell.WHOLE_GRAIN])
    def test_panel_with_item_provided_saves_correct_shell(self, t_shell):
        """Correct shell test.

        Verifies that the Spartacus
        panel correctly saves the shell.

        Args:
            t_shell: Used to parameterize the test
            for each shell.
        """
        spart = Spartacus()
        spart.shell = t_shell
        master = PrimaryWindow()
        spart_p = SpartacusPanel(master, item=spart)
        spart_p.action_performed("save")
        assert spart_p._item.shell == t_shell

    @pytest.mark.parametrize("t_addin", [Addin.PEPPERS, Addin.TOMATOES,
                                         Addin.ONIONS, Addin.PICKLES,
                                         Addin.BUFFALO_SAUCE, Addin.DRESSING,
                                         Addin.MUSTARD])
    def test_addin_checkboxes_saves_correctly_true(self, t_addin):
        """Addin checkbox test.

        Verifies that Spartacus
        panel correctly saves the addins
        (true).

        Args:
            t_addin: Used to parameterize
            for all addins.
        """
        master = PrimaryWindow()
        spart = Spartacus()
        spart.add_addin(t_addin)
        spart_p = SpartacusPanel(master, item=spart)
        spart_p.action_performed("save")
        assert t_addin in spart_p._item.addins

    @pytest.mark.parametrize("t_addin", [Addin.PEPPERS, Addin.TOMATOES,
                                         Addin.ONIONS, Addin.PICKLES,
                                         Addin.BUFFALO_SAUCE, Addin.DRESSING,
                                         Addin.MUSTARD])
    def test_addin_checkboxes_saves_correctly_false(self, t_addin):
        """Addin checkbox test.

        Verifies that Spartacus
        panel correctly saves the addins
        (false).

        Args:
            t_addin: Used to parameterize
            for all addins.
        """
        master = PrimaryWindow()
        spart = Spartacus()
        spart.remove_addin(t_addin)
        spart_p = SpartacusPanel(master, item=spart)
        spart_p.action_performed("save")
        assert t_addin not in spart_p._item.addins

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
        spart = Spartacus()
        spart_p = SpartacusPanel(master, item=spart)
        spart_p._addins[t_addin].set(False)
        spart_p._cheese.set(False)
        spart_p._shell.set(Shell.SPINACH)
        spart_p.action_performed("cancel")
        assert spart == spart_p._item
