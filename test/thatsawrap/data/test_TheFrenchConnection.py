from src.thatsawrap.data.enums.Size import Size
from src.thatsawrap.data.sides.TheFrenchConnection import TheFrenchConnection
import pytest
from src.thatsawrap.data.sides.YankeeDoodleDandy import YankeeDoodleDandy
from src.thatsawrap.data.sides.Side import Side
from src.thatsawrap.data.menu.Item import Item


class TestTheFrenchConnection:

    def test_new_object_should_have_default_size(self):
        french = TheFrenchConnection()
        assert french.size == Size.INDIE

    @pytest.mark.parametrize("t_size, t_price", [
        (Size.INDIE, 2.75),
        (Size.STUDIO, 4.85),
        (Size.BLOCKBUSTER, 5.25)])
    def test_every_size_has_correct_price(self, t_size, t_price):
        french = TheFrenchConnection()
        french.size = t_size
        assert french.price == t_price

    @pytest.mark.parametrize("t_size, t_calories", [
        (Size.INDIE, 550),
        (Size.STUDIO, 700),
        (Size.BLOCKBUSTER, 950)])
    def test_every_size_has_correct_calories(self, t_size, t_calories):
        french = TheFrenchConnection()
        french.size = t_size
        assert french.calories == t_calories

    @pytest.mark.parametrize("t_size, t_string", [
        (Size.INDIE, "Indie The French Connection"),
        (Size.STUDIO, "Studio The French Connection"),
        (Size.BLOCKBUSTER, "Blockbuster The French Connection")])
    def test_every_size_has_correct_str_representation(self, t_size, t_string):
        french = TheFrenchConnection()
        french.size = t_size
        assert str(french) == t_string

    def test_two_instances_of_same_object_are_equal(self):
        french = TheFrenchConnection()
        french2 = TheFrenchConnection()
        assert french == french2

    @pytest.mark.parametrize("t_size", [Size.INDIE, Size.STUDIO,
                                        Size.BLOCKBUSTER])
    def test_two_objects_with_different_sizes_are_not_equal(self, t_size):
        french = TheFrenchConnection()
        french2 = TheFrenchConnection()
        french.size = t_size
        if french2.size == Size.INDIE:
            french.size = Size.BLOCKBUSTER
            assert french != french2
        else:
            assert french != french2

    def test_an_instance_of_a_different_object_is_not_equal(self):
        french = TheFrenchConnection()
        yank = YankeeDoodleDandy()
        assert french != yank

    def test_new_object_is_instance_of_base(self):
        french = TheFrenchConnection()
        assert isinstance(french, Side)

    def test_new_object_implements_Item_interface(self):
        french = TheFrenchConnection()
        assert isinstance(french, Item)

    def test_new_object_has_no_instructions(self):
        french = TheFrenchConnection()
        assert len(french.instructions) == 0

    def test_name_is_correct(self):
        french = TheFrenchConnection()
        assert french.name == "The French Connection"
