"""The Side Panel.

This file contains the code required to represent
the sides in the GUI.

Author: Dustin Hayes djhayes@ksu.edu
Version 0.1
"""
import tkinter as tk
from tkinter import ttk
from src.thatsawrap.data.enums.Size import Size
from src.thatsawrap.data.sides.Side import Side
from src.thatsawrap.data.sides.SnowWhite import SnowWhite
from src.thatsawrap.data.sides.TheFrenchConnection import TheFrenchConnection
from src.thatsawrap.data.sides.YankeeDoodleDandy import YankeeDoodleDandy


class SidePanel(tk.Frame):
    """The Side Panel class.

    This class builds the representation of the each
    side in our GUI.
    """
    def __init__(self, master, side: str, item: Side = None, buttons: bool = True) -> None:
        """The Side Panel constructor.

        This constructor sets the state of our
        representation to match the state of
        the Side object.  It makes
        use of the tkinter library to format
        the panel.  It also contains the logic
        to show the correct information for the side
        passed in to the constructor.

        Args:
            master: A reference to the PrimaryWindow.
            side: A string corresponding to the side.
            item: Reference to item that was used
            to set the state of the class at instantiation.
        """
        self.__master = master
        tk.Frame.__init__(self, master=self.__master)
        self.__side = side

        if item is None:
            if side == "Indie Snow White":
                self._item = SnowWhite()
            if side == "Studio Snow White":
                self._item = SnowWhite()
                self._item.size = Size.STUDIO
            if side == "Blockbuster Snow White":
                self._item = SnowWhite()
                self._item.size = Size.BLOCKBUSTER
            if side == "Indie Yankee Doodle Dandy":
                self._item = YankeeDoodleDandy()
            if side == "Studio Yankee Doodle Dandy":
                self._item = YankeeDoodleDandy()
                self._item.size = Size.STUDIO
            if side == "Blockbuster Yankee Doodle Dandy":
                self._item = YankeeDoodleDandy()
                self._item.size = Size.BLOCKBUSTER
            if side == "Indie The French Connection":
                self._item = TheFrenchConnection()
            if side == "Studio The French Connection":
                self._item = TheFrenchConnection()
                self._item.size = Size.STUDIO
            if side == "Blockbuster The French Connection":
                self._item = TheFrenchConnection()
                self._item.size = Size.BLOCKBUSTER
        else:
            self._item = item

        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(2, weight=1)

        title = tk.Label(master=self, text=self._item.name)
        title.grid(row=0, column=1, padx=2, pady=2, sticky="SEW")

        self._size = tk.StringVar(value=str(self._item.size))
        size_combo = ttk.Combobox(master=self,
                                  textvariable=self._size)
        size_combo['values'] = [str(x) for x in Size]
        size_combo.grid(row=1, column=1, padx=2, pady=2, sticky="W")

        self.grid_rowconfigure(3, weight=1)
        
        if buttons:
            save = tk.Button(master=self, text="Save",
                            command=lambda: self.action_performed("save"))
            save.grid(row=2, column=1, sticky="NEW")

            
            cancel = tk.Button(master=self, text="Cancel",
                            command=lambda:
                            self.action_performed("cancel"))
            cancel.grid(row=3, column=1, sticky="NEW")

    def action_performed(self, text, combo: bool = False):
        """Action performed method.

        This method is called when a button is
        pushed on our GUI.  If the save button is
        pushed, this method is called and will
        return the user to the primary window.

        Args:
            text: A string corresponding to the action
            performed.
        """
        print(text)
        if text == "save":
            self._item.size = Size(self._size.get())
            self.__master.save_item(self._item)
            if not combo:
                self.__master.load_menu_panel()
        elif text == "cancel":
            self.__master.load_menu_panel()
