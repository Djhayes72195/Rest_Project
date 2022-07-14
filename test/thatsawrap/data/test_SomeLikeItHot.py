from src.thatsawrap.data.enums.Shell import Shell
from src.thatsawrap.data.enums.Addin import Addin
import pytest
from src.thatsawrap.data.wraps.SomeLikeItHot import SomeLikeItHot
from src.thatsawrap.data.wraps.TheWizardOfOz import TheWizardOfOz
from src.thatsawrap.data.wraps.Wrap import Wrap
from src.thatsawrap.data.menu.Item import Item


t_calories = 1370
t_base_price = 11.45


class TestSomeLikeItHot:

    def test_new_object_instructions_list_should_be_default(self):
        some = SomeLikeItHot()
        assert len(some.instructions) == 3

    def test_new_object_should_have_correct_shell(self):
        some = SomeLikeItHot()
        assert some.shell == Shell.WHOLE_GRAIN

    def test_new_object_addins_are_default(self):
        some = SomeLikeItHot()
        assert some.addins == {Addin.ONIONS, Addin.PEPPERS, Addin.BUFFALO_SAUCE}

    def test_calories_are_correct(self):
        some = SomeLikeItHot()
        assert some.calories == t_calories

    @pytest.mark.parametrize("t_shell, t_price", [
        (Shell.STROMBOLI, t_base_price + .75),
        (Shell.WHOLE_GRAIN, t_base_price),
        (Shell.SPINACH, t_base_price + .25)])
    def test_price_for_each_shell_is_correct(self, t_shell, t_price):
        some = SomeLikeItHot()
        some.shell = t_shell
        assert some.price == t_price

    @pytest.mark.parametrize("t_shell, t_string", [
        (Shell.STROMBOLI, "Some Like It Hot in a Stromboli Shell"),
        (Shell.WHOLE_GRAIN, "Some Like It Hot in a Whole Grain Shell"),
        (Shell.SPINACH, "Some Like It Hot in a Spinach Shell")])
    def test_string_for_each_shell_is_correct(self, t_shell, t_string):
        some = SomeLikeItHot()
        some.shell = t_shell
        assert str(some) == t_string

    def test_chicken_included_by_default(self):
        some = SomeLikeItHot()
        assert some.chicken

    def test_cheese_included_by_default(self):
        some = SomeLikeItHot()
        assert some.cheese

    def test_changing_an_ingredient_should_change_instructions(self):
        some = SomeLikeItHot()
        some.chicken = False
        assert len(some.instructions) == 4
        some.cheese = False
        assert len(some.instructions) == 5
        some.cheese = True
        assert len(some.instructions) == 4

    @pytest.mark.parametrize("t_addin", [Addin.PEPPERS, Addin.ONIONS,
                                         Addin.BUFFALO_SAUCE])
    def test_addins_included_by_default(self, t_addin):
        some = SomeLikeItHot()
        assert t_addin in some.addins

    @pytest.mark.parametrize("t_addin_removed", [Addin.PEPPERS, Addin.TOMATOES,
                                                 Addin.ONIONS, Addin.PICKLES,
                                                 Addin.BUFFALO_SAUCE,
                                                 Addin.DRESSING, Addin.MUSTARD])
    def test_modifying_addins_modifies_addin_list(self, t_addin_removed):
        some = SomeLikeItHot()
        if t_addin_removed in some.addins:
            some.remove_addin(t_addin_removed)
            assert t_addin_removed not in some.addins
            some.add_addin(t_addin_removed)
            assert t_addin_removed in some.addins
        else:
            some.add_addin(t_addin_removed)
            assert t_addin_removed in some.addins

    def test_two_instances_of_same_object_are_equal(self):
        some = SomeLikeItHot()
        some2 = SomeLikeItHot()
        assert some == some2

    def test_two_objects_with_different_shells_are_not_equal(self):
        some = SomeLikeItHot()
        some2 = SomeLikeItHot()
        some2.shell = Shell.STROMBOLI
        assert some != some2
        some2.shell = Shell.SPINACH
        assert some != some2

    def test_two_objects_with_different_ingredients_are_not_equal(self):
        some = SomeLikeItHot()
        some2 = SomeLikeItHot()
        some2.cheese = False
        assert some != some2
        some2.cheese = True
        some2.chicken = False
        assert some != some2

    @pytest.mark.parametrize("t_addin_change", [Addin.PEPPERS, Addin.TOMATOES,
                                                Addin.ONIONS, Addin.PICKLES,
                                                Addin.BUFFALO_SAUCE,
                                                Addin.DRESSING, Addin.MUSTARD])
    def test_two_objects_with_different_addins_are_not_equal(self, t_addin_change):
        some = SomeLikeItHot()
        if t_addin_change in some.addins:
            some.remove_addin(t_addin_change)
            some2 = SomeLikeItHot()
            assert some != some2
        else:
            some.add_addin(t_addin_change)
            some2 = SomeLikeItHot()
            assert some != some2

    def test_two_different_objects_are_not_equal(self):
        some = SomeLikeItHot()
        wiz = TheWizardOfOz()
        assert some != wiz

    def test_new_object_has_entries_for_addins(self):
        some = SomeLikeItHot()
        assert ["Add Onions", "Add Peppers",
                "Add Buffalo Sauce" in some.instructions]

    def test_inheritance_from_base_class(self):
        some = SomeLikeItHot()
        assert isinstance(some, Wrap)

    def test_implements_Item_interface(self):
        some = SomeLikeItHot()
        assert isinstance(some, Item)

    @pytest.mark.parametrize("t_addin_modified", [Addin.PEPPERS, Addin.TOMATOES,
                                                  Addin.ONIONS, Addin.PICKLES,
                                                  Addin.BUFFALO_SAUCE,
                                                  Addin.DRESSING, Addin.MUSTARD])
    def test_modifying_addins_modifies_instructions(self, t_addin_modified):
        some = SomeLikeItHot()
        some.add_addin(t_addin_modified)
        assert "Add {}".format(t_addin_modified) in some.instructions
        some.remove_addin(t_addin_modified)
        assert "Add {}".format(t_addin_modified) not in some.instructions

    def test_name_is_correct(self):
        some = SomeLikeItHot()
        assert some.name == "Some Like it Hot"
