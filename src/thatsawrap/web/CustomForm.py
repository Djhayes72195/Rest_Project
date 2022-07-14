from flask_wtf import FlaskForm  # type: ignore
from wtforms import (StringField, IntegerField, DecimalField,  # type: ignore
                     validators)  # type: ignore
from wtforms.widgets import NumberInput  # type: ignore
import decimal


class CustomForm(FlaskForm):

    name = StringField("Name", [validators.length(min=4)])
    price = DecimalField("Price",
                         [validators.NumberRange(min=1.5, max=30)],
                         default=0, 
                         places=2,
                         rounding=decimal.ROUND_HALF_UP,
                         widget=NumberInput(min=1.5, max=30,
                         step=.01))
    calories = IntegerField("Calories",
                            [validators.NumberRange(min=250, max=4000)],
                            default=0,
                            widget=NumberInput(
                            min=250, max=4000, step=1))

