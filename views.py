from flask import Flask, render_template, request, redirect, url_for

from app import app, db
from models import Item, Shipment
from forms import MyForm, IDForm, SearchForm


## --Globals--
##items = Item.query.all()

## --Routes--
## Home page
@app.route("/", methods=['POST', 'GET'])
@app.route("/home", methods=['POST', 'GET'])
def home_page():
    form = IDForm()
    if request.method == 'POST':
        editID = request.values.get('id_num')
        print("teehee " + editID)
        try:
            return redirect(url_for('edit', editID=editID))
        except:
            print("Something went wrong")
    items = Item.query.all()
    return render_template("home.html", items=items, form=form)

## For adding an item to the database
@app.route("/add", methods=['POST', 'GET'])
def item_create():
    message = "Input"
    form = MyForm()

    if request.method == 'POST':
        name = request.form.get('name').strip()
        inventory = request.form.get('inventory')
        price = request.form.get('price')
        description = request.form.get('description').strip()
        ## defaults inventory and price to 0
        if str(inventory) == "":
            inventory = 0.0
        if str(price) == "":
            price = 0 

        try:
            if float(price) >= 0.0 and int(float(inventory)) >= 0:
                item = Item(name=name, inventory=int(float(inventory)), price=(round(float(price), 2)), description=description)
                db.session.add(item)
                db.session.commit()
                message = "Success!"
            else:
                message = "Non-negative numbers only >:("
        except:
            message = "Something went wrong xO"
    else:
        message = "Input info"
            


    return render_template('add.html', form=form, message=message)

## For removing an item from the database
@app.route("/remove", methods=['POST', 'GET'])
def delete():
    form = IDForm()
    items = Item.query.all()
    message = ""
    if request.method == 'POST':
        id_num = request.form.get("id_num")
        try:
            Item.query.filter_by(id_num=int(id_num)).delete()
            db.session.commit()
            items = Item.query.all()
        except:
            print("Bad things happend")
            message = "bad input"
    return render_template("remove.html", form=form, message=message, items=items)

## For searching items and viewing all items
@app.route("/search", methods=['POST', 'GET'])
def view():
    message = ""
    form = SearchForm()
    items = Item.query.all()
    if request.method == 'POST':
        search = request.form.get('search').strip()
        if str(search):
            items = Item.query.filter(Item.name.contains(search)).all()
            if search=="" or len(items) == 0:
                items = Item.query.all()

    return render_template("search.html", items=items, form=form)

## For editing certain items in the database
@app.route("/edit/<int:editID>", methods=['POST', 'GET'])
def edit(editID):
    message = ""
    form = MyForm()
    if editID == "":
        message = "Invalid page, please go back and enter a value"
        return render_template("edit.html", form=form, message=message, editID=editID)

    item = Item.query.filter_by(id_num=editID).first()
    if not item:
        message = "So empty :o, seems like there isn't an item with ID: " + str(editID)
        return render_template("edit.html", form=form, message=message, editID=editID)

    form.name.data = item.name
    form.inventory.data = item.inventory
    form.price.data = item.price
    form.description.data = item.description

    if request.method == 'POST':
        name = request.form.get('name').strip()
        inventory = request.form.get('inventory')
        price = request.form.get('price')
        description = request.form.get('description').strip()
        if str(name) == "":
            name = item.name
        if str(inventory) == "":
            inventory = int(item.inventory)
        if str(price) == "":
            price = float(item.price)
        try:
            if float(price) >= 0.0 and int(float(inventory)) >= 0:
                item.name = name
                item.inventory = int(float(inventory))
                item.price = round(float(price), 2)
                item.description = description
                db.session.commit()
                form.name.data = item.name
                form.inventory.data = item.inventory
                form.price.data = item.price
                form.description.data = item.description
                message = "Success!"
            else:
                message = "Non-negative numbers only >:("
        except:
            message = "Something went wrong xO"
    else:
        message = "Input new info"
    return render_template("edit.html", form=form, message=message, editID=editID, item=item)

## Challenge problem
@app.route("/shipment", methods=['POST', 'GET'])
@app.route("/shipment/<queryID>", methods=['POST', 'GET'])
def challenge(queryID):
    message = ""
    form = MyForm()
    formSearch = IDForm()
    items = Item.query.all()

    if request.form['action'] == 'Add New':
        print(1)
    elif request.form['action'] == 'Search Item ID':
        print(2)
    elif request.form['action'] == 'Search Shipment ID':
        print(3)
    return render_template("shipment.html", formSearch=formSearch, form=form, message=message, queryID=queryID, items=items)