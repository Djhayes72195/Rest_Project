from src.thatsawrap.data.enums.Size import Size
from src.thatsawrap.data.sides.YankeeDoodleDandy import YankeeDoodleDandy
import pytest
from src.thatsawrap.data.sides.SnowWhite import SnowWhite
from src.thatsawrap.data.sides.Side import Side
from src.thatsawrap.data.menu.Item import Item


class TestYankeeDoodleDandy:

    def test_new_object_should_have_default_size(self):
        yank = YankeeDoodleDandy()
        assert yank.size == Size.INDIE

    @pytest.mark.parametrize("t_size, t_price", [
        (Size.INDIE, 2.25),
        (Size.STUDIO, 3.65),
        (Size.BLOCKBUSTER, 6.25)])
    def test_every_size_has_correct_price(self, t_size, t_price):
        yank = YankeeDoodleDandy()
        yank.size = t_size
        assert yank.price == t_price

    @pytest.mark.parametrize("t_size, t_calories", [
        (Size.INDIE, 400),
        (Size.STUDIO, 650),
        (Size.BLOCKBUSTER, 875)])
    def test_every_size_has_correct_calories(self, t_size, t_calories):
        yank = YankeeDoodleDandy()
        yank.size = t_size
        assert yank.calories == t_calories

    @pytest.mark.parametrize("t_size, t_string", [
        (Size.INDIE, "Indie Yankee Doodle Dandy"),
        (Size.STUDIO, "Studio Yankee Doodle Dandy"),
        (Size.BLOCKBUSTER, "Blockbuster Yankee Doodle Dandy")])
    def test_every_size_has_correct_str_representation(self, t_size, t_string):
        yank = YankeeDoodleDandy()
        yank.size = t_size
        assert str(yank) == t_string

    def test_two_instances_of_same_object_are_equal(self):
        yank = YankeeDoodleDandy()
        yank2 = YankeeDoodleDandy()
        assert yank == yank2

    @pytest.mark.parametrize("t_size", [Size.INDIE, Size.STUDIO,
                                        Size.BLOCKBUSTER])
    def test_two_objects_with_different_sizes_are_not_equal(self, t_size):
        yank = YankeeDoodleDandy()
        yank2 = YankeeDoodleDandy()
        yank.size = t_size
        if yank.size == Size.INDIE:
            yank2.size = Size.BLOCKBUSTER
            assert yank != yank2
        else:
            assert yank != yank2

    def test_an_instance_of_a_different_object_is_not_equal(self):
        yank = YankeeDoodleDandy()
        snow = SnowWhite()
        assert yank != snow

    def test_new_object_is_instance_of_base(self):
        yank = YankeeDoodleDandy()
        assert isinstance(yank, Side)

    def test_new_object_implements_item_interface(self):
        yank = YankeeDoodleDandy()
        assert isinstance(yank, Item)

    def test_new_object_has_no_instructions(self):
        yank = YankeeDoodleDandy()
        assert len(yank.instructions) == 0

    def test_name_is_correct(self):
        yank = YankeeDoodleDandy()
        assert yank.name == "Yankee Doodle Dandy"
