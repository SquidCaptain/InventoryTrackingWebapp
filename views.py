from flask import Flask, render_template, request, redirect, url_for

from app import app, db
from models import Item
from forms import AddForm, DelForm


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
    form = AddForm()

    if request.method == 'POST':
        name = request.form.get('name')
        inventory = request.form.get('inventory')
        price = request.form.get('price')
        description = request.form.get('description')

        try:
            item = Item(name=name, inventory=inventory, price=price, description=description)
            db.session.add(item)
            db.session.commit()
        except:
            print("Bad things happend")


    return render_template('add.html', form=form)

@app.route("/remove", methods=['POST', 'GET'])
def delete():
    form = DelForm()
    items = Item.query.all()
    message = ""
    if request.method == 'POST':
        id_num = request.form.get("id_num")
        print(id_num)
        try:
            Item.query.filter_by(id_num=int(id_num)).delete()
            db.session.commit()
        except:
            print("Bad things happend")
            message = "bad input"
    return render_template("remove.html", form=form, message=message, items=items)

@app.route("/search")
def view():
    searchResult = searching()
    return render_template("search.html", items=searchResult)

@app.route("/edit/<editID>")
def edit(editID):
    '''searchResult=searchID(editID)
    message = "Welcome"
    if searchResult == None:
        message = "Invalid ID"
        searchResult = []
    else:
        message = "Edit here"'''
    return render_template("edit.html")

@app.route("/edit/verify/<valid>")
def verify(valid):
    return "valid"

@app.route("/challenge")
def challenge():
    return render_template("challenge.html", items=items)