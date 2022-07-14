from src.thatsawrap.data.enums.Size import Size
from src.thatsawrap.data.drinks.ForrestGump import ForrestGump
from src.thatsawrap.data.drinks.KingKong import KingKong
import pytest
from src.thatsawrap.data.drinks.Drink import Drink
from src.thatsawrap.data.menu.Item import Item


class TestForrestGump:

    def test_when_a_new_object_is_created_instructions_is_empty(self):
        forrest = ForrestGump()
        assert len(forrest.instructions) == 0

    def test_default_size_is_correct(self):
        forrest = ForrestGump()
        assert forrest.size == Size.INDIE

    @pytest.mark.parametrize("t_size, t_price", [
        (Size.INDIE, 5.25),
        (Size.STUDIO, 7.50),
        (Size.BLOCKBUSTER, 9.0)])
    def test_every_size_has_correct_price(self, t_size, t_price):
        forrest = ForrestGump()
        forrest.size = t_size
        assert forrest.price == t_price

    @pytest.mark.parametrize("t_size, t_calories", [
        (Size.INDIE, 980),
        (Size.STUDIO, 1365),
        (Size.BLOCKBUSTER, 1875)])
    def test_every_size_has_correct_calories(self, t_size, t_calories):
        forrest = ForrestGump()
        forrest.size = t_size
        assert forrest.calories == t_calories

    @pytest.mark.parametrize("t_size, t_string", [
        (Size.INDIE, "Indie Forrest Gump"),
        (Size.STUDIO, "Studio Forrest Gump"),
        (Size.BLOCKBUSTER, "Blockbuster Forrest Gump")])
    def test_every_size_has_correct_string_representation(self, t_size, t_string):
        forrest = ForrestGump()
        forrest.size = t_size
        assert str(forrest) == t_string

    def test_flavors_are_correct_at_instantiation(self):
        forrest = ForrestGump()
        assert forrest.chocolate
        assert not forrest.vanilla
        assert not forrest.caramel
        assert not forrest.coffee

    def test_adding_or_removing_a_flavor_updates_instructions(self):
        forrest = ForrestGump()
        forrest.chocolate = False
        assert len(forrest.instructions) == 1
        forrest.chocolate = True
        assert len(forrest.instructions) == 0
        forrest.vanilla = True
        assert len(forrest.instructions) == 1
        forrest.vanilla = False
        assert len(forrest.instructions) == 0
        forrest.caramel = True
        assert len(forrest.instructions) == 1
        forrest.caramel = False
        assert len(forrest.instructions) == 0
        forrest.coffee = True
        assert len(forrest.instructions) == 1
        forrest.coffee = False
        assert len(forrest.instructions) == 0

    def test_two_instances_of_same_object_are_equal(self):
        forrest = ForrestGump()
        forrest2 = ForrestGump()
        assert forrest == forrest2

    @pytest.mark.parametrize("t_size", [Size.INDIE, Size.STUDIO,
                                        Size.BLOCKBUSTER])
    def test_two_objects_with_different_sizes_are_not_equal(self, t_size):
        forrest = ForrestGump()
        forrest2 = ForrestGump()
        forrest.size = t_size
        if forrest.size == Size.INDIE:
            forrest2.size = Size.BLOCKBUSTER
            assert forrest != forrest2
        else:
            assert forrest != forrest2

    def test_two_instances_with_different_flavors_are_not_equal(self):
        forrest = ForrestGump()
        forrest2 = ForrestGump
        forrest.chocolate = False
        assert forrest != forrest2
        forrest.chocolate = True
        forrest.vanilla = True
        assert forrest != forrest2
        forrest.vanilla = False
        forrest.caramel = True
        assert forrest != forrest2
        forrest.caramel = False
        forrest.coffee = True
        assert forrest != forrest2

    def test_instances_of_two_different_objects_are_not_equal(self):
        kong = KingKong()
        forrest = ForrestGump()
        assert kong != forrest

    def test_adding_or_removing_multiple_flavors_adds_multiple_to_instructions(self):
        forrest = ForrestGump()
        forrest.chocolate = False
        assert len(forrest.instructions) == 1
        forrest.vanilla = True
        assert len(forrest.instructions) == 2
        forrest.caramel = True
        assert len(forrest.instructions) == 3
        forrest.coffee = True
        assert len(forrest.instructions) == 4
        forrest.coffee = False
        assert len(forrest.instructions) == 3

    def test_new_object_is_instance_of_base(self):
        forrest = ForrestGump()
        assert isinstance(forrest, Drink)

    def test_new_object_implements_Item_interface(self):
        forrest = ForrestGump()
        assert isinstance(forrest, Item)

    def test_name_is_correct(self):
        forrest = ForrestGump()
        assert forrest.name == "Forrest Gump"
