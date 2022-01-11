from flask import Flask, render_template, request

from app import app, db
from models import Item
## Routes

## --Globals--
items = Item.query.all()

## searching() this function returns items with names matching the search
def searching():
    search = str(request.args.get('search')).strip()
    result = Item.query.filter_by(Item.name.contains(search))
    if len(items.all()) == 0:
        result = Item.query.all()
    return result

## searching() this function returns items with ID matching specified ID
def searchID():
    search = str(request.args.get('search')).strip()
    result = Item.query.filter_by(id==search)
    if len(items.all()) == 0:
        result = Item.query.all()
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
    return render_template("add.html", items=items)

@app.route("/remove")
def delete():
    return render_template("remove.html", items=items)

@app.route("/search")
def view():
    searchResult = searching()
    return render_template("search.html", items=searchResult)

@app.route("/edit/<editID>")
def edit(editID):
    searchResult=searchID()
    
    return render_template("edit.html", items=items)

@app.route("/challenge")
def challenge():
    return render_template("challenge.html", items=items)