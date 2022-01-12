from flask import Flask, render_template, request

from app import app, db
from models import Item
## Routes

## --Globals--
items = Item.query.all()

## searching() this function returns items with names matching the search otherwise returns all items
def searching():
    search = str(request.args.get('search')).strip()
    result = Item.query.filter_by(Item.name.contains(search))
    if search=="" or len(items.all()) == 0:
        result = Item.query.all()
    return result

## searching() this function returns the item with ID matching specified ID
def searchID():
    search = editID ##str(request.args.get('searchID')).strip()
    result = Item.query.filter_by(id==search).first()
    return result
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

@app.route("/add")
def input():
    message = "Add a new item!"
    name = str(request.args.get('name')).strip()
    price = float(request.args.get('price'))
    inventory = int(request.args.get('inventory'))
    description = str(request.args.get('description')).strip()
    if name and price>=0.0 and inventory>=0:
        item = Item(name=name, inventory=inventory, price=price, description=description)
        db.session.add(item)
        db.session.commit()

    return render_template("add.html", message=message ,name=name)

@app.route("/remove")
def delete():
    message = "Warning: input will be floored and item will be permanantly deleted"
    Item.query.filter_by(id_num=int(request.args.get('inventory'))).delete()
    db.session.commit()
    return render_template("remove.html", items=items)

@app.route("/search")
def view():
    searchResult = searching()
    return render_template("search.html", items=searchResult)

@app.route("/edit/<editID>")
def edit(editID):
    searchResult=searchID(editID)
    message = "Welcome"
    if searchResult == None:
        message = "Invalid ID"
        searchResult = []
    else:


    
    return render_template("edit.html", message=message, item=searchResult)

@app.route("/edit/verify/<valid>")
def verify(valid):


@app.route("/challenge")
def challenge():
    return render_template("challenge.html", items=items)