"""The Menu.

This file contains the code required to
create a Menu type object that can
return all of the items at our restaurant.

Author: Dustin Hayes djhayes@ksu.edu
Version 0.1
"""
from typing import List
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
from src.thatsawrap.data.menu.Item import Item
from src.thatsawrap.data.order.Combo import Combo
from src.thatsawrap.data.wraps.Wrap import Wrap
from src.thatsawrap.data.drinks.Drink import Drink
from src.thatsawrap.data.sides.Side import Side
from src.thatsawrap.data.order.ComboBuilder import ComboBuilder

forrest_indie = ForrestGump()
forrest_studio = ForrestGump()
forrest_studio.size = Size.STUDIO
forrest_blockbuster = ForrestGump()
forrest_blockbuster.size = Size.BLOCKBUSTER
king_indie = KingKong()
king_studio = KingKong()
king_blockbuster = KingKong()
king_studio.size = Size.STUDIO
king_blockbuster.size = Size.BLOCKBUSTER
sing_indie = SinginInTheRain()
sing_studio = SinginInTheRain()
sing_blockbuster = SinginInTheRain()
sing_studio.size = Size.STUDIO
sing_blockbuster.size = Size.BLOCKBUSTER
snow_indie = SnowWhite()
snow_studio = SnowWhite()
snow_studio.size = Size.STUDIO
snow_blockbuster = SnowWhite()
snow_blockbuster.size = Size.BLOCKBUSTER
french_indie = TheFrenchConnection()
french_studio = TheFrenchConnection()
french_blockbuster = TheFrenchConnection()
french_studio.size = Size.STUDIO
french_blockbuster.size = Size.BLOCKBUSTER
yank_indie = YankeeDoodleDandy()
yank_studio = YankeeDoodleDandy()
yank_blockbuster = YankeeDoodleDandy()
yank_studio.size = Size.STUDIO
yank_blockbuster.size = Size.BLOCKBUSTER


class Menu(object):
    """The Menu class.

    This class contains static methods
    that will return the wraps, drinks,
    and sides that are available in the
    restaurant.

    Author: Dustin Hayes djhayes@ksu.edu
    Version 0.1
    """
    @classmethod
    def wraps(cls) -> List[Item]:
        """Getter for wraps.

        This method will return a list containing
        instances of all of the available wraps.

        Args:
            cls: reference to the Menu class.

        Returns:
            A List of Wrap/Item type objects.
        """
        return [TheGodFather(), WestSideStory(), SomeLikeItHot(),
                TheWizardOfOz(), Spartacus()]

    @classmethod
    def drinks(cls) -> List[Item]:
        """Getter for drinks.

        This method will return a list containing
        instances of all of the available drinks.

        Args:
            cls: reference to the Menu class.

        Returns:
            A List of Drink/Item type objects.
        """
        return [forrest_indie, forrest_studio, forrest_blockbuster,
                king_indie, king_studio, king_blockbuster,
                sing_indie, sing_blockbuster, sing_studio]

    @classmethod
    def sides(cls) -> List[Item]:
        """Getter for sides.

        This method will return a list containing
        instances of all of the available sides.

        Args:
            cls: reference to the Menu class.

        Returns:
            A List of Drink/Item type objects.
        """
        return [snow_indie, snow_studio, snow_blockbuster,
                french_indie, french_studio, french_blockbuster,
                yank_indie, yank_studio, yank_blockbuster]

    @classmethod
    def fullmenu(cls) -> List[Item]:
        """Getter for everything on the menu.

        This method will return a list containing
        an instance of all of the available items.

        Args:
            cls: reference to the Menu class

        Returns:
            A List of Item type objects.
        """
        return [TheGodFather(), WestSideStory(), SomeLikeItHot(),
                TheWizardOfOz(), Spartacus(), forrest_indie,
                forrest_studio, forrest_blockbuster,
                king_indie, king_studio, king_blockbuster,
                sing_indie, sing_blockbuster, sing_studio,
                snow_indie, snow_studio, snow_blockbuster,
                french_indie, french_studio, french_blockbuster,
                yank_indie, yank_studio, yank_blockbuster,
                ComboBuilder().build_combo("Classic"),
                ComboBuilder().build_combo("Hungry"),
                ComboBuilder().build_combo("Spicy"),
                ComboBuilder().build_combo("Green")]

    @classmethod
    def combos(cls) -> List[Combo]:
        """Getter for the combos.

        This method will return a list
        containing all named combos.

        Args:
            cls: reference to Menu class.

        Returns:
            A list of Combo type objects.
        """
        return [ComboBuilder().build_combo("Classic"),
                ComboBuilder().build_combo("Hungry"),
                ComboBuilder().build_combo("Spicy"),
                ComboBuilder().build_combo("Green")]

    @classmethod
    def parsed_drinks(cls) -> List[List[Item]]:
        """Getter for a parsed list of drinks.

        This method will return a nested list of
        items parsed such that it can be used to
        generate content of the website.

        Args:
            cls: reference to Menu class.

        Returns:
            A list of lists of Item/Drink type objects.
        """
        return [[forrest_indie, forrest_studio,
                 forrest_blockbuster],
                [king_indie, king_studio,
                 king_blockbuster], [sing_indie,
                 sing_studio, sing_blockbuster]]

    @classmethod
    def parsed_sides(cls) -> List[List[Item]]:
        """Getter for a parsed list of drinks.

        This method will return a nested list of
        items parsed such that it can be used to
        generate content of the website.

        Args:
            cls: reference to Menu class.

        Returns:
            A list of lists of Item/Drink type objects.
        """
        return [[yank_indie, yank_studio,
                 yank_blockbuster],
                [french_indie, french_studio,
                 french_blockbuster], [snow_indie,
                 snow_studio, snow_blockbuster]]

    @staticmethod
    def filter_keywords(items: List[Item],
                        keywords: str) -> List[Item]:
        """Filter based on keywords.

        This method will filter menu items
        based on a list of keywords. If an item
        on the menu contains one of the keywords,
        it will be returned.

        Args:
            items: The list of items to be filtered.
            keywords: The keywords to filter on.

        Returns:
            A list of items that meet the keyword
            criteria.
        """
        if keywords is None or len(keywords) == 0:
            return items
        output: List[Item] = list()
        for keyword in keywords.split(" "):
            keyword = keyword.lower()
            for item in items:
                if keyword in item.name.lower():
                    if item not in output:
                        output.append(item)
        combos: List[Combo] = Menu.combos()
        for keyword in keywords.split(" "):
            keyword = keyword.lower()
            for combo in combos:
                if keyword in combo.wrap.name.lower():
                    if combo not in output:
                        output.append(combo)
        return output

    @staticmethod
    def filter_type_of_item(wraps: bool, drinks: bool,
                            sides: bool, combos: bool,
                            items: List[Item]) -> List[Item]:
        """Filter based on type of item.

        This method will filter menu items
        based on the kind of item desired.

        Args:
            items: The list of items to be filtered.
            wraps: If set to False, this method will
            remove all wraps from the list.
            drinks: If set to False, this method will
            remove all drinks from the list.
            sides: If set to False, this method will
            remove all sides from the list.
            combos: If set to False, this method will
            remove all combos from the list.

        Returns:
            A list of items that meet the
            criteria.
        """
        output: List[Item] = list()
        if wraps:
            for item in items:
                if isinstance(item, Wrap):
                    output.append(item)
        if drinks:
            for item in items:
                if isinstance(item, Drink):
                    output.append(item)
        if sides:
            for item in items:
                if isinstance(item, Side):
                    output.append(item)
        if combos:
            for item in items:
                if isinstance(item, Combo):
                    output.append(item)
        return output

    @staticmethod
    def filter_calories(items: List[Item],
                        caloriesmin: int,
                        caloriesmax: int) -> List[Item]:
        """Filter based on calories.

        This method will filter menu items
        based on the number of calories the item
        contains.

        Args:
            items: The list of items to be filtered.
            caloriesmin: The minimum value for
            calories; all items with fewer calories
            will be removed from the list.
            caloriesmax: The maximum value for
            calories; all items with more calories
            will be removed from the list.

        Returns:
            A list of items that meet the
            criteria.
        """
        if caloriesmin < 0 and caloriesmax < 0:
            return items
        if caloriesmax < 0:
            caloriesmax = 5000
        output: List[Item] = list()
        for item in items:
            try:
                calories = item.calories
                if calories >= caloriesmin and calories <= caloriesmax:
                    output.append(item)
            except Exception:
                continue
        return output

    @staticmethod
    def filter_price(items: List[Item],
                        pricemin: float,
                        pricemax: float) -> List[Item]:
        """Filter based on price.

        This method will filter menu items
        based on price.

        Args:
            items: The list of items to be filtered.
            pricemin: The minimum value for
            price; all items that cost less
            will be removed from the list.
            pricemax: The maximum value for
            price; all items that cost more will be
            removed from the list.

        Returns:
            A list of items that meet the
            criteria.
        """
        if pricemin < 0 and pricemax < 0:
            return items
        if pricemax < 0:
            pricemax = 5000
        output: List[Item] = list()
        for item in items:
            try:
                price = item.price
                if price >= pricemin and price <= pricemax:
                    output.append(item)
            except Exception:
                continue
        return output
