"""The Menu Panel.

This file contains the code required to represent
the Menu in the GUI.

Author: Dustin Hayes djhayes@ksu.edu
Version 0.1
"""
import tkinter as tk
from src.thatsawrap.data.menu.Menu import Menu
from src.thatsawrap.gui.PanelFactory import PanelFactory
from src.thatsawrap.gui.combo.ComboPanelFactory import ComboPanelFactory


class MenuPanel(tk.Frame):
    """The Menu Panel class.

    This class builds the representation of Menu
    Panel in the GUI.

    Author: Dustin Hayes djhayes@ksu.edu
    Version 0.1
    """
    def __init__(self, master) -> None:
        """The Menu Panel constructor.

        This constructor builds the layout
        of our menu panel, which contains
        buttons for each of our wraps, sides and
        drinks.  The layout is formatted using
        the tkinter python library.

        Args:
            master: A reference to the PrimaryWindow.

        Author: Dustin Hayes djhayes@ksu.edu
        Version 0.1
        """
        self.__master = master
        tk.Frame.__init__(self, master=self.__master)
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure(2, weight=1)

        i = 0
        j = 0
        k = 0
        for wrap in Menu.wraps():
            self.grid_rowconfigure(i, weight=1)
            button = tk.Button(master=self, text=wrap.name,
                               command=lambda x=wrap.name:
                               self.action_performed(x))
            button.grid(row=i, column=0, padx=2, pady=2, sticky="NSEW")
            i += 1

        for combo in Menu.combos():
            self.grid_rowconfigure(i, weight=1)
            button = tk.Button(master=self, text=combo.name,
                               command=lambda x=combo.name:
                               self.action_performed(x))
            button.grid(row=i, column=0, padx=2, pady=2, sticky="NSEW")
            i += 1

        self.grid_rowconfigure(i, weight=1)
        button = tk.Button(master=self, text="Custom Combo",
                           command=lambda x="Custom Combo":
                           self.action_performed(x))
        button.grid(row=i, column=1, padx=2, pady=2, sticky="NSEW")


        for side in Menu.sides():
            self.grid_rowconfigure(j, weight=1)
            button = tk.Button(master=self, text=str(side),
                               command=lambda x=str(side):
                               self.action_performed(x))
            button.grid(row=j, column=1, padx=2, pady=2, sticky="NSEW")
            j += 1

        for drink in Menu.drinks():
            self.grid_rowconfigure(k, weight=1)
            button = tk.Button(master=self, text=str(drink),
                               command=lambda x=str(drink):
                               self.action_performed(x))
            button.grid(row=k, column=2, padx=2, pady=2, sticky="NSEW")
            k += 1

    def action_performed(self, text: str) -> None:
        """Action performed method.

        This method is called when a button is
        pushed menu panel.  If a button corresponding
        to a menu item is pushed, this method will load
        the appropriate panel.

        Args:
            text: A string corresponding to the action
            performed.
        """
        if text not in ["Classic", "Hungry",
                        "Spicy", "Green",
                        "Custom Combo"]:
            print(text)
            pan_fac = PanelFactory()
            self.__master.load_panel(pan_fac.get_panel(window=self.__master,
                                                    str_name=text))
        else:
            print(text)
            pan_fac = ComboPanelFactory()
            self.__master.load_panel(pan_fac.get_panel(
                                     window=self.__master,
                                     str_name=text))
