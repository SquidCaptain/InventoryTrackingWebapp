from wtforms import Form, StringField, TextAreaField, IntegerField, DecimalField

class AddForm(Form):
    name = StringField("name")
    inventory = IntegerField("inventory")
    price = DecimalField("price")
    description = TextAreaField("description")

class DelForm(Form):
    id_num = IntegerField("id_num")