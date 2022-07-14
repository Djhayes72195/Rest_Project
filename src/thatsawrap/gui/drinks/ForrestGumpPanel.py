"""The Forrest Gump drink Panel.

This file contains the code required to represent
the Forrest Gump in the GUI.

Author: Dustin Hayes djhayes@ksu.edu
Version 0.1
"""
import tkinter as tk
from tkinter import ttk
from src.thatsawrap.data.drinks.ForrestGump import ForrestGump
from src.thatsawrap.data.enums.Size import Size


class ForrestGumpPanel(tk.Frame):
    """The Forrest Gump Panel class.

    This class builds the representation of the Forrest Gump
    in our GUI.

    Author: Dustin Hayes djhayes@ksu.edu
    Version 0.1
    """
    def __init__(self, master, t: Size = Size.INDIE,
                 item: ForrestGump = None, buttons: bool = True) -> None:
        """The Forrest Gump Panel constructor.

        This constructor sets the state of our
        representation to match the state of
        the Forrest Gump object.  It makes
        use of the tkinter library to format
        the panel.

        Args:
            master: A reference to the PrimaryWindow
            or ComboPanel.
            t: A string used to set the size of the drink.
            item: Optional ForrestGump type object
            that will set the panel according to its
            parameters.
            buttons: Boolean value that indicates
            if the panel should be formatted as part
            of a Combo Panel.

        Author: Dustin Hayes djhayes@ksu.edu
        Version 0.1
        """
        self.__master = master
        tk.Frame.__init__(self, master=self.__master)

        if item is None:
            self._item = ForrestGump()
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
        size_combo.grid(row=1, column=1, padx=2, pady=2, sticky="NW")

        self._chocolate = tk.BooleanVar(value=bool(self._item.chocolate))
        chocolate = tk.Checkbutton(master=self, text="chocolate",
                                   variable=self._chocolate, onvalue=True,
                                   offvalue=False)
        chocolate.grid(row=2, column=1, padx=2, pady=2, sticky="NW")

        self._caramel = tk.BooleanVar(value=bool(self._item.caramel))
        caramel = tk.Checkbutton(master=self, text="caramel",
                                 variable=self._caramel, onvalue=True,
                                 offvalue=False)
        caramel.grid(row=3, column=1, padx=2, pady=2, sticky="NW")

        self._vanilla = tk.BooleanVar(value=bool(self._item.vanilla))
        vanilla = tk.Checkbutton(master=self, text="vanilla",
                                 variable=self._vanilla, onvalue=True,
                                 offvalue=False)
        vanilla.grid(row=4, column=1, padx=2, pady=2, sticky="NW")

        self._coffee = tk.BooleanVar(value=bool(self._item.coffee))
        coffee = tk.Checkbutton(master=self, text="coffee",
                                variable=self._coffee, onvalue=True,
                                offvalue=False)
        coffee.grid(row=5, column=1, padx=2, pady=2, sticky="NW")

        self.grid_rowconfigure(7, weight=1)

        if buttons:
            save = tk.Button(master=self, text="Save",
                            command=lambda: self.action_performed("save"))
            save.grid(row=6, column=1, sticky="NEW")

            self.grid_rowconfigure(7, weight=1)
            cancel = tk.Button(master=self, text="Cancel",
                            command=lambda:
                            self.action_performed("cancel"))
            cancel.grid(row=7, column=1, sticky="NEW")

    def action_performed(self, text: str, combo: bool = False):
        """Action performed method.

        This method is called when a button is
        pushed on our GUI to handle the event.

        Args:
            text: A string corresponding to the action
            performed.
        """
        print(text)
        if text == "save":
            self._item.size = Size(self._size.get())
            self._item.vanilla = self._vanilla.get()
            self._item.chocolate = self._chocolate.get()
            self._item.coffee = self._coffee.get()
            self._item.caramel = self._caramel.get()
            self.__master.save_item(self._item)
            if not combo:
                self.__master.load_menu_panel()
        elif text == "cancel":
            self.__master.load_menu_panel()
