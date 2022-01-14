from wtforms import Form, StringField, TextAreaField, IntegerField, DecimalField

class MyForm(Form):
    name = StringField("name")
    inventory = IntegerField("inventory")
    price = DecimalField("price")
    description = TextAreaField("description")

class IDForm(Form):
    id_num = IntegerField("id_num")

class SearchForm(Form):
    search = StringField("search")