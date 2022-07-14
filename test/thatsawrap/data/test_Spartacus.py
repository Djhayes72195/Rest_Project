from src.thatsawrap.data.enums.Shell import Shell
from src.thatsawrap.data.enums.Addin import Addin
import pytest
from src.thatsawrap.data.wraps.Spartacus import Spartacus
from src.thatsawrap.data.wraps.TheGodFather import TheGodFather
from src.thatsawrap.data.wraps.Wrap import Wrap
from src.thatsawrap.data.menu.Item import Item


t_calories = 1874
t_base_price = 16.30


class TestSpartacus:

    def test_new_object_instructions_list_should_be_default(self):
        spart = Spartacus()
        assert len(spart.instructions) == 6

    def test_new_object_should_have_correct_shell(self):
        spart = Spartacus()
        assert spart.shell == Shell.SPINACH

    def test_new_object_addins_are_default(self):
        spart = Spartacus()
        assert spart.addins == {Addin.ONIONS, Addin.PEPPERS,
                                Addin.TOMATOES, Addin.PICKLES,
                                Addin.BUFFALO_SAUCE, Addin.DRESSING}

    def test_calories_are_correct(self):
        spart = Spartacus()
        assert spart.calories == t_calories

    @pytest.mark.parametrize("t_shell, t_price", [
        (Shell.STROMBOLI, t_base_price + .75),
        (Shell.WHOLE_GRAIN, t_base_price),
        (Shell.SPINACH, t_base_price + .25)])
    def test_price_for_each_shell_is_correct(self, t_shell, t_price):
        spart = Spartacus()
        spart.shell = t_shell
        assert spart.price == t_price

    @pytest.mark.parametrize("t_shell, t_string", [
        (Shell.STROMBOLI, "Spartacus in a Stromboli Shell"),
        (Shell.WHOLE_GRAIN, "Spartacus in a Whole Grain Shell"),
        (Shell.SPINACH, "Spartacus in a Spinach Shell")])
    def test_string_for_each_shell_is_correct(self, t_shell, t_string):
        spart = Spartacus()
        spart.shell = t_shell
        assert str(spart) == t_string

    def test_chicken_included_by_default(self):
        spart = Spartacus()
        assert spart.chicken

    def test_cheese_included_by_default(self):
        spart = Spartacus()
        assert spart.cheese

    def test_corned_beef_included_by_default(self):
        spart = Spartacus()
        assert spart.corned_beef

    def test_sausage_included_by_default(self):
        spart = Spartacus()
        assert spart.sausage

    def test_pepperoni_included_by_default(self):
        spart = Spartacus()
        assert spart.pepperoni

    def test_changing_an_ingredient_should_change_instructions(self):
        spart = Spartacus()
        spart.chicken = False
        assert len(spart.instructions) == 7
        spart.cheese = False
        assert len(spart.instructions) == 8
        spart.corned_beef = False
        assert len(spart.instructions) == 9
        spart.sausage = False
        assert len(spart.instructions) == 10
        spart.pepperoni = False
        assert len(spart.instructions) == 11
        spart.chicken = True
        assert len(spart.instructions) == 10

    @pytest.mark.parametrize("t_addin", [Addin.PEPPERS, Addin.TOMATOES,
                                         Addin.ONIONS, Addin.PICKLES,
                                         Addin.BUFFALO_SAUCE, Addin.DRESSING])
    def test_addins_included_by_default(self, t_addin):
        spart = Spartacus()
        assert t_addin in spart.addins

    @pytest.mark.parametrize("t_addin_removed", [Addin.PEPPERS, Addin.TOMATOES,
                                                 Addin.ONIONS, Addin.PICKLES,
                                                 Addin.BUFFALO_SAUCE,
                                                 Addin.DRESSING,
                                                 Addin.MUSTARD])
    def test_modifying_addins_modifies_addin_list(self, t_addin_removed):
        spart = Spartacus()
        if t_addin_removed in spart.addins:
            spart.remove_addin(t_addin_removed)
            assert t_addin_removed not in spart.addins
            spart.add_addin(t_addin_removed)
            assert t_addin_removed in spart.addins
        else:
            spart.add_addin(t_addin_removed)
            assert t_addin_removed in spart.addins

    def test_two_instances_of_same_object_are_equal(self):
        spart = Spartacus()
        spart2 = Spartacus()
        assert spart == spart2

    def test_two_objects_with_different_shells_are_not_equal(self):
        spart = Spartacus()
        spart2 = Spartacus()
        spart2.shell = Shell.STROMBOLI
        assert spart != spart2
        spart2.shell = Shell.WHOLE_GRAIN
        assert spart != spart2

    def test_two_objects_with_different_ingredients_are_not_equal(self):
        spart = Spartacus()
        spart2 = Spartacus()
        spart2.cheese = False
        assert spart != spart2
        spart2.cheese = True
        spart2.chicken = False
        assert spart != spart2
        spart2.chicken = True
        spart2.pepperoni = False
        assert spart != spart2
        spart2.pepperoni = True
        spart2.sausage = False
        assert spart != spart2
        spart2.sausage = True
        spart2.corned_beef = False
        assert spart != spart2

    @pytest.mark.parametrize("t_addin_change", [Addin.PEPPERS, Addin.TOMATOES,
                                                Addin.ONIONS, Addin.PICKLES,
                                                Addin.BUFFALO_SAUCE,
                                                Addin.DRESSING, Addin.MUSTARD])
    def test_two_objects_different_addins_not_equal(self, t_addin_change):
        spart = Spartacus()
        if t_addin_change in spart.addins:
            spart.remove_addin(t_addin_change)
            spart2 = Spartacus()
            assert spart != spart2
        else:
            spart.add_addin(t_addin_change)
            spart2 = Spartacus()
            assert spart != spart2

    def test_two_different_objects_are_not_equal(self):
        spart = Spartacus()
        god = TheGodFather()
        assert spart != god

    def test_new_object_has_entries_for_addins(self):
        spart = Spartacus()
        assert ["Add Onions", "Add Peppers",
                "Add Buffalo Sauce", "Add Tomatoes",
                "Add Pickles", "Add Dressing" in spart.instructions]

    def test_inheritance_from_base_class(self):
        spart = Spartacus()
        assert isinstance(spart, Wrap)

    def test_implements_Item_interface(self):
        spart = Spartacus()
        assert isinstance(spart, Item)

    @pytest.mark.parametrize("t_addin_modified", [Addin.PEPPERS, Addin.TOMATOES,
                                                  Addin.ONIONS, Addin.PICKLES,
                                                  Addin.BUFFALO_SAUCE,
                                                  Addin.DRESSING, Addin.MUSTARD])
    def test_modifying_addins_modifies_instructions(self, t_addin_modified):
        spart = Spartacus()
        spart.add_addin(t_addin_modified)
        assert "Add {}".format(t_addin_modified) in spart.instructions
        spart.remove_addin(t_addin_modified)
        assert "Add {}".format(t_addin_modified) not in spart.instructions

    def test_name_is_correct(self):
        spart = Spartacus()
        assert spart.name == "Spartacus"
