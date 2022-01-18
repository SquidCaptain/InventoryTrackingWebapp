from datetime import datetime

from app import db

# Models for SQLAlchemy to create and manage database

# For many to one relationship of Item to Shipment
item_ship = db.Table('item_ship',
                     db.Column('item_id', db.Integer,
                               db.ForeignKey('item.id_num')),
                     db.Column('ship_id', db.Integer,
                               db.ForeignKey('shipment.id_num')),
                     db.Column('inventory', db.Integer))

# Item model for database
# primary key: id_num
class Item(db.Model):
    id_num = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(140))
    inventory = db.Column(db.Integer)
    price = db.Column(db.Float)
    description = db.Column(db.Text)
    created = db.Column(db.DateTime, default=datetime.now())
    ships = db.relationship('Shipment', secondary=item_ship, backref=db.backref('item'), lazy='dynamic')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def __repr__(self):
        return f'< Item id: {self.id_num}, Name: {self.name}, Inventory: {self.inventory}, Price: ${self.price}, Description: {self.description} >'

# Shipment model for database
# primary key: id_num
# Note: Have not implemented Shipment source\destination\price since warehouse locations have not been implemented
class Shipment(db.Model):
    id_num = db.Column(db.Integer, primary_key=True)
    created = db.Column(db.DateTime, default=datetime.now())
    ##items = db.relationship('Item', secondary=item_ship, backref=db.backref('shipment'), lazy='dynamic')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def __repr__(self):
        return f'<Item id: {self.id_num} Transaction Date: {self.created}>'

db.create_all()