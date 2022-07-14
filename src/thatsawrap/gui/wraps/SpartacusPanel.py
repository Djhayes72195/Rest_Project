"""The Some Like it Hot Panel.

This file contains the code required to represent
the Some Like it Hot Wrap panel in the GUI.

Author: Dustin Hayes djhayes@ksu.edu
Version 0.1
"""
import tkinter as tk
from tkinter import ttk
from src.thatsawrap.data.wraps.Spartacus import Spartacus
from src.thatsawrap.data.enums.Shell import Shell
from src.thatsawrap.data.enums.Addin import Addin


class SpartacusPanel(tk.Frame):
    """The Spartacus class.

    This class builds the representation of the
    Spartacus Panel in the GUI.

    Author: Dustin Hayes djhayes@ksu.edu
    Version 0.1
    """
    def __init__(self, master, item: Spartacus = None, buttons: bool = True) -> None:
        """The Spartacus Panel constructor.

        This constructor sets the state of our
        representation to match the state of
        the Spartacus object.  It makes
        use of the tkinter library to format
        the panel.  It also contains the logic
        to show the correct information for the wrap
        as passed in to the constructor.

        Args:
            master: A reference to the PrimaryWindow.

        Author: Dustin Hayes djhayes@ksu.edu
        Version 0.1
        """
        self.__master = master
        tk.Frame.__init__(self, master=self.__master)

        if item is None:
            self._item = Spartacus()
        else:
            self._item = item

        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(2, weight=1)

        title = tk.Label(master=self, text=self._item.name)
        title.grid(row=0, column=1, padx=2, pady=2, sticky="SEW")

        self._shell = tk.StringVar(value=str(self._item.shell))
        shell_combo = ttk.Combobox(master=self,
                                   textvariable=self._shell)
        shell_combo['values'] = [str(x) for x in Shell]
        shell_combo.grid(row=1, column=1, padx=2, pady=2, sticky="W")

        self._pepperoni = tk.BooleanVar(value=bool(self._item.pepperoni))
        pepperoni = tk.Checkbutton(master=self, text="Pepperoni",
                                   variable=self._pepperoni, onvalue=True,
                                   offvalue=False)
        pepperoni.grid(row=2, column=1, padx=2, pady=2, sticky="W")

        self._sausage = tk.BooleanVar(value=bool(self._item.sausage))
        sausage = tk.Checkbutton(master=self, text="Sausage",
                                 variable=self._sausage, onvalue=True,
                                 offvalue=False)
        sausage.grid(row=3, column=1, padx=2, pady=2, sticky="W")

        self._chicken = tk.BooleanVar(value=bool(self._item.chicken))
        chicken = tk.Checkbutton(master=self, text="Chicken",
                                 variable=self._chicken, onvalue=True,
                                 offvalue=False)
        chicken.grid(row=4, column=1, padx=2, pady=2, sticky="W")

        self._cheese = tk.BooleanVar(value=bool(self._item.cheese))
        cheese = tk.Checkbutton(master=self, text="Cheese",
                                variable=self._cheese, onvalue=True,
                                offvalue=False)
        cheese.grid(row=5, column=1, padx=2, pady=2, sticky="W")

        self._corned_beef = tk.BooleanVar(value=bool(self._item.corned_beef))
        corned_beef = tk.Checkbutton(master=self, text="Corned Beef",
                                     variable=self._corned_beef, onvalue=True,
                                     offvalue=False)
        corned_beef.grid(row=6, column=1, padx=2, pady=2, sticky="W")

        addlabel = tk.Label(master=self, text="Addins")
        addlabel.grid(row=7, column=1, padx=2, pady=2, sticky="EW")

        i = 8
        self._addins = dict()
        for a in Addin:
            self._addins[a] = tk.BooleanVar(value=(a in self._item.addins))
            check = tk.Checkbutton(master=self, text=str(a),
                                   variable=self._addins[a], onvalue=True,
                                   offvalue=False)
            check.grid(row=i, column=1, padx=2, pady=2, sticky="W")
            i += 1

        self.grid_rowconfigure(i, weight=1)
        
        if buttons:
            save = tk.Button(master=self, text="Save",
                            command=lambda: self.action_performed("save"))
            save.grid(row=i, column=1, sticky="SEW")
            i += 1

            self.grid_rowconfigure(i, weight=1)
            cancel = tk.Button(master=self, text="Cancel",
                            command=lambda:
                            self.action_performed("cancel"))
            cancel.grid(row=i, column=1, sticky="NEW")

    def action_performed(self, text: str, combo: bool = False) -> None:
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
            self._item.shell = Shell(self._shell.get())
            self._item.sausage = self._sausage.get()
            self._item.chicken = self._chicken.get()
            self._item.pepperoni = self._pepperoni.get()
            self._item.cheese = self._cheese.get()
            self._item.corned_beef = self._corned_beef.get()
            for a in Addin:
                if self._addins[a].get():
                    self._item.add_addin(a)
                else:
                    self._item.remove_addin(a)
            self.__master.save_item(self._item)
            if not combo:
                self.__master.load_menu_panel()
        elif text == "cancel":
            self.__master.load_menu_panel()
