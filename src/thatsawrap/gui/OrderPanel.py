"""The Order Panel.

This file contains the code required to represent
the Order in the GUI.

Author: Dustin Hayes djhayes@ksu.edu
Version 0.1
"""
from tkinter import Frame, Button, Label
from tkinter.ttk import Treeview, Scrollbar
from typing import Dict

from src.thatsawrap.data.menu.Item import Item
from src.thatsawrap.gui.PanelFactory import PanelFactory
from src.thatsawrap.data.sides.Side import Side
from src.thatsawrap.data.order.Order import Order
from src.thatsawrap.data.order.Combo import Combo
from src.thatsawrap.gui.combo.ComboPanel import ComboPanel
from src.thatsawrap.data.wraps.Wrap import Wrap


class OrderPanel(Frame):
    """The Order Panel class.

    This class builds the representation of the
    order panel in the GUI.
    """
    def __init__(self, master) -> None:
        """The Order Panel constructor.

        This constructor builds the layout
        of our order panel, which contains
        labels corresponding to total, subtotal,
        order number, and tax.  It also includes
        an edit button and a blank frame.
        The functionality of these items will be
        implemented in a later update.
        The layout is formatted using
        the tkinter python library.

        Args:
            master: A reference to the PrimaryWindow.
        """
        self.__master = master
        self.__order: Order = Order()
        Frame.__init__(self, master=self.__master)
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(1, weight=1)

        order_label = Label(master=self, text="Order #")
        order_label.grid(row=0, column=0, sticky="E")

        self.__order_num = Label(master=self, text="000")
        self.__order_num.grid(row=0, column=1, padx=2, pady=2, sticky="W")

        self.__items: Dict[str, Item] = dict()
        list_frame = Frame(master=self)
        list_frame.grid_columnconfigure(0, weight=1)
        list_frame.grid_rowconfigure(0, weight=1)
        self.__order_list = Treeview(master=list_frame, show="tree",
                                     selectmode="browse")
        order_list_scrollbar = Scrollbar(master=list_frame, orient="vertical",
                                         command=self.__order_list.yview)
        self.__order_list.configure(yscrollcommand=order_list_scrollbar.set)
        self.__order_list.grid(row=0, column=0, sticky="NSEW")
        order_list_scrollbar.grid(row=0, column=1, sticky="NSE")
        list_frame.grid(row=1, column=0, columnspan=2, sticky="NSEW")

        edit = Button(master=self, text="Edit",
                      command=lambda:
                      self.action_performed("edit"))
        edit.grid(row=2, column=0, sticky="NSEW")

        new_order = Button(master=self, text="New Order",
                           command=lambda:
                           self.action_performed("new_order"))
        new_order.grid(row=3, column=0, sticky="NSEW")

        checkout = Button(master=self, text="Checkout",
                          command=lambda:
                          self.action_performed("checkout"))
        checkout.grid(row=3, column=1, sticky="NSEW")

        delete = Button(master=self, text="Delete",
                        command=lambda:
                        self.action_performed("delete"))
        delete.grid(row=2, column=1, sticky="NSEW")

        subtotal_label = Label(master=self, text="Subtotal $")
        subtotal_label.grid(row=4, column=0, sticky="E")

        self.__subtotal_price_label = Label(master=self, text="0.00")
        self.__subtotal_price_label.grid(row=4, column=1, sticky="W")

        tax_label = Label(master=self, text="Tax $")
        tax_label.grid(row=5, column=0, sticky="E")

        self.__tax_price_label = Label(master=self, text="0.00")
        self.__tax_price_label.grid(row=5, column=1, sticky="W")

        total_label = Label(master=self, text="Total $")
        total_label.grid(row=6, column=0, sticky="E")

        self.__total_price_label = Label(master=self, text="0.00")
        self.__total_price_label.grid(row=6, column=1, sticky="W")

    def action_performed(self, text: str) -> None:
        """Handles button actions.

        Will make the necesary actions when
        a button on the Order Panel is pressed.

        Args:
            text: Corresponds to the button
            that was pushed.
        """
        print(text)
        if text == "edit":
            node = self.__order_list.focus()
            if node:
                while node not in self.__items:
                    node = self.__order_list.parent(node)
                item: Item = self.__items[node]
                if isinstance(item, Side):
                    self.__master.load_panel(PanelFactory.get_panel(self.__master, item.name, item=item))
                elif isinstance(item, Combo):
                    self.__master.load_panel(ComboPanel(self.__master, item))
                else:
                    self.__master.load_panel(PanelFactory.get_panel(window=self.__master, item=item))
        elif text == "delete":
            node = self.__order_list.focus()
            if node:
                while node not in self.__items:
                    node = self.__order_list.parent(node)
                print(text)
                self.__order.remove_item(self.__items[node])
                del self.__items[node]
                self.__order_list.delete(node)
                self.__update_money()
        elif text == "new_order":
            self.__order = Order()
            self.__update_money()
            self.__items.clear()
            for item in self.__order_list.get_children():
                self.__order_list.delete(item)

    def save_item(self, item: Item) -> None:
        """Saves an item.

        Saves the item so that it will
        appear to the user.

        Args:
            item: The Item type object,
            representing a wrap, side
            or drink to be saved.
        """
        for item_id, value in self.__items.items():
            if item is value:
                self.__update_tree(item, item_id)
                return
        self.__items[self.__update_tree(item)] = item
        self.__order.add_item(item)
        self.__update_money()

    def __update_tree(self, item: Item, index: str = "end") -> str:
        """Update order.

        Updates the an item in
        the order, saved by a
        Treeview stucture in the GUI.

        Args:
            item: Item to be updated.
            index: string reference to the
            ID used to track items in the
            Treeview

        Returns:
            A string indicating the item
            to be updated.
        """
        if index == "end":
            if isinstance(item, Combo):
                index = self.__order_list.insert(parent="", index="end",
                                             text="Combo")
            else:
                index = self.__order_list.insert(parent="", index="end",
                                                text=str(item))
        else:
            if isinstance(item, Combo):
                self.__order_list.item(index, text=item.name)
            else:
                self.__order_list.item(index, text=str(item))
            for child in self.__order_list.get_children(index):
                self.__order_list.delete(child)
        self.__order_list.item(index, open=True)
        for line in item.instructions:
            self.__order_list.insert(parent=index, index="end",
                                     text=line)
        if isinstance(item, Combo):
            for order_item in item.items_in_combo:
                if isinstance(order_item, Wrap):
                    index2 = self.__order_list.insert(parent=index, index="end",
                                                      text=order_item.name)
                else:
                    index2 = self.__order_list.insert(parent=index, index="end",
                                             text=str(order_item))
                self.__order_list.item(index2, open=True)
                for instruction in order_item.instructions:
                    self.__order_list.insert(parent=index2, index="end",
                                             text=order_item.instructions)
        return index
# do what you are currently doing first, then

# if item is a combo:

    # for each order_item in the combo:

        # new_index = insert new item to tree using index as parent that contains order_item name

        # set that new tree item to be open

        # for each special instruction in order_item:

            # insert new item to tree using new_index as parent

    def __update_money(self) -> None:
        """Update money.

        Updates the tax, subtotal
        and total labels in the GUI.
        """
        self.__subtotal_price_label['text'] = \
        "${:,.2f}".format(self.__order.subtotal)
        self.__total_price_label['text'] = \
        "${:,.2f}".format(self.__order.total)
        self.__tax_price_label['text'] = \
        "${:,.2f}".format(self.__order.tax)
