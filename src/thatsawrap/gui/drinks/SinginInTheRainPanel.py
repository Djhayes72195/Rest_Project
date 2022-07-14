"""The Singin' in the Rain drink Panel.

This file contains the code required to represent
the Singin' in the Rain in the GUI.

Author: Dustin Hayes djhayes@ksu.edu
Version 0.1
"""
import tkinter as tk
from tkinter import ttk
from src.thatsawrap.data.drinks.SinginInTheRain import SinginInTheRain
from src.thatsawrap.data.enums.Size import Size


class SinginInTheRainPanel(tk.Frame):
    """The Singin' in the Rain Panel class.

    This class builds the representation of the Singin'
    in the Rain in our GUI.

    Author: Dustin Hayes djhayes@ksu.edu
    Version 0.1
    """
    def __init__(self, master, t=Size.INDIE,
                 item: SinginInTheRain = None,
                 buttons: bool = True) -> None:
        """The Singin' in the Rain Panel constructor.

        This constructor sets the state of our
        representation to match the state of
        the Singin' in the Rain object.  It makes
        use of the tkinter library to format
        the panel.

        Args:
            master: A reference to the PrimaryWindow.
            t: a string used to indicate the size of the drink.

        Author: Dustin Hayes djhayes@ksu.edu
        Version 0.1
        """
        self.__master = master
        tk.Frame.__init__(self, master=self.__master)

        if item is None:
            self._item = SinginInTheRain()
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

        self._cherry = tk.BooleanVar(value=bool(self._item.cherry))
        cherry = tk.Checkbutton(master=self, text="cherry",
                                variable=self._cherry, onvalue=True,
                                offvalue=False)
        cherry.grid(row=2, column=1, padx=2, pady=2, sticky="W")

        self._cola = tk.BooleanVar(value=bool(self._item.cola))
        cola = tk.Checkbutton(master=self, text="cola",
                              variable=self._cola, onvalue=True,
                              offvalue=False)
        cola.grid(row=3, column=1, padx=2, pady=2, sticky="W")

        self._strawberry = tk.BooleanVar(value=bool(self._item.strawberry))
        strawberry = tk.Checkbutton(master=self, text="strawberry",
                                    variable=self._strawberry, onvalue=True,
                                    offvalue=False)
        strawberry.grid(row=4, column=1, padx=2, pady=2, sticky="W")

        self._grape = tk.BooleanVar(value=bool(self._item.grape))
        grape = tk.Checkbutton(master=self, text="grape",
                               variable=self._grape, onvalue=True,
                               offvalue=False)
        grape.grid(row=5, column=1, padx=2, pady=2, sticky="W")

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
            self._item.cherry = self._cherry.get()
            self._item.cola = self._cola.get()
            self._item.strawberry = self._strawberry.get()
            self._item.grape = self._grape.get()
            self.__master.save_item(self._item)
            if not combo:
                self.__master.load_menu_panel()
        elif text == "cancel":
            self.__master.load_menu_panel()
