"""Sample HelloWorld Program.

This is a sample HelloWorld program to demonstrate proper
Python coding style, testing, documentation, and more.

Author: Russell Feldhausen russfeld@ksu.edu
Version: 0.1
"""
from typing import List
from src.thatsawrap.data.enums.Size import Size
from src.thatsawrap.data.enums.Addin import Addin
from src.thatsawrap.data.enums.Shell import Shell
from src.thatsawrap.data.wraps.TheGodFather import TheGodFather
from src.thatsawrap.data.wraps.WestSideStory import WestSideStory
from src.thatsawrap.data.wraps.SomeLikeItHot import SomeLikeItHot
from src.thatsawrap.data.wraps.TheWizardOfOz import TheWizardOfOz
from src.thatsawrap.data.wraps.Spartacus import Spartacus
from src.thatsawrap.data.enums.Shell import Shell
from src.thatsawrap.data.enums.Addin import Addin
from src.thatsawrap.data.enums.Size import Size
from src.thatsawrap.data.sides.YankeeDoodleDandy import YankeeDoodleDandy
from src.thatsawrap.data.sides.TheFrenchConnection import TheFrenchConnection
from src.thatsawrap.data.sides.SnowWhite import SnowWhite
from src.thatsawrap.data.drinks.ForrestGump import ForrestGump
from src.thatsawrap.data.drinks.SinginInTheRain import SinginInTheRain
from src.thatsawrap.data.drinks.KingKong import KingKong
from src.thatsawrap.data.menu.Item import Item
from src.thatsawrap.data.menu.Menu import Menu
from src.thatsawrap.gui.PrimaryWindow import PrimaryWindow
from src.thatsawrap.gui.drinks.KingKongPanel import KingKongPanel
from src.thatsawrap.data.order.Order import Order
from src.thatsawrap.data.order.Combo import Combo
from src.thatsawrap.data.order.ComboBuilder import ComboBuilder
from src.thatsawrap.data.order.OrderNumberSingleton import OrderNumberSingleton
from src.thatsawrap.gui.PanelFactory import PanelFactory


class HelloWorld:
    """Simple HelloWorld Class.

    Prints "Hello World" to the terminal when the main function is executed.
    """
    @staticmethod
    def main(args: List[str]) -> None:
        """Prints a hello message.

        This method prints the standard "Hello World" message to the terminal.

        Args:
            args: The command-line arguments provided to the program.
        """
        if len(args) == 2:
            print("Hello {}".format(args[1]))
        else:
            # ord = Order()
            # PrimaryWindow().mainloop()
            forrestgump = ForrestGump()
            forrestgump.size = Size.BLOCKBUSTER
            print(forrestgump.calories)
