from datetime import datetime
from turtle import back
from weather import get_weather, get_cities

from app import db

import requests, json

# Models for SQLAlchemy to create and manage database

# Association table for many to many relationship of Item and Shipment
# pimary key: id
# foreignkey: item_id (Item.id_num)
#             ship_id (Shipment.id_num)
class ItemShip(db.Model):
    __tabelname__= 'item_ship'
    item_id = db.Column('item_id', db.Integer, db.ForeignKey('item.id_num'), primary_key=True)
    ship_id = db.Column('ship_id', db.Integer, db.ForeignKey('shipment.id_num'), primary_key=True)
    inventory = db.Column('inventory', db.Integer)
    item = db.relationship("Item", back_populates="shipment")
    shipment = db.relationship("Shipment", back_populates="item")
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def __repr__(self):
        return f'< Item ID: { self.item_id }, Inventory Shipped: { self.inventory } >'


# Item model for database
# primary key: id_num
class Item(db.Model):
    __tabelname__= 'item'
    id_num = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(140))
    inventory = db.Column(db.Integer)
    price = db.Column(db.Float)
    location = db.Column(db.Integer)
    description = db.Column(db.Text)
    created = db.Column(db.DateTime, default=datetime.now())
    shipment = db.relationship('ItemShip', back_populates="item")

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def __repr__(self):
        weather = get_weather()
        cities = get_cities()
        loc_weather = weather[0]
        translated_loc = cities[self.location - 1]
        
        for i in range(len(cities)):
            if cities[i] == translated_loc:
                loc_weather = weather[i]
                 
        return f'< Item id: {self.id_num}, Name: {self.name}, Inventory: {self.inventory}, Price: ${self.price}, Location: {translated_loc}: {loc_weather}, Description: {self.description} >'

# Shipment model for database
# primary key: id_num
# Note: Have not implemented Shipment source\destination\price
class Shipment(db.Model):
    __tabelname__= 'shipment'
    id_num = db.Column(db.Integer, primary_key=True)
    created = db.Column(db.DateTime, default=datetime.now())
    item = db.relationship('ItemShip', back_populates="shipment")

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def __repr__(self):
        return f'<Item id: {self.id_num} Transaction Date: {self.created}>'

db.create_all()