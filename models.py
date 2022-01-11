from app import db

class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(140))
    inventory = db.Column(db.Integer)
    price = db.Column(db.Integer)
    slug = db.Column(db.String(140), unique=True)
    
