"""Menu controller file.

This file contains the code to send the appropriate
data to our web application when the site is interacted
with.

Author: Dustin Hayes djhayes@ksu.edu
Version 0.1
"""
from flask import render_template, request
from flask_classful import FlaskView, route  # type: ignore
from src.thatsawrap.data.menu.Menu import Menu
from typing import List
from src.thatsawrap.data.order.Combo import Combo
from src.thatsawrap.data.menu.Item import Item


class MenuController(FlaskView):
    """Menu controller class.

    This class contains the code to send the appropriate
    data and to our web application when the site
    is interacted with.  Sends the data to html files
    which do the work of generating the pages.
    """

    route_base = "/"

    @route('/')
    def index(self):
        """Index page action.

        Called when the homepage link is clicked on the
        webpage, or when the website is first opened and 
        renders index.html.

        Returns:
            The rendered index template.
        """
        return render_template("index.html")

    @route('/menu/')
    def menu(self):
        """Menu page action.

        Called when the homepage link is clicked on and 
        renders the menu template.  

        Returns:
            The rendered menu template, containing the appropriate
            data generated from the Menu class.
        """
        menu = Menu()
        combo = Combo()
        discount = combo.get_discount()
        return render_template("menu.html",
                               wraps=menu.wraps(),
                               drinks=menu.parsed_drinks(),
                               sides=menu.parsed_sides(),
                               combos=menu.combos(),
                               discount=discount)

    @route('/about/')
    def about(self):
        """About page action.

        Called when the about link is clicked on and 
        renders the menu template.  

        Returns:
            The rendered about template.
        """
        return render_template("about.html")

    @route('/search/', methods=['GET'])
    def simple_search(self):
        return render_template(
            "search.html")

    @route('/search/', methods=['POST'])
    def simple_search_results(self):
        text: str = request.form.get('text', None)
        items: List[Item] = Menu.fullmenu()
        items = Menu.filter_keywords(items, text)
        return render_template(
            "search.html",
            text=text,
            items=items)

    @route('/advancedsearch/', methods=['GET'])
    def search(self):
        return render_template("advanced_search.html")

    @route('/advancedsearch/', methods=['POST'])
    def search_results(self):
        text: str = request.form.get('text', None)
        wraps: bool = request.form.get('wraps', False)
        drinks: bool = request.form.get('drinks', False)
        sides: bool = request.form.get('sides', False)
        combos: bool = request.form.get('combos', False)
        try:
            caloriesmin: int = int(request.form.get('caloriesmin', "-1"))
        except Exception:
            caloriesmin = -1
        try:
            caloriesmax: int = int(request.form.get('caloriesmax', "-1"))
        except Exception:
            caloriesmax = -1
        try:
            pricemin: float = float(request.form.get('pricemin', "-1"))
        except Exception:
            pricemin = -1
        try:
            pricemax: float = float(request.form.get('pricemax', "-1"))
        except Exception:
            pricemax = -1
        items: List[Item] = Menu.fullmenu()
        items = Menu.filter_keywords(items, text)
        items = Menu.filter_type_of_item(wraps, drinks,
                                               sides, combos,
                                               items)
        items = Menu.filter_calories(items, caloriesmin,
                                           caloriesmax)
        items = Menu.filter_price(items, pricemin,
                                        pricemax)
        if len(items) != 0:
            search_success = True
        else:
            search_success = False
        return render_template(
            "advanced_search.html",
            text=text,
            wraps=wraps,
            drinks=drinks,
            sides=sides,
            combos=combos,
            items=items,
            caloriesmin=("" if caloriesmin < 0 else caloriesmin),
            caloriesmax=("" if caloriesmax < 0 else caloriesmax),
            pricemin=("" if pricemin < 0 else pricemin),
            pricemax=("" if pricemax < 0 else pricemax),
            search_success=search_success)