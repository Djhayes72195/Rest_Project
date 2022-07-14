"""Combo builder.

Follows builder pattern to construct
combos.

Author: Dustin hayes djhayes@ksu.edu
Version: 0.1
"""
from src.thatsawrap.data.wraps.TheGodFather import TheGodFather
from src.thatsawrap.data.wraps.Spartacus import Spartacus
from src.thatsawrap.data.wraps.TheWizardOfOz import TheWizardOfOz
from src.thatsawrap.data.wraps.SomeLikeItHot import SomeLikeItHot
from src.thatsawrap.data.sides.TheFrenchConnection import TheFrenchConnection
from src.thatsawrap.data.sides.SnowWhite import SnowWhite
from src.thatsawrap.data.sides.YankeeDoodleDandy import YankeeDoodleDandy
from src.thatsawrap.data.drinks.ForrestGump import ForrestGump
from src.thatsawrap.data.drinks.KingKong import KingKong
from src.thatsawrap.data.drinks.SinginInTheRain import SinginInTheRain
from src.thatsawrap.data.order.Combo import Combo


class ComboBuilder:
    """Combo builder class.

    Contains the code to construct
    combos based on key-words.
    """
    @staticmethod
    def build_combo(c_name: str) -> Combo:
        """Build combo method.

        Takes a string input to construct
        and return one of 4 combos.

        Args:
            c_name: A string representing
            one of 4 combos.
        
        Returns: A combo type object,
        populated with the appropriate
        attributes depending on the key-words
        given to the method.
        """
        if c_name == "Classic":
            c = Combo("Classic")
            c.wrap = TheGodFather()
            c.drink = SinginInTheRain()
            c.side = TheFrenchConnection()
            return c
        elif c_name == "Green":
            g = Combo("Green")
            g.wrap = TheWizardOfOz()
            g.drink = KingKong()
            g.side = SnowWhite()
            return g
        elif c_name == "Hungry":
            h = Combo("Hungry")
            h.wrap = Spartacus()
            h.drink = ForrestGump()
            h.side = YankeeDoodleDandy()
            return h
        elif c_name == "Spicy":
            s = Combo("Spicy")
            s.wrap = SomeLikeItHot()
            s.drink = ForrestGump()
            s.side = TheFrenchConnection()
            return s
        elif c_name == "Custom Combo":
            custom = Combo()
            return custom
        else:
            raise ValueError
