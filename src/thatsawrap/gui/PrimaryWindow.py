"""The Primary Window.

This file contains the code required to represent
the Primary Window in the GUI.

Author: Dustin Hayes djhayes@ksu.edu
Version 0.1
"""
import tkinter as tk
from src.thatsawrap.gui.OrderPanel import OrderPanel
from src.thatsawrap.gui.MenuPanel import MenuPanel
from src.thatsawrap.data.menu.Item import Item


class PrimaryWindow(tk.Tk):
    """The Primary Window class.

    This class builds the representation of order
    Panel in the GUI.

    Author: Dustin Hayes djhayes@ksu.edu
    Version 0.1
    """
    def __init__(self) -> None:
        """The Primary Window constructor.

        This constructor builds the layout
        of our primary window, which will contain
        both the order panel and menu panel.
        The layout is formatted using
        the tkinter python library.

        Author: Dustin Hayes djhayes@ksu.edu
        Version 0.1
        """
        tk.Tk.__init__(self)
        self.minsize(width=1024, height=740)
        self.title("That's a Wrap")

        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=5)
        self.grid_columnconfigure(1, weight=2)

        self.__main = None
        self.load_menu_panel()

        self.__order = OrderPanel(self)
        self.__order.grid(row=0, column=1, padx=10, pady=10, sticky="NSEW")

    def load_menu_panel(self):
        """Load menu method.

        This method loads an instance of
        the menu panel to be displayed in the
        primary window.
        """
        self.load_panel(MenuPanel(self))

    def load_panel(self, panel):
        """Load panel method.

        This method destroys the current
        panel if there is one and replaces it
        with the argument passed to this method.

        Args:
            panel: A panel object that will
            be displayed by this method.
        """
        if self.__main is not None:
            self.__main.destroy()
        self.__main = panel
        self.__main.grid(row=0, column=0, padx=10, pady=10, sticky="NSEW")

    def save_item(self, item: Item) -> None:
        """Save item.

        Calls the save item method in
        the order panel.

        Args:
            item: Reference to item
            to be saved in the order
            panel class.
        """
        self.__order.save_item(item)
