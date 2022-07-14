from src.thatsawrap.data.enums.Size import Size
from src.thatsawrap.data.drinks.KingKong import KingKong
from src.thatsawrap.data.drinks.SinginInTheRain import SinginInTheRain
import pytest
from src.thatsawrap.data.drinks.Drink import Drink
from src.thatsawrap.data.menu.Item import Item


class TestKingKong:

    def test_when_a_new_object_is_created_instructions_is_empty(self):
        kong = KingKong()
        assert len(kong.instructions) == 0

    def test_default_size_is_correct(self):
        kong = KingKong()
        assert kong.size == Size.INDIE

    @pytest.mark.parametrize("t_size, t_price", [
        (Size.INDIE, 4.85),
        (Size.STUDIO, 5.95),
        (Size.BLOCKBUSTER, 7.45)])
    def test_every_size_has_correct_price(self, t_size, t_price):
        kong = KingKong()
        kong.size = t_size
        assert kong.price == t_price

    @pytest.mark.parametrize("t_size, t_calories", [
        (Size.INDIE, 465),
        (Size.STUDIO, 625),
        (Size.BLOCKBUSTER, 860)])
    def test_every_size_has_correct_calories(self, t_size, t_calories):
        kong = KingKong()
        kong.size = t_size
        assert kong.calories == t_calories

    @pytest.mark.parametrize("t_size, t_string", [
        (Size.INDIE, "Indie King Kong"),
        (Size.STUDIO, "Studio King Kong"),
        (Size.BLOCKBUSTER, "Blockbuster King Kong")])
    def test_every_size_has_correct_string_representation(self, t_size, t_string):
        kong = KingKong()
        kong.size = t_size
        assert str(kong) == t_string

    def test_flavors_are_correct_at_instantiation(self):
        kong = KingKong()
        assert kong.banana
        assert not kong.strawberry
        assert not kong.peach
        assert not kong.mango

    def test_adding_or_removing_a_flavor_updates_instructions(self):
        kong = KingKong()
        kong.banana = False
        assert len(kong.instructions) == 1
        kong.banana = True
        assert len(kong.instructions) == 0
        kong.strawberry = True
        assert len(kong.instructions) == 1
        kong.strawberry = False
        assert len(kong.instructions) == 0
        kong.peach = True
        assert len(kong.instructions) == 1
        kong.peach = False
        assert len(kong.instructions) == 0
        kong.mango = True
        assert len(kong.instructions) == 1
        kong.mango = False
        assert len(kong.instructions) == 0

    def test_two_instances_of_same_object_are_equal(self):
        kong = KingKong()
        kong2 = KingKong()
        assert kong == kong2

    @pytest.mark.parametrize("t_size", [Size.INDIE, Size.STUDIO,
                                        Size.BLOCKBUSTER])
    def test_two_objects_with_different_sizes_are_not_equal(self, t_size):
        kong = KingKong()
        kong2 = KingKong()
        kong.size = t_size
        if kong.size == Size.INDIE:
            kong2.size = Size.BLOCKBUSTER
            assert kong != kong2
        else:
            assert kong != kong2

    def test_two_instances_with_different_flavors_are_not_equal(self):
        kong = KingKong()
        kong2 = KingKong
        kong.banana = False
        assert kong != kong2
        kong.banana = True
        kong.strawberry = True
        assert kong != kong2
        kong.strawberry = False
        kong.peach = True
        assert kong != kong2
        kong.peach = False
        kong.mango = True
        assert kong != kong2

    def test_instances_of_two_different_objects_are_not_equal(self):
        kong = KingKong()
        sing = SinginInTheRain()
        assert kong != sing

    def test_adding_or_removing_multiple_flavors_adds_multiple_to_instructions(self):
        kong = KingKong()
        kong.banana = False
        assert len(kong.instructions) == 1
        kong.strawberry = True
        assert len(kong.instructions) == 2
        kong.mango = True
        assert len(kong.instructions) == 3
        kong.peach = True
        assert len(kong.instructions) == 4
        kong.peach = False
        assert len(kong.instructions) == 3

    def test_new_object_is_instance_of_base(self):
        king = KingKong()
        assert isinstance(king, Drink)

    def test_new_object_implements_Item_interface(self):
        king = KingKong()
        assert isinstance(king, Item)

    def test_name_is_correct(self):
        king = KingKong()
        assert king.name == "King Kong"
