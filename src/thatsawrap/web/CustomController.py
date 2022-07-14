"""Custom controller file.

This file contains the code to send the appropriate
data to our web application when the site is interacted
with.

Author: Dustin Hayes djhayes@ksu.edu
Version 0.1
"""
from flask import render_template, redirect
from flask_classful import FlaskView, route  # type: ignore
from src.thatsawrap.data.custom.CustomItem import CustomItem
from src.thatsawrap.data.custom.CustomItemList import CustomItemList
from src.thatsawrap.web.CustomForm import CustomForm


class CustomController(FlaskView):
    """Custom controller class.

    This class contains the code to send the appropriate
    data and to our web application when the site
    is interacted with. Deals specificaly with requests
    about custom items.
    """
    route_base = "/custom/"

    @route('/', methods=['GET'])
    def show_custom_items(self):
        """Show custom items.

        Called when the custom items link on the homepage
        is clicked; Tells the application to render
        the html file which shows the user
        all custom items.
        """
        c_item_list = CustomItemList()
        return render_template("customitems.html",
                               items=c_item_list)

    @route('/new/', methods=['GET'])
    def new_custom_item(self):
        """New custom item.

        Called when the user creates a new item;
        Renders a form for the user to fill out.
        """
        c_item = CustomItem(name="custom",
                            price=0.0,
                            calories=0)
        form = CustomForm(obj=c_item)
        return render_template("newcustomitem.html",
                               form=form)

    @route('/new/', methods=['POST'])
    def custom_items(self):
        """New custom item.

        Called when the user saves a new
        item; Sets the new object in the
        CustomItem list and redirects the user
        to the page that shows all custom
        items.
        """
        form = CustomForm()
        if not form.validate_on_submit():
            return render_template("newcustomitem.html",
                                   form=form,
                                   id=id)
        c_item_list = CustomItemList()
        c_item = CustomItem(name=form.name.data,
                            price=form.price.data,
                            calories=form.calories.data)
        c_item_list.__setitem__(c_item)
        return redirect('/custom/')

    @route('/<id>/', methods=['GET'])
    def single_custom_item(self, id: int):
        """Single custom item.

        Called when the user attempts to change
        an existing item; Displays the data
        for the single item the user is attempting
        to either modify or delete.

        Args:
            id: The id of the object that the
            user wants to modify.
        """
        c_item_list = CustomItemList()
        item = c_item_list[int(id)]
        return render_template("singlecustomitem.html",
                               item=item,
                               id=id)

    @route('/<id>/edit/', methods=['GET'])
    def edit_custom_item(self, id):
        """Edit single item.

        Called when the user edits
        a custom item; Returns a
        form that the user will fill out.

        Args:
            id: The id of the object that the
            user wants to modify.
        """
        print("asifhjaosiduyfhai")
        c_item_list = CustomItemList()
        c_item = c_item_list[int(id)]
        print("Id is")
        print(id)
        form = CustomForm(obj=c_item)
        return render_template("editcustomitem.html",
                               form=form,
                               id=id)

    @route('/<id>/', methods=['POST'])
    def edit(self, id: int):
        """Edit single item.

        Called when the user saves an
        edited item; will change the item
        accordingly in the CustomItemList
        and then redirect the user to the
        root custom item page.

        Args:
            id: The id of the object that the
            user wants to modify.
        """
        print('222222')
        form = CustomForm()
        print(form.name.errors)
        if not form.validate_on_submit():
            return render_template("editcustomitem.html",
                                   form=form,
                                   id=id)
        c_item_list = CustomItemList()
        c_item = CustomItem(name=form.name.data,
                            price=form.price.data,
                            calories=form.calories.data)
        print("id is")
        print(id)
        print(c_item)
        c_item_list.update_item(index=int(id),
                                item=c_item)
        return redirect('/custom/')

    @route('/<id>/delete/', methods=['GET'])
    def delete_custom_item(self, id):
        """Delete single item.

        Called when the user deletes
        a custom item; Returns a
        page where the user verifies that
        they want to delete the item, or cancels
        if they change their mind.

        Args:
            id: The id of the object that the
            user wants to delete.
        """
        c_item_list = CustomItemList()
        item = c_item_list[int(id)]
        return render_template("deletecustomitem.html",
                               item=item,
                               id=id)

    @route('/<id>/delete/', methods=['POST'])
    def delete(self, id):
        """Delete single item.

        Called when the user deletes
        a custom item after confirmation;
        Will remove the item from the
        CustomItemList and return the user
        to the page that lists all custom items.

        Args:
            id: The id of the object that the
            user wants to delete.
        """
        c_item_list = CustomItemList()
        c_item_list.__delitem__(index=int(id))
        return redirect('/custom/')

    @route('/save/', methods=['POST'])
    def save(self):
        """route to save custom items."""
        CustomItemList().save()
        return redirect('/custom/')