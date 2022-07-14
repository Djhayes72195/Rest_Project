"""The Tests for the ComboBuilder file.

This file contains a number of unit tests
used to verify that the ComboBuilder class is
working correctly.

Author: Dustin Hayes djhayes@ksu.edu
Version 0.1
"""
from src.thatsawrap.data.order.ComboBuilder import ComboBuilder
from src.thatsawrap.data.wraps.TheGodFather import TheGodFather
from src.thatsawrap.data.wraps.Spartacus import Spartacus
from src.thatsawrap.data.wraps.TheWizardOfOz import TheWizardOfOz
from src.thatsawrap.data.wraps.SomeLikeItHot import SomeLikeItHot
from src.thatsawrap.data.drinks.SinginInTheRain import SinginInTheRain
from src.thatsawrap.data.drinks.KingKong import KingKong
from src.thatsawrap.data.drinks.ForrestGump import ForrestGump
from src.thatsawrap.data.sides.TheFrenchConnection import TheFrenchConnection
from src.thatsawrap.data.sides.YankeeDoodleDandy import YankeeDoodleDandy
from src.thatsawrap.data.sides.SnowWhite import SnowWhite
import pytest


class TestComboBuilder:
    """The Tests for the ComboBuilder class.

    This class contains the unit tests
    used to verify that the ComboBuilder class is
    working correctly.
    """
    def test_classic_builds_correctly(self):
        """Test Build Classic.

        This test verifies that the builder
        correctly constructs the "Classic"
        combo.
        """
        classic = ComboBuilder().build_combo("Classic")
        assert classic.name == "Classic"
        assert type(classic.wrap) == TheGodFather
        assert type(classic.drink) == SinginInTheRain
        assert type(classic.side) == TheFrenchConnection

    def test_green_builds_correctly(self):
        """Test Build Green.

        This test verifies that the builder
        correctly constructs the "Green"
        combo.
        """
        green = ComboBuilder().build_combo("Green")
        assert green.name == "Green"
        assert type(green.wrap) == TheWizardOfOz
        assert type(green.drink) == KingKong
        assert type(green.side) == SnowWhite

    def test_hungry_builds_correctly(self):
        """Test Build Hungry.

        This test verifies that the builder
        correctly constructs the "Hungry"
        combo.
        """
        hungry = ComboBuilder().build_combo("Hungry")
        assert hungry.name == "Hungry"
        assert type(hungry.wrap) == Spartacus
        assert type(hungry.drink) == ForrestGump
        assert type(hungry.side) == YankeeDoodleDandy

    def test_spicy_builds_correctly(self):
        """Test Spicy Hungry.

        This test verifies that the builder
        correctly constructs the "Spicy"
        combo.
        """
        spicy = ComboBuilder().build_combo("Spicy")
        assert spicy.name == "Spicy"
        assert type(spicy.wrap) == SomeLikeItHot
        assert type(spicy.drink) == ForrestGump
        assert type(spicy.side) == TheFrenchConnection

    def test_bad_name_thros_exception(self):
        """Test bad name.

        This test verifies the ComboBuilder
        will throw an exception if provided
        with an invalid combo name.
        """
        with pytest.raises(Exception):
            bad = ComboBuilder().build_combo("bad")
