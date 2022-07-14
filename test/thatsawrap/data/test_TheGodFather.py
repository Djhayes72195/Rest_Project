from src.thatsawrap.data.enums.Shell import Shell
from src.thatsawrap.data.enums.Addin import Addin
import pytest
from src.thatsawrap.data.wraps.SomeLikeItHot import SomeLikeItHot
from src.thatsawrap.data.wraps.TheGodFather import TheGodFather
from src.thatsawrap.data.wraps.Wrap import Wrap
from src.thatsawrap.data.menu.Item import Item


t_calories = 1268
t_base_price = 8.9


class TestTheGodFather:

    def test_new_object_instructions_list_should_be_default(self):
        god = TheGodFather()
        assert len(god.instructions) == 2

    def test_new_object_should_have_correct_shell(self):
        god = TheGodFather()
        assert god.shell == Shell.STROMBOLI

    def test_new_object_addins_are_default(self):
        god = TheGodFather()
        assert god.addins == {Addin.PEPPERS, Addin.ONIONS}

    def test_calories_are_correct(self):
        god = TheGodFather()
        assert god.calories == t_calories

    @pytest.mark.parametrize("t_shell, t_price", [
        (Shell.STROMBOLI, t_base_price + .75),
        (Shell.WHOLE_GRAIN, t_base_price),
        (Shell.SPINACH, t_base_price + .25)])
    def test_price_for_each_shell_is_correct(self, t_shell, t_price):
        god = TheGodFather()
        god.shell = t_shell
        assert god.price == t_price

    @pytest.mark.parametrize("t_shell, t_string", [
        (Shell.STROMBOLI, "The Godfather in a Stromboli Shell"),
        (Shell.WHOLE_GRAIN, "The Godfather in a Whole Grain Shell"),
        (Shell.SPINACH, "The Godfather in a Spinach Shell")])
    def test_string_for_each_shell_is_correct(self, t_shell, t_string):
        god = TheGodFather()
        god.shell = t_shell
        assert str(god) == t_string

    def test_pepperoni_included_by_default(self):
        god = TheGodFather()
        assert god.pepperoni

    def test_cheese_included_by_default(self):
        god = TheGodFather()
        assert god.cheese

    def test_sausage_included_by_default(self):
        god = TheGodFather()
        assert god.sausage

    def test_marinara_included_by_default(self):
        god = TheGodFather()
        assert god.marinara

    def test_changing_an_ingredient_should_change_instructions(self):
        god = TheGodFather()
        god.sausage = False
        assert len(god.instructions) == 3
        god.cheese = False
        assert len(god.instructions) == 4
        god.marinara = False
        assert len(god.instructions) == 5
        god.pepperoni = False
        assert len(god.instructions) == 6
        god.pepperoni = True
        assert len(god.instructions) == 5

    @pytest.mark.parametrize("t_addin", [Addin.PEPPERS, Addin.ONIONS])
    def test_addins_included_by_default(self, t_addin):
        god = TheGodFather()
        assert t_addin in god.addins

    @pytest.mark.parametrize("t_addin_removed", [Addin.PEPPERS, Addin.TOMATOES,
                                                 Addin.ONIONS, Addin.PICKLES,
                                                 Addin.BUFFALO_SAUCE, Addin.DRESSING,
                                                 Addin.MUSTARD])
    def test_modifying_addins_modifies_addin_list(self, t_addin_removed):
        god = TheGodFather()
        if t_addin_removed in god.addins:
            god.remove_addin(t_addin_removed)
            assert t_addin_removed not in god.addins
            god.add_addin(t_addin_removed)
            assert t_addin_removed in god.addins
        else:
            god.add_addin(t_addin_removed)
            assert t_addin_removed in god.addins

    def test_two_instances_of_same_object_are_equal(self):
        god = TheGodFather()
        god2 = TheGodFather()
        assert god == god2

    def test_two_objects_with_different_shells_are_not_equal(self):
        god = TheGodFather()
        god2 = TheGodFather()
        god2.shell = Shell.SPINACH
        assert god != god2
        god2.shell = Shell.WHOLE_GRAIN
        assert god != god2

    def test_two_objects_with_different_ingredients_are_not_equal(self):
        god = TheGodFather()
        god2 = TheGodFather()
        god2.cheese = False
        assert god != god2
        god2.cheese = True
        god2.pepperoni = False
        assert god != god2
        god2.pepperoni = True
        god2.marinara = False
        assert god != god2
        god2.marinara = True
        god2.sausage = False
        assert god != god2

    @pytest.mark.parametrize("t_addin_change", [Addin.PEPPERS, Addin.TOMATOES,
                                                Addin.ONIONS, Addin.PICKLES,
                                                Addin.BUFFALO_SAUCE,
                                                Addin.DRESSING, Addin.MUSTARD])
    def test_two_objects_different_addins_not_eq(self, t_addin_change):
        god = TheGodFather()
        if t_addin_change in god.addins:
            god.remove_addin(t_addin_change)
            god2 = TheGodFather()
            assert god != god2
        else:
            god.add_addin(t_addin_change)
            god2 = TheGodFather()
            assert god != god2

    def test_two_different_objects_are_not_equal(self):
        god = TheGodFather()
        some = SomeLikeItHot()
        assert god != some

    def test_new_object_has_entries_for_addins(self):
        god = TheGodFather()
        assert "Add Onions", "Add Peppers" in god.instructions

    def test_inheritance_from_base_class(self):
        god = TheGodFather()
        assert isinstance(god, Wrap)

    def test_implements_Item_interface(self):
        god = TheGodFather()
        assert isinstance(god, Item)

    @pytest.mark.parametrize("t_addin_modified", [Addin.PEPPERS, Addin.TOMATOES,
                                                  Addin.ONIONS, Addin.PICKLES,
                                                  Addin.BUFFALO_SAUCE,
                                                  Addin.DRESSING, Addin.MUSTARD])
    def test_modifying_addins_modifies_instructions(self, t_addin_modified):
        god = TheGodFather()
        god.add_addin(t_addin_modified)
        assert "Add {}".format(t_addin_modified) in god.instructions
        god.remove_addin(t_addin_modified)
        assert "Add {}".format(t_addin_modified) not in god.instructions

    def test_name_is_correct(self):
        god = TheGodFather()
        assert god.name == "The Godfather"
