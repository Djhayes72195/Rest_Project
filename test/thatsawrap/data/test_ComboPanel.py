"""The Tests for the Combo Panel.

This file contains a number of unit tests
used to verify that the Combo panel is
working correctly.

Author: Dustin Hayes djhayes@ksu.edu
Version 0.1
"""
from src.thatsawrap.gui.combo.ComboPanel import ComboPanel
from src.thatsawrap.gui.combo.ComboPanelFactory import ComboPanelFactory
from src.thatsawrap.data.order.Combo import Combo
from src.thatsawrap.gui.PrimaryWindow import PrimaryWindow



class TestComboPanel:
    """Combo Panel panel test class.

    This class contains all of the unit
    tests for the Combo Panel.
    """
    # def test_custom_instantiates_correctly(self):
        # master = PrimaryWindow()
        # cp = ComboPanel(master, item = Combo())
        # assert type(cp.wrap) is None

