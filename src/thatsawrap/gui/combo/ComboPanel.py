"""The Combo Panel.

This file contains the code required to represent
the Combos in the GUI.

Author: Dustin Hayes djhayes@ksu.edu
Version 0.1
"""
from src.thatsawrap.data.order.Combo import Combo
from src.thatsawrap.gui.PanelFactory import PanelFactory
from src.thatsawrap.data.drinks.Drink import Drink
from src.thatsawrap.data.sides.Side import Side
from src.thatsawrap.data.wraps.Wrap import Wrap
from src.thatsawrap.data.menu.Item import Item
import tkinter as tk
from tkinter import ttk


class ComboPanel(tk.Frame):
    """The Forrest Gump Panel class.

    This class builds the representation of a Combo
    in our GUI.
    """
    def __init__(self, master, item: Combo):
        """The Combo Panel constructor.

        This constructor sets the state of our
        representation to match the state of
        the Combo.  It makes
        use of the tkinter library to format
        the panel, and to allow the user to change
        the combo.

        Args:
            master: A reference to the PrimaryWindow
            item: Combo type object which sets
            the state of the ComboPanel according to
            its parameters.

        Author: Dustin Hayes djhayes@ksu.edu
        Version 0.1
        """
        self.__master = master
        tk.Frame.__init__(self, master=self.__master)
        
        self._combo = item
        self.__index_compare = 0

        self.grid_rowconfigure(1, weight=1)
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure(2, weight=1)

        if self._combo.wrap is not None:
            self._wrap_panel = PanelFactory().get_panel(window=self,
                                                        item=self._combo.wrap,
                                                        buttons=False)
            self._wrap_panel.grid(row=1, column=0, padx=2, pady=2, sticky="SNEW")
            self._wrap = tk.StringVar(value=self._combo.wrap.name)
        else:
            self._wrap_panel = None
            self._wrap = tk.StringVar(value="No Wrap")

        if self._combo.side is not None:
            self._side_panel = PanelFactory().get_panel(window=self,
                                                        item=self._combo.side,
                                                        buttons=False)
            
            self._side_panel.grid(row=1, column=1, padx=2, pady=2, sticky="SNWE")
            self._side = tk.StringVar(value=self._combo.side.name)
        else:
            self._side_panel = None
            self._side = tk.StringVar(value="No Side")

        if self._combo.drink is not None:
            self._drink_panel = PanelFactory().get_panel(window=self,
                                                        item=self._combo.drink,
                                                        buttons=False)
            self._drink_panel.grid(row=1, column=2, padx=2, pady=2, sticky="SNWE")
            self._drink = tk.StringVar(value=self._combo.drink.name)
        else:
            self._drink_panel = None
            self._drink = tk.StringVar(value="No Drink")

        combo_wrap = ttk.Combobox(master=self,
                                  textvariable=self._wrap)
        combo_wrap['values'] = ["The Godfather", "West Side Story",
                                "Some Like it Hot", "The Wizard of Oz",
                                "Spartacus", "No Wrap"]
        combo_wrap.grid(row=0, column=0, padx=2, pady=2, sticky="NEW")

        combo_side = ttk.Combobox(master=self,
                                  textvariable=self._side) 
        combo_side['values'] = ["The French Connection",
                                "Snow White",
                                "Yankee Doodle Dandy",
                                "No Side"]    
        combo_side.grid(row=0, column=1, padx=2, pady=2, sticky="NEW")

        combo_drink = ttk.Combobox(master=self,
                                   textvariable=self._drink)
        combo_drink['values'] = ["Forrest Gump", "King Kong",
                                 "Singin' In The Rain",
                                 "No Drink"]
        combo_drink.grid(row=0, column=2, padx=2, pady=2, sticky="NEW")

        combo_wrap.bind('<<ComboboxSelected>>', self.wrap_changed)
        combo_drink.bind('<<ComboboxSelected>>', self.drink_changed)
        combo_side.bind('<<ComboboxSelected>>', self.side_changed)

        save = tk.Button(master=self, text="Save",
                            command=lambda: self.action_performed("save"))
        save.grid(row=2, column=1, sticky="SEW")


        self.grid_rowconfigure(2, weight=1)
        
        cancel = tk.Button(master=self, text="Cancel",
                           command=lambda:
                           self.action_performed("cancel"))
        cancel.grid(row=3, column=1, sticky="NEW")

    def action_performed(self, text: str) -> None:
        """Action performed method.

        This method is called when a button is
        pushed on our GUI to handle the event.

        Args:
            text: A string corresponding to the action
            performed.
        """
        if text == "save":
            if self._wrap.get() != "No Wrap":
                self._wrap_panel.action_performed(text=text, combo=True)
            else:
                self._combo.wrap = None
            if self._side.get() != "No Side":
                self._side_panel.action_performed(text=text, combo=True)
            else:
                self._combo.side = None
            if self._drink.get() != "No Drink":
                self._drink_panel.action_performed(text=text, combo=True)
            else:
                self._combo.drink = None
            self.save_item_to_order(self._combo)
            self.__master.load_menu_panel()
        elif text == "cancel":
            self.__master.load_menu_panel()

    def wrap_changed(self, event) -> None:
        """Wrap changed method.

        This method is called when the user
        interacts with the wrap combobox.
        It will change the wrap panel to the
        user's selection.

        Args:
            event: Reference to the tkinter
            event to be handled.
        """
        if self._wrap_panel is not None:
            self._wrap_panel.destroy()
        wrap_name: str = self._wrap.get()
        if wrap_name != "No Wrap":
            self._wrap_panel = PanelFactory().get_panel(window=self,
                                                        str_name=wrap_name,
                                                        buttons=False)
            self._wrap_panel.grid(row=1, column=0, padx=2, pady=2, sticky="SNEW")

    def drink_changed(self, event) -> None:
        """Drink changed method.

        This method is called when the user
        interacts with the drink combobox.
        It will change the drink panel to the
        user's selection.

        Args:
            event: Reference to the tkinter
            event to be handled.
        """
        if self._drink_panel is not None:
            self._drink_panel.destroy()
        drink_name: str = self._drink.get()
        if drink_name != "No Drink":
            self._drink_panel = PanelFactory().get_panel(window=self,
                                                        str_name="Indie " + drink_name,
                                                        buttons=False)
            self._drink_panel.grid(row=1, column=2, padx=2, pady=2, sticky="SNWE")

    def side_changed(self, event) -> None:
        """Side changed method.

        This method is called when the user
        interacts with the side combobox.
        It will change the side panel to the
        user's selection.

        Args:
            event: Reference to the tkinter
            event to be handled.
        """
        if self._side_panel is not None:
            self._side_panel.destroy()
        side_name: str = self._side.get()
        if side_name != "No Drink":
            self._side_panel = PanelFactory().get_panel(window=self,
                                                        str_name="Indie " + side_name,
                                                        buttons=False)
            self._side_panel.grid(row=1, column=1, padx=2, pady=2, sticky="SNWE")

    def save_item(self, item: Item) -> None:
        """Save item method.

        Updates the Combo according to the user's
        selection.

        Args:
            item: Item type object to be added
            to the combo.
        """
        if isinstance(item, Wrap):
            self._combo.wrap = item
        if isinstance(item, Drink):
            self._combo.drink = item
        if isinstance(item, Side):
            self._combo.side = item

    def save_item_to_order(self, item: Combo):
        """Save item to order method.

        Saves the updated combo according to
        the user's selection to the order sidebar.

        Args:
            item: The updated combo item.
        """
        self.__master.save_item(item)
