from src.thatsawrap.data.enums.Shell import Shell
from src.thatsawrap.data.enums.Addin import Addin
import pytest
from src.thatsawrap.data.wraps.WestSideStory import WestSideStory
from src.thatsawrap.data.wraps.Spartacus import Spartacus
from src.thatsawrap.data.wraps.Wrap import Wrap
from src.thatsawrap.data.menu.Item import Item


t_calories = 1240
t_base_price = 8.75


class TestWestSideStory:

    def test_new_object_instructions_list_should_be_default(self):
        west = WestSideStory()
        assert len(west.instructions) == 3

    def test_new_object_should_have_correct_shell(self):
        west = WestSideStory()
        assert west.shell == Shell.WHOLE_GRAIN

    def test_new_object_addins_are_default(self):
        west = WestSideStory()
        assert west.addins == {Addin.ONIONS, Addin.PICKLES, Addin.MUSTARD}

    def test_calories_are_correct(self):
        west = WestSideStory()
        assert west.calories == t_calories

    @pytest.mark.parametrize("t_shell, t_price", [
        (Shell.STROMBOLI, t_base_price + .75),
        (Shell.WHOLE_GRAIN, t_base_price),
        (Shell.SPINACH, t_base_price + .25)])
    def test_price_for_each_shell_is_correct(self, t_shell, t_price):
        west = WestSideStory()
        west.shell = t_shell
        assert west.price == t_price

    @pytest.mark.parametrize("t_shell, t_string", [
        (Shell.STROMBOLI, "West Side Story in a Stromboli Shell"),
        (Shell.WHOLE_GRAIN, "West Side Story in a Whole Grain Shell"),
        (Shell.SPINACH, "West Side Story in a Spinach Shell")])
    def test_string_for_each_shell_is_correct(self, t_shell, t_string):
        west = WestSideStory()
        west.shell = t_shell
        assert str(west) == t_string

    def test_corned_beef_included_by_default(self):
        west = WestSideStory()
        assert west.corned_beef

    def test_cheese_included_by_default(self):
        west = WestSideStory()
        assert west.cheese

    def test_cabbage_included_by_default(self):
        west = WestSideStory()
        assert west.cabbage

    def test_changing_an_ingredient_should_change_instructions(self):
        west = WestSideStory()
        west.corned_beef = False
        assert len(west.instructions) == 4
        west.cheese = False
        assert len(west.instructions) == 5
        west.corned_beef = True
        assert len(west.instructions) == 4
        west.cabbage = False
        assert len(west.instructions) == 5

    @pytest.mark.parametrize("t_addin", [Addin.ONIONS, Addin.PICKLES, Addin.MUSTARD])
    def test_addins_included_by_default(self, t_addin):
        west = WestSideStory()
        assert t_addin in west.addins

    @pytest.mark.parametrize("t_addin_removed", [Addin.PEPPERS, Addin.TOMATOES,
                                                 Addin.ONIONS, Addin.PICKLES,
                                                 Addin.BUFFALO_SAUCE,
                                                 Addin.DRESSING, Addin.MUSTARD])
    def test_modifying_addins_modifies_addin_list(self, t_addin_removed):
        west = WestSideStory()
        if t_addin_removed in west.addins:
            west.remove_addin(t_addin_removed)
            assert t_addin_removed not in west.addins
            west.add_addin(t_addin_removed)
            assert t_addin_removed in west.addins
        else:
            west.add_addin(t_addin_removed)
            assert t_addin_removed in west.addins

    def test_two_instances_of_same_object_are_equal(self):
        west = WestSideStory()
        west2 = WestSideStory()
        assert west == west2

    def test_two_objects_with_different_shells_are_not_equal(self):
        west = WestSideStory()
        west2 = WestSideStory()
        west2.shell = Shell.STROMBOLI
        assert west != west2
        west2.shell = Shell.SPINACH
        assert west != west2

    def test_two_objects_with_different_ingredients_are_not_equal(self):
        west = WestSideStory()
        west2 = WestSideStory()
        west2.cheese = False
        assert west != west2
        west2.cheese = True
        west2.corned_beef = False
        assert west != west2
        west2.corned_beef = True
        west2.cabbage = False
        assert west != west2

    @pytest.mark.parametrize("t_addin_change", [Addin.PEPPERS, Addin.TOMATOES,
                                                Addin.ONIONS, Addin.PICKLES,
                                                Addin.BUFFALO_SAUCE,
                                                Addin.DRESSING, Addin.MUSTARD])
    def test_two_objects_with_different_addins_are_not_equal(self, t_addin_change):
        west = WestSideStory()
        if t_addin_change in west.addins:
            west.remove_addin(t_addin_change)
            west2 = WestSideStory()
            assert west != west2
        else:
            west.add_addin(t_addin_change)
            west2 = WestSideStory()
            assert west != west2

    def test_two_different_objects_are_not_equal(self):
        west = WestSideStory()
        spart = Spartacus()
        assert west != spart

    def test_new_object_has_entries_for_addins(self):
        west = WestSideStory()
        assert "Add Tomatoes", "Add Dressing" in west.instructions

    def test_inheritance_from_base_class(self):
        west = WestSideStory()
        assert isinstance(west, Wrap)

    def test_implements_Item_interface(self):
        west = WestSideStory()
        assert isinstance(west, Item)

    @pytest.mark.parametrize("t_addin_modified", [Addin.PEPPERS, Addin.TOMATOES,
                                                  Addin.ONIONS, Addin.PICKLES,
                                                  Addin.BUFFALO_SAUCE,
                                                  Addin.DRESSING, Addin.MUSTARD])
    def test_modifying_addins_modifies_instructions(self, t_addin_modified):
        west = WestSideStory()
        west.add_addin(t_addin_modified)
        assert "Add {}".format(t_addin_modified) in west.instructions
        west.remove_addin(t_addin_modified)
        assert "Add {}".format(t_addin_modified) not in west.instructions

    def test_name_is_correct(self):
        west = WestSideStory()
        assert west.name == "West Side Story"
