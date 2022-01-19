from curses import is_term_resized
from wtforms import Form, StringField, TextAreaField, IntegerField, DecimalField, validators
from wtforms.validators import NumberRange

## These are Form objects from wtforms used to implement forms in webapp

## MyForm() this is used to collect all information of the item from the user
class MyForm(Form):
    name = StringField("name")
    inventory = IntegerField("inventory", validators=[NumberRange(min=0)])
    price = DecimalField("price", validators=[NumberRange(min=0)])
    description = TextAreaField("description")

## IDForm() this is used to collect ID from the user so specific item can be found
class IDForm(Form):
    id_num = IntegerField("id_num", validators=[NumberRange(min=1)])

## SearchForm() this is used to collect input from the user so specific item can be found
class SearchForm(Form):
    search = StringField("search")
    
## ShipmentForm() this is used to specify inventory for shipment
class ShipmentForm(Form):
    item_id = IntegerField("item_id", validators=[NumberRange(min=1)])
    inventory = IntegerField("inventory", validators=[NumberRange(min=0)])