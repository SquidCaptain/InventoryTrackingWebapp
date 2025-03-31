from flask import Flask, render_template, request, redirect, url_for

from app import app, db
from models import Item, Shipment, ItemShip
from forms import MyForm, IDForm, SearchForm, ShipmentForm
from weather import get_cities, get_weather
from datetime import datetime
from config import Config
import json


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
        try:
            return redirect(url_for('edit', editID=editID))
        except:
            print("Something went wrong")
    
    items = ["Here"]
    try:
        with app.app_context():
            testQuery = Item.query.all()
    except Exception as e:
        items = f"Database connection failed: {e}"
    
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
        location = request.form.get('location')
        description = request.form.get('description').strip()
        ## defaults inventory and price to 0
        ## defaults location to London
        if str(inventory) == "":
            inventory = 0.0
        if str(price) == "":
            price = 0 

        try:
            if float(price) >= 0.0 and int(float(inventory)) >= 0:
                item = Item(name=name, inventory=int(float(inventory)), price=(round(float(price), 2)), location=location, description=description)
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
            print("Bad things happened")
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

    item = Item.query.filter_by(id_num=editID).first()
    form = MyForm(location=item.location)
    
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
        location = request.form.get('location')
        print(item.location)
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
                item.location = location
                item.description = description
                db.session.commit()
                form.name.data = item.name
                form.inventory.data = item.inventory
                form.price.data = item.price
                form.location.data = location
                form.description.data = item.description
                message = "Success!"
            else:
                message = "Non-negative numbers only >:("
        except:
            message = "Something went wrong xO"
    else:
        message = "Input new info"
    return render_template("edit.html", form=form, message=message, editID=editID, item=item)

## Shipment pages
@app.route("/shipment", methods=['POST', 'GET'])
def shipment():
    message = "Input shipment or leave blank for new shipment. You can not delete a shipment."
    form = IDForm()
    current_url = url_for('shipment')
    back_url = url_for('home_page')
    items = Shipment.query.all()
    if items is None:
        items = []
    if request.method == 'POST':
        shipID = request.form.get("id_num")
        if shipID:
            if Shipment.query.filter_by(id_num=shipID).first() is not None:
                return redirect(url_for('ship_id', shipID=int(shipID)))
            else:
                message = "Input shipment or leave blank for new shipment \n Your shipment doesn't seem to exist"
        else:
            ship = Shipment()
            db.session.add(ship)
            db.session.commit()
            return redirect(url_for('ship_id', shipID=ship.id_num))

    return render_template("shipments.html", current_url=current_url, back_url=back_url, form=form, message=message, items=items)

## Find shipment by ID and add items
@app.route("/shipment/<int:shipID>", methods=['POST', 'GET'])
def ship_id(shipID):
    current_url = url_for('ship_id', shipID=shipID)
    back_url = url_for('shipment')
    message = "Add or edit items. If inventory is left empty or is 0, item is deleted from shipment."
    form = ShipmentForm()
    items = ItemShip.query.filter_by(ship_id=shipID).first()
    if items is None:
        items = []
    if request.method == 'POST':
        itemID = int(request.form.get("item_id"))
        inventory = int(request.form.get("inventory"))
        item = Item.query.get(itemID)
        if item is not None:
            if item.inventory >= inventory:
                item_in_ship = ItemShip.query.filter_by(ship_id=shipID).filter_by(item_id=itemID).first()
                if item_in_ship is not None:
                    if inventory == 0:
                        ItemShip.query.filter_by(ship_id=shipID).filter_by(item_id=itemID).delete()
                        db.session.commit()
                    else:
                        item.inventory = item.inventory + (item_in_ship.inventory - inventory)
                        item_in_ship.inventory = inventory
                        db.session.commit()
                        form.item_id.data = itemID
                        form.inventory.data = inventory
                        message += "Successfully edited item in shipment."
                else:
                    item.shipment.append(ItemShip(item_id=itemID, ship_id=shipID, inventory=inventory))
                    item.inventory = item.inventory - inventory
                    db.session.commit()
                    form.item_id.data = itemID
                    form.inventory.data = inventory
                    message += "Successfully added item to shipment."
            else:
                message += "Not enough of item in stock >:("
        else:
            message += "Item does not exist >:("
    
    items = ItemShip.query.filter_by(ship_id=shipID).all()

    return render_template("shipments.html", current_url=current_url, back_url=back_url, form=form, message=message, items=items)