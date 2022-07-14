from src.thatsawrap.data.enums.Size import Size
from src.thatsawrap.data.sides.TheFrenchConnection import TheFrenchConnection
import pytest
from src.thatsawrap.data.sides.SnowWhite import SnowWhite
from src.thatsawrap.data.sides.Side import Side
from src.thatsawrap.data.menu.Item import Item


class TestSnowWhite:

    def test_new_object_should_have_default_size(self):
        snow = SnowWhite()
        assert snow.size == Size.INDIE

    @pytest.mark.parametrize("t_size, t_price", [
        (Size.INDIE, 1.5),
        (Size.STUDIO, 2.25),
        (Size.BLOCKBUSTER, 3.0)])
    def test_every_size_has_correct_price(self, t_size, t_price):
        snow = SnowWhite()
        snow.size = t_size
        assert snow.price == t_price

    @pytest.mark.parametrize("t_size, t_calories", [
        (Size.INDIE, 225),
        (Size.STUDIO, 350),
        (Size.BLOCKBUSTER, 475)])
    def test_every_size_has_correct_calories(self, t_size, t_calories):
        snow = SnowWhite()
        snow.size = t_size
        assert snow.calories == t_calories

    @pytest.mark.parametrize("t_size, t_string", [
        (Size.INDIE, "Indie Snow White"),
        (Size.STUDIO, "Studio Snow White"),
        (Size.BLOCKBUSTER, "Blockbuster Snow White")])
    def test_every_size_has_correct_str_representation(self, t_size, t_string):
        snow = SnowWhite()
        snow.size = t_size
        assert str(snow) == t_string

    def test_two_instances_of_same_object_are_equal(self):
        snow = SnowWhite()
        snow2 = SnowWhite()
        assert snow == snow2

    @pytest.mark.parametrize("t_size", [Size.INDIE, Size.STUDIO,
                                        Size.BLOCKBUSTER])
    def test_two_objects_with_different_sizes_are_not_equal(self, t_size):
        snow = SnowWhite()
        snow2 = SnowWhite()
        snow.size = t_size
        if snow2.size == Size.INDIE:
            snow.size = Size.BLOCKBUSTER
            assert snow != snow2
        else:
            assert snow != snow2

    def test_an_instance_of_a_different_object_is_not_equal(self):
        snow = SnowWhite()
        french = TheFrenchConnection()
        assert snow != french

    def test_new_object_is_instance_of_base(self):
        snow = SnowWhite()
        assert isinstance(snow, Side)

    def test_new_object_implements_item_interface(self):
        snow = SnowWhite()
        assert isinstance(snow, Item)

    def test_new_object_has_no_instructions(self):
        snow = SnowWhite()
        assert len(snow.instructions) == 0

    def test_name_is_correct(self):
        snow = SnowWhite()
        assert snow.name == "Snow White"
