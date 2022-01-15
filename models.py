from datetime import datetime

from app import db

## Models for SQLAlchemy to create and manage database

## Item model for database
## primary key: id_num
class Item(db.Model):
    id_num = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(140))
    inventory = db.Column(db.Integer)
    price = db.Column(db.Float)
    description = db.Column(db.Text)
    created = db.Column(db.DateTime, default=datetime.now())
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def __repr__(self):
        return f'<Item id: {self.id_num}, name: {self.name}, inventory: {self.inventory}, price: ${self.price}, description: {self.description}>'