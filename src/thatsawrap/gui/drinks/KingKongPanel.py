"""The King Kong drink Panel.

This file contains the code required to represent
the King Kong in the GUI.

Author: Dustin Hayes djhayes@ksu.edu
Version 0.1
"""
import tkinter as tk
from tkinter import ttk
from src.thatsawrap.data.drinks.KingKong import KingKong
from src.thatsawrap.data.enums.Size import Size


class KingKongPanel(tk.Frame):
    """The King Kong Panel class.

    This class builds the representation of the King Kong
    in our GUI.

    Author: Dustin Hayes djhayes@ksu.edu
    Version 0.1
    """
    def __init__(self, master, t=Size.INDIE,
                 item: KingKong = None, buttons: bool = True) -> None:
        """The King Kong Panel constructor.

        This constructor sets the state of our
        representation to match the state of
        the King Kong object.  It makes
        use of the tkinter library to format
        the panel.

        Args:
            master: A reference to the PrimaryWindow
            t: A string used to set the size of the drink.

        Author: Dustin Hayes djhayes@ksu.edu
        Version 0.1
        """
        self.__master = master
        tk.Frame.__init__(self, master=self.__master)

        if item is None:
            self._item = KingKong()
            self._item.size = t
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

        self._banana = tk.BooleanVar(value=bool(self._item.banana))
        banana = tk.Checkbutton(master=self, text="banana",
                                variable=self._banana, onvalue=True,
                                offvalue=False)
        banana.grid(row=2, column=1, padx=2, pady=2, sticky="W")

        self._strawberry = tk.BooleanVar(value=bool(self._item.strawberry))
        strawberry = tk.Checkbutton(master=self, text="strawberry",
                                    variable=self._strawberry, onvalue=True,
                                    offvalue=False)
        strawberry.grid(row=3, column=1, padx=2, pady=2, sticky="W")

        self._peach = tk.BooleanVar(value=bool(self._item.peach))
        peach = tk.Checkbutton(master=self, text="peach",
                               variable=self._peach, onvalue=True,
                               offvalue=False)
        peach.grid(row=4, column=1, padx=2, pady=2, sticky="W")

        self._mango = tk.BooleanVar(value=bool(self._item.mango))
        mango = tk.Checkbutton(master=self, text="mango",
                               variable=self._mango, onvalue=True,
                               offvalue=False)
        mango.grid(row=5, column=1, padx=2, pady=2, sticky="W")

        self.grid_rowconfigure(7, weight=1)

        if buttons:
            save = tk.Button(master=self, text="Save",
                            command=lambda: self.action_performed("save"))
            save.grid(row=6, column=1, sticky="NEW")

            cancel = tk.Button(master=self, text="Cancel",
                            command=lambda:
                            self.action_performed("cancel"))
            cancel.grid(row=7, column=1, sticky="NEW")

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
            self._item.banana = self._banana.get()
            self._item.strawberry = self._strawberry.get()
            self._item.mango = self._mango.get()
            self._item.peach = self._peach.get()
            self.__master.save_item(self._item)
            if not combo:
                self.__master.load_menu_panel()
        elif text == "cancel":
            self.__master.load_menu_panel()
