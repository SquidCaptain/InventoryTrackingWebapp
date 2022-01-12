from wtforms import Form, StringField, TextAreaField, IntegerField, FloatField

class AddForm(Form):
    name = StringField("name")
    inventory = IntegerField("inventory")
    price = FloatField("price")
    description = TextAreaField("description")

class DelForm(Form):
    id_num = IntegerField("id_num")