from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

from config import Config
#from orderedList import *

## --Flask App--
app = Flask(__name__)
app.config.from_object(Config)

## --Database--
db = SQLAlchemy(app)
with app.app_context():
    db.create_all()
    db.session.commit()

## --Database Migration--
migrate = Migrate(app, db)
