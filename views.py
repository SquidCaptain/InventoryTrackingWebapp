from flask import Flask, render_template, request, redirect, url_for

from app import app, db
from models import Item
from forms import AddForm, DelForm, SearchForm


## --Globals--
items = Item.query.all()

## searching() this function returns items with names matching the search otherwise returns all items
def searching():
    search = str(request.args.get('search')).strip()
    result = Item.query.filter(Item.name.contains(search))
    if search=="" or len(items) == 0:
        result = Item.query.all()
    return result

## searching() this function returns the item with ID matching specified ID
def searchID():
    search = editID ##str(request.args.get('searchID')).strip()
    result = Item.query.filter_by(id==search).first()
    return result

## Routes
@app.route("/")
@app.route("/home")
def home_page():
    #Item.query.filter_by(id_num=2).delete()
    #Item.query.filter_by(id_num=4).delete()
    #Item.query.filter_by(id_num=5).delete()
    #Item.query.filter_by().delete()
    #item = Item(name='Fat cat', inventory=1, price=9.0, description='Has enough food')
    #db.session.add(item)
    #db.session.commit()
    items = Item.query.all()
    return render_template("home.html", items=items)

@app.route("/add", methods=['POST', 'GET'])
def item_create():
    message = "Input"
    form = AddForm()

    if request.method == 'POST':
        name = request.form.get('name').strip()
        inventory = request.form.get('inventory')
        price = request.form.get('price')
        description = request.form.get('description').strip()
        if name:
            ##check if other args defaults
            if str(inventory) == "":
                inventory = 0
            if str(price) == "":
                price = 0 
            try:
                if price >= 0 and inventory >= 0:
                    item = Item(name=name, inventory=inventory, price=price, description=description)
                    db.session.add(item)
                    db.session.commit()
                    message = "Success"
                else:
                    message = "Non-negative numbers only >:("
            except:
                message = "Bad Input"
        message = "Bad Input"
    else:
        message = "Input"
            


    return render_template('add.html', form=form, message=message)

@app.route("/remove", methods=['POST', 'GET'])
def delete():
    form = DelForm()
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

@app.route("/search")
def view():
    message = ""
    form = SearchForm()

    if request.method == 'POST':
        search = request.form.get('search').strip()

    searchResult = searching()
    return render_template("search.html", items=searchResult)

@app.route("/edit/<editID>")
def edit(editID):
    message = ""
    form = AddForm()

    if request.method == 'POST':
        name = request.form.get('name').strip()
        inventory = request.form.get('inventory')
        price = request.form.get('price')
        description = request.form.get('description').strip()
        if str(name) == "":
            price = ""
        if str(inventory) == "":
            inventory = 0
        if str(price) == "":
            price = 0
        if str(description) == "":
            price = ""
        try:
            if price >= 0 and inventory >= 0:
                item = Item(name=name, inventory=inventory, price=price, description=description)
                db.session.add(item)
                db.session.commit()
                message = "Success"
            else:
                message = "Non-negative numbers only >:("
        except:
            message = "Bad Input"
    else:
        message = "Input"

    return render_template("edit.html", form=form, message=message)

@app.route("/challenge")
def challenge():
    return render_template("challenge.html", items=items)