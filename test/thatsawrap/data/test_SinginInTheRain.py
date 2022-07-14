from src.thatsawrap.data.enums.Size import Size
from src.thatsawrap.data.drinks.SinginInTheRain import SinginInTheRain
from src.thatsawrap.data.drinks.ForrestGump import ForrestGump
import pytest
from src.thatsawrap.data.drinks.Drink import Drink
from src.thatsawrap.data.menu.Item import Item


class TestSinginInTheRain:

    def test_when_a_new_object_is_created_instructions_is_empty(self):
        sing = SinginInTheRain()
        assert len(sing.instructions) == 0

    def test_default_size_is_correct(self):
        sing = SinginInTheRain()
        assert sing.size == Size.INDIE

    @pytest.mark.parametrize("t_size, t_price", [
        (Size.INDIE, 2.75),
        (Size.STUDIO, 3.25),
        (Size.BLOCKBUSTER, 4.0)])
    def test_every_size_has_correct_price(self, t_size, t_price):
        sing = SinginInTheRain()
        sing.size = t_size
        assert sing.price == t_price

    @pytest.mark.parametrize("t_size, t_calories", [
        (Size.INDIE, 360),
        (Size.STUDIO, 400),
        (Size.BLOCKBUSTER, 550)])
    def test_every_size_has_correct_calories(self, t_size, t_calories):
        sing = SinginInTheRain()
        sing.size = t_size
        assert sing.calories == t_calories

    @pytest.mark.parametrize("t_size, t_string", [
        (Size.INDIE, "Indie Singin' In The Rain"),
        (Size.STUDIO, "Studio Singin' In The Rain"),
        (Size.BLOCKBUSTER, "Blockbuster Singin' In The Rain")])
    def test_every_size_has_correct_string_representation(self, t_size, t_string):
        sing = SinginInTheRain()
        sing.size = t_size
        assert str(sing) == t_string

    def test_flavors_are_correct_at_instantiation(self):
        sing = SinginInTheRain()
        assert sing.cherry
        assert not sing.strawberry
        assert not sing.cola
        assert not sing.grape

    def test_adding_or_removing_a_flavor_updates_instructions(self):
        sing = SinginInTheRain()
        sing.cherry = False
        assert len(sing.instructions) == 1
        sing.cherry = True
        assert len(sing.instructions) == 0
        sing.strawberry = True
        assert len(sing.instructions) == 1
        sing.strawberry = False
        assert len(sing.instructions) == 0
        sing.cola = True
        assert len(sing.instructions) == 1
        sing.cola = False
        assert len(sing.instructions) == 0
        sing.grape = True
        assert len(sing.instructions) == 1
        sing.grape = False
        assert len(sing.instructions) == 0

    def test_two_instances_of_same_object_are_equal(self):
        sing = SinginInTheRain()
        sing2 = SinginInTheRain()
        assert sing == sing2

    @pytest.mark.parametrize("t_size", [Size.INDIE, Size.STUDIO,
                                        Size.BLOCKBUSTER])
    def test_two_objects_with_different_sizes_are_not_equal(self, t_size):
        sing = SinginInTheRain()
        sing2 = SinginInTheRain()
        sing.size = t_size
        if sing.size == Size.INDIE:
            sing2.size = Size.BLOCKBUSTER
            assert sing != sing2
        else:
            assert sing != sing2

    def test_two_instances_with_different_flavors_are_not_equal(self):
        sing = SinginInTheRain()
        sing2 = SinginInTheRain
        sing.cherry = False
        assert sing != sing2
        sing.cherry = True
        sing.strawberry = True
        assert sing != sing2
        sing.strawberry = False
        sing.cola = True
        assert sing != sing2
        sing.cola = False
        sing.grape = True
        assert sing != sing2

    def test_instances_of_two_different_objects_are_not_equal(self):
        sing = SinginInTheRain()
        forrest = ForrestGump()
        assert sing != forrest

    def test_adding_or_removing_multiple_flavors_adds_multiple_to_instructions(self):
        sing = SinginInTheRain()
        sing.cherry = False
        assert len(sing.instructions) == 1
        sing.strawberry = True
        assert len(sing.instructions) == 2
        sing.grape = True
        assert len(sing.instructions) == 3
        sing.cola = True
        assert len(sing.instructions) == 4
        sing.cola = False
        assert len(sing.instructions) == 3

    def test_new_object_is_instance_of_base(self):
        sing = SinginInTheRain()
        assert isinstance(sing, Drink)

    def test_new_object_implements_item_interface(self):
        sing = SinginInTheRain()
        assert isinstance(sing, Item)

    def test_name_is_correct(self):
        sing = SinginInTheRain()
        assert sing.name == "Singin' in the Rain"
