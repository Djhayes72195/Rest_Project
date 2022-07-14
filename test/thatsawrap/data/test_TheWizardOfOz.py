from src.thatsawrap.data.enums.Shell import Shell
from src.thatsawrap.data.enums.Addin import Addin
import pytest
from src.thatsawrap.data.wraps.WestSideStory import WestSideStory
from src.thatsawrap.data.wraps.TheWizardOfOz import TheWizardOfOz
from src.thatsawrap.data.wraps.Wrap import Wrap
from src.thatsawrap.data.menu.Item import Item


t_calories = 1085
t_base_price = 10.10


class TestTheWizardOfOz:

    def test_new_object_instructions_list_should_be_default(self):
        wiz = TheWizardOfOz()
        assert len(wiz.instructions) == 2

    def test_new_object_should_have_correct_shell(self):
        wiz = TheWizardOfOz()
        assert wiz.shell == Shell.SPINACH

    def test_new_object_addins_are_default(self):
        wiz = TheWizardOfOz()
        assert wiz.addins == {Addin.TOMATOES, Addin.DRESSING}

    def test_calories_are_correct(self):
        wiz = TheWizardOfOz()
        assert wiz.calories == t_calories

    @pytest.mark.parametrize("t_shell, t_price", [
        (Shell.STROMBOLI, t_base_price + .75),
        (Shell.WHOLE_GRAIN, t_base_price),
        (Shell.SPINACH, t_base_price + .25)])
    def test_price_for_each_shell_is_correct(self, t_shell, t_price):
        wiz = TheWizardOfOz()
        wiz.shell = t_shell
        assert wiz.price == t_price

    @pytest.mark.parametrize("t_shell, t_string", [
        (Shell.STROMBOLI, "The Wizard Of Oz in a Stromboli Shell"),
        (Shell.WHOLE_GRAIN, "The Wizard Of Oz in a Whole Grain Shell"),
        (Shell.SPINACH, "The Wizard Of Oz in a Spinach Shell")])
    def test_string_for_each_shell_is_correct(self, t_shell, t_string):
        wiz = TheWizardOfOz()
        wiz.shell = t_shell
        assert str(wiz) == t_string

    def test_chicken_included_by_default(self):
        wiz = TheWizardOfOz()
        assert wiz.chicken

    def test_cheese_included_by_default(self):
        wiz = TheWizardOfOz()
        assert wiz.cheese

    def test_spinach_included_by_default(self):
        wiz = TheWizardOfOz()
        assert wiz.spinach

    def test_changing_an_ingredient_should_change_instructions(self):
        wiz = TheWizardOfOz()
        wiz.chicken = False
        assert len(wiz.instructions) == 3
        wiz.cheese = False
        assert len(wiz.instructions) == 4
        wiz.cheese = True
        assert len(wiz.instructions) == 3
        wiz.spinach = False
        assert len(wiz.instructions) == 4

    @pytest.mark.parametrize("t_addin", [Addin.TOMATOES, Addin.DRESSING])
    def test_addins_included_by_default(self, t_addin):
        wiz = TheWizardOfOz()
        assert t_addin in wiz.addins

    @pytest.mark.parametrize("t_addin_removed", [Addin.PEPPERS, Addin.TOMATOES,
                                                 Addin.ONIONS, Addin.PICKLES,
                                                 Addin.BUFFALO_SAUCE,
                                                 Addin.DRESSING, Addin.MUSTARD])
    def test_modifying_addins_modifies_addin_list(self, t_addin_removed):
        wiz = TheWizardOfOz()
        if t_addin_removed in wiz.addins:
            wiz.remove_addin(t_addin_removed)
            assert t_addin_removed not in wiz.addins
            wiz.add_addin(t_addin_removed)
            assert t_addin_removed in wiz.addins
        else:
            wiz.add_addin(t_addin_removed)
            assert t_addin_removed in wiz.addins

    def test_two_instances_of_same_object_are_equal(self):
        wiz = TheWizardOfOz()
        wiz2 = TheWizardOfOz()
        assert wiz == wiz2

    def test_two_objects_with_different_shells_are_not_equal(self):
        wiz = TheWizardOfOz()
        wiz2 = TheWizardOfOz()
        wiz2.shell = Shell.STROMBOLI
        assert wiz != wiz2
        wiz2.shell = Shell.WHOLE_GRAIN
        assert wiz != wiz2

    def test_two_objects_with_different_ingredients_are_not_equal(self):
        wiz = TheWizardOfOz()
        wiz2 = TheWizardOfOz()
        wiz2.cheese = False
        assert wiz != wiz2
        wiz2.cheese = True
        wiz2.chicken = False
        assert wiz != wiz2
        wiz2.chicken = True
        wiz2.spinach = False
        assert wiz != wiz2

    @pytest.mark.parametrize("t_addin_change", [Addin.PEPPERS, Addin.TOMATOES,
                                                Addin.ONIONS, Addin.PICKLES,
                                                Addin.BUFFALO_SAUCE,
                                                Addin.DRESSING, Addin.MUSTARD])
    def test_two_objects_with_different_addins_are_not_equal(self, t_addin_change):
        wiz = TheWizardOfOz()
        if t_addin_change in wiz.addins:
            wiz.remove_addin(t_addin_change)
            wiz2 = TheWizardOfOz()
            assert wiz != wiz2
        else:
            wiz.add_addin(t_addin_change)
            wiz2 = TheWizardOfOz()
            assert wiz != wiz2

    def test_two_different_objects_are_not_equal(self):
        wiz = TheWizardOfOz()
        west = WestSideStory()
        assert wiz != west

    def test_new_object_has_entries_for_addins(self):
        wiz = TheWizardOfOz()
        assert "Add Tomatoes", "Add Dressing" in wiz.instructions

    def test_inheritance_from_base_class(self):
        wiz = TheWizardOfOz()
        assert isinstance(wiz, Wrap)

    def test_implements_Item_interface(self):
        wiz = TheWizardOfOz()
        assert isinstance(wiz, Item)

    @pytest.mark.parametrize("t_addin_modified", [Addin.PEPPERS, Addin.TOMATOES,
                                                  Addin.ONIONS, Addin.PICKLES,
                                                  Addin.BUFFALO_SAUCE,
                                                  Addin.DRESSING, Addin.MUSTARD])
    def test_modifying_addins_modifies_instructions(self, t_addin_modified):
        wiz = TheWizardOfOz()
        wiz.add_addin(t_addin_modified)
        assert "Add {}".format(t_addin_modified) in wiz.instructions
        wiz.remove_addin(t_addin_modified)
        assert "Add {}".format(t_addin_modified) not in wiz.instructions

    def test_name_is_correct(self):
        wiz = TheWizardOfOz()
        assert wiz.name == "The Wizard of Oz"
