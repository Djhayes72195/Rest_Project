"""Panel Factory.

Constructs panels according to string input.

Author: Dustin hayes djhayes@ksu.edu
Version: 0.1
"""
from src.thatsawrap.data.menu.Item import Item
from src.thatsawrap.data.enums.Size import Size
from src.thatsawrap.data.wraps.TheGodFather import TheGodFather
from src.thatsawrap.gui.wraps.TheGodFatherPanel import TheGodFatherPanel
from src.thatsawrap.data.wraps.WestSideStory import WestSideStory
from src.thatsawrap.gui.wraps.WestSideStoryPanel import WestSideStoryPanel
from src.thatsawrap.data.wraps.Spartacus import Spartacus
from src.thatsawrap.gui.wraps.SpartacusPanel import SpartacusPanel
from src.thatsawrap.data.wraps.TheWizardOfOz import TheWizardOfOz
from src.thatsawrap.gui.wraps.TheWizardOfOzPanel import TheWizardOfOzPanel
from src.thatsawrap.data.wraps.SomeLikeItHot import SomeLikeItHot
from src.thatsawrap.gui.wraps.SomeLikeItHotPanel import SomeLikeItHotPanel
from src.thatsawrap.data.sides.Side import Side
from src.thatsawrap.gui.sides.SidePanel import SidePanel
from src.thatsawrap.data.drinks.ForrestGump import ForrestGump
from src.thatsawrap.gui.drinks.ForrestGumpPanel import ForrestGumpPanel
from src.thatsawrap.data.drinks.KingKong import KingKong
from src.thatsawrap.gui.drinks.KingKongPanel import KingKongPanel
from src.thatsawrap.data.drinks.SinginInTheRain import SinginInTheRain
from src.thatsawrap.gui.drinks.SinginInTheRainPanel import SinginInTheRainPanel
# from src.thatsawrap.gui.combo.ComboPanelFactory import ComboPanelFactory


class PanelFactory:
    """Panel Factory class.

    Builds Item panels according to
    string inputs.
    """
    @staticmethod
    def get_panel(window, str_name=None, item: Item = None, buttons: bool = True) -> object:
        """Get panel method.

        Builds and returns ItemPanels
        according to either string inputs
        or Item type object inputs.

        Args:
            str_name: A string corresponding
            to the type of panel to be returned.
            item: Alternative to str_name argument.
            Will return a panel corresponding to
            the Item provided as an argument.

        Returns:
            a Panel Object
        """
        if str_name is not None and item is None:
            if str_name == "The Godfather":
                return TheGodFatherPanel(master=window, buttons=buttons)
            elif str_name == "Spartacus":
                return SpartacusPanel(master=window, buttons=buttons)
            elif str_name == "Some Like it Hot":
                return SomeLikeItHotPanel(master=window, buttons=buttons)
            elif str_name == "The Wizard of Oz":
                return TheWizardOfOzPanel(master=window, buttons=buttons)
            elif str_name == "West Side Story":
                return WestSideStoryPanel(master=window, buttons=buttons)
            elif str_name == "Indie Forrest Gump":
                return ForrestGumpPanel(master=window, t=Size.INDIE,
                                        buttons=buttons)
            elif str_name == "Studio Forrest Gump":
                return ForrestGumpPanel(master=window, t=Size.STUDIO,
                                        buttons=buttons)
            elif str_name == "Blockbuster Forrest Gump":
                return ForrestGumpPanel(master=window, t=Size.BLOCKBUSTER,
                                        buttons=buttons)
            elif str_name == "Indie King Kong":
                return KingKongPanel(master=window, t=Size.INDIE,
                                     buttons=buttons)
            elif str_name == "Studio King Kong":
                return KingKongPanel(master=window, t=Size.STUDIO,
                                     buttons=buttons)
            elif str_name == "Blockbuster King Kong":
                return KingKongPanel(master=window, t=Size.BLOCKBUSTER,
                                     buttons=buttons)
            elif str_name == "Indie Singin' In The Rain":
                return SinginInTheRainPanel(master=window, t=Size.INDIE,
                                            buttons=buttons)
            elif str_name == "Studio Singin' In The Rain":
                return SinginInTheRainPanel(master=window, t=Size.STUDIO,
                                            buttons=buttons)
            elif str_name == "Blockbuster Singin' In The Rain":
                return SinginInTheRainPanel(master=window, t=Size.BLOCKBUSTER,
                                            buttons=buttons)
            elif (str_name == "Indie Snow White" or
                  str_name == "Studio Snow White" or
                  str_name == "Blockbuster Snow White" or
                  str_name == "Indie The French Connection" or
                  str_name == "Studio The French Connection" or
                  str_name == "Blockbuster The French Connection" or
                  str_name == "Indie Yankee Doodle Dandy" or
                  str_name == "Studio Yankee Doodle Dandy" or
                  str_name == "Blockbuster Yankee Doodle Dandy"):
                return SidePanel(master=window, side=str_name, buttons=buttons)
            else:
                print(str_name)
                print(str_name + "str_name")
                raise ValueError

        if item is not None:
            if isinstance(item, TheGodFather):
                return TheGodFatherPanel(master=window, item=item,
                                         buttons=buttons)
            elif isinstance(item, Spartacus):
                return SpartacusPanel(master=window, item=item,
                                      buttons=buttons)
            elif isinstance(item, SomeLikeItHot):
                return SomeLikeItHotPanel(master=window, item=item,
                                          buttons=buttons)
            elif isinstance(item, TheWizardOfOz):
                return TheWizardOfOzPanel(master=window, item=item,
                                          buttons=buttons)
            elif isinstance(item, WestSideStory):
                return WestSideStoryPanel(master=window, item=item,
                                          buttons=buttons)
            elif isinstance(item, ForrestGump):
                return ForrestGumpPanel(master=window, item=item,
                                        buttons=buttons)
            elif isinstance(item, KingKong):
                return KingKongPanel(master=window, item=item,
                                     buttons=buttons)
            elif isinstance(item, SinginInTheRain):
                return SinginInTheRainPanel(master=window, item=item,
                                            buttons=buttons)
            elif isinstance(item, Side):
                return SidePanel(window, item.name, item,
                                 buttons=buttons)
            else:
                print(str(item) + "item")
                raise ValueError
