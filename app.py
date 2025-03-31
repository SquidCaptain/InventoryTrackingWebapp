from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy

from config import Config
#from orderedList import *

## --Flask App--
app = Flask(__name__)
app.config.from_object(Config)

## --Database--
try:
    db = SQLAlchemy(app)
    with app.app_context():
        db.create_all()
        print("Database initialized successfully.")
except Exception as e:
    print(f"Database connection failed: {e}")