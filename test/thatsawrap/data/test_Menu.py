from src.thatsawrap.data.enums.Size import Size
from src.thatsawrap.data.wraps.TheGodFather import TheGodFather
from src.thatsawrap.data.wraps.WestSideStory import WestSideStory
from src.thatsawrap.data.wraps.SomeLikeItHot import SomeLikeItHot
from src.thatsawrap.data.wraps.TheWizardOfOz import TheWizardOfOz
from src.thatsawrap.data.wraps.Spartacus import Spartacus
from src.thatsawrap.data.sides.YankeeDoodleDandy import YankeeDoodleDandy
from src.thatsawrap.data.sides.TheFrenchConnection import TheFrenchConnection
from src.thatsawrap.data.sides.SnowWhite import SnowWhite
from src.thatsawrap.data.drinks.ForrestGump import ForrestGump
from src.thatsawrap.data.drinks.SinginInTheRain import SinginInTheRain
from src.thatsawrap.data.drinks.KingKong import KingKong
from src.thatsawrap.data.menu.Menu import Menu
from src.thatsawrap.data.wraps.Wrap import Wrap
from src.thatsawrap.data.drinks.Drink import Drink
from src.thatsawrap.data.sides.Side import Side
from src.thatsawrap.data.order.Combo import Combo
import pytest
from typing import List
from unittest.mock import patch, PropertyMock


class TestMenu:

    @pytest.mark.parametrize("t_wrap", [TheGodFather(), WestSideStory(),
                                        SomeLikeItHot(), TheWizardOfOz(),
                                        Spartacus()])
    def test_wraps_list_has_all_wraps(self, t_wrap):
        menu = Menu()
        assert t_wrap in menu.wraps()

    @pytest.mark.parametrize("t_side", [YankeeDoodleDandy(),
                                        SnowWhite(),
                                        TheFrenchConnection()])
    def test_menu_side_list_has_all_sides(self, t_side):
        menu = Menu()
        assert t_side in menu.sides()
        t_side.size = Size.STUDIO
        assert t_side.size == Size.STUDIO
        assert t_side in menu.sides()
        t_side.size = Size.BLOCKBUSTER
        assert t_side.size == Size.BLOCKBUSTER
        assert t_side in menu.sides()

    @pytest.mark.parametrize("t_drink", [ForrestGump(),
                                         KingKong(),
                                         SinginInTheRain()])
    def test_menu_drink_list_has_all_drinks(self, t_drink):
        menu = Menu()
        assert t_drink in menu.drinks()
        t_drink.size = Size.STUDIO
        assert t_drink.size == Size.STUDIO
        assert t_drink in menu.drinks()
        t_drink.size = Size.BLOCKBUSTER
        assert t_drink.size == Size.BLOCKBUSTER
        assert t_drink in menu.drinks()

    @pytest.mark.parametrize("t_item", [TheGodFather(), WestSideStory(),
                                        SomeLikeItHot(), TheWizardOfOz(),
                                        Spartacus(), YankeeDoodleDandy(),
                                        SnowWhite(), TheFrenchConnection(),
                                        ForrestGump(), KingKong(),
                                        SinginInTheRain()])
    def test_full_menu_has_all_items(self, t_item):
        menu = Menu()
        assert t_item in menu.fullmenu()
        if not isinstance(t_item, Wrap):
            t_item.size = Size.STUDIO
            assert t_item in menu.fullmenu()
            t_item.size = Size.BLOCKBUSTER
            assert t_item in menu.fullmenu()

    @pytest.mark.parametrize("t_size", [Size.INDIE, Size.STUDIO,
                                        Size.BLOCKBUSTER])
    def test_parsed_drinks_has_correct_content(self, t_size):
        menu = Menu()
        forrest = ForrestGump()
        king = KingKong()
        sing = SinginInTheRain()
        forrest.size = t_size
        king.size = t_size
        sing.size = t_size
        assert forrest in menu.parsed_drinks()[0]
        assert king in menu.parsed_drinks()[1]
        assert sing in menu.parsed_drinks()[2]

    @pytest.mark.parametrize("t_size", [Size.INDIE, Size.STUDIO,
                                        Size.BLOCKBUSTER])
    def test_parsed_sides_has_correct_content(self, t_size):
        menu = Menu()
        yank = YankeeDoodleDandy()
        french = TheFrenchConnection()
        snow = SnowWhite()
        yank.size = t_size
        french.size = t_size
        snow.size = t_size
        assert yank in menu.parsed_sides()[0]
        assert french in menu.parsed_sides()[1]
        assert snow in menu.parsed_sides()[2]

    def test_filter_by_keyword_none_returns_full_menu(self):
        menu = Menu()
        item = menu.fullmenu()
        keywords = None
        item2 = menu.filter_keywords(item, keywords)
        assert item == item2

    def test_filter_by_keyword_works_correctly(self):
        menu = Menu()
        god = TheGodFather()
        king = KingKong()
        snow = SnowWhite()
        item_list = menu.filter_keywords(menu.fullmenu(), "god")
        assert god in item_list
        assert snow not in item_list
        assert king not in item_list

    @patch('src.thatsawrap.data.sides.Side', spec=Side)
    @patch('src.thatsawrap.data.wraps.Wrap', spec=Wrap)
    @patch('src.thatsawrap.data.drinks.Drink', spec=Drink)
    @patch('src.thatsawrap.data.order.Combo', spec=Combo)
    def test_filter_by_type_works_correctly(self, mock_side,
                                            mock_wrap, mock_drink,
                                            mock_combo):
        mock_wrap.__class__ = Wrap
        mock_drink.__class__ = Drink
        mock_side.__class__ = Side
        mock_combo.__class__ = Combo
        mock_list: List[object] = [mock_wrap, mock_drink,
                                   mock_side, mock_combo]
        menu = Menu()
        mock_list_2 = menu.filter_type_of_item(wraps=False,
                                               drinks=False,
                                               sides=False,
                                               combos=False,
                                               items=mock_list)
        assert len(mock_list_2) == 0
        mock_list_3 = menu.filter_type_of_item(wraps=True,
                                               drinks=True,
                                               sides=True,
                                               combos=True,
                                               items=mock_list)
        assert mock_list_3 == mock_list

    @patch('src.thatsawrap.data.sides.Side', spec=Side)
    @patch('src.thatsawrap.data.wraps.Wrap', spec=Wrap)
    @patch('src.thatsawrap.data.drinks.Drink', spec=Drink)
    @patch('src.thatsawrap.data.order.Combo', spec=Combo)
    def test_filter_by_calories_works(self, mock_side,
                                      mock_wrap, mock_drink,
                                      mock_combo):
        type(mock_wrap).calories = PropertyMock(return_value=2)
        type(mock_drink).calories = PropertyMock(return_value=2)
        type(mock_side).calories = PropertyMock(return_value=2)
        type(mock_combo).calories = PropertyMock(return_value=2)
        mock_list: List[object] = [mock_wrap, mock_drink,
                                   mock_side, mock_combo]
        menu = Menu()
        mock_list_2 = menu.filter_calories(mock_list, 3, 4)
        assert len(mock_list_2) == 0
        mock_list_3 = menu.filter_calories(mock_list, 1, 4)
        assert mock_list_3 == mock_list

    @patch('src.thatsawrap.data.sides.Side', spec=Side)
    @patch('src.thatsawrap.data.wraps.Wrap', spec=Wrap)
    @patch('src.thatsawrap.data.drinks.Drink', spec=Drink)
    @patch('src.thatsawrap.data.order.Combo', spec=Combo)
    def test_filter_by_price_works(self, mock_side,
                                      mock_wrap, mock_drink,
                                      mock_combo):
        type(mock_wrap).price = PropertyMock(return_value=2)
        type(mock_drink).price = PropertyMock(return_value=2)
        type(mock_side).price = PropertyMock(return_value=2)
        type(mock_combo).price = PropertyMock(return_value=2)
        mock_list: List[object] = [mock_wrap, mock_drink,
                                   mock_side, mock_combo]
        menu = Menu()
        mock_list_2 = menu.filter_price(mock_list, 3, 4)
        assert len(mock_list_2) == 0
        mock_list_3 = menu.filter_price(mock_list, 1, 4)
        assert mock_list_3 == mock_list
