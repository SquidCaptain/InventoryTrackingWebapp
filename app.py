from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy

from config import Config
#from orderedList import *

## --Flask App--
app = Flask(__name__)
app.config.from_object(Config)

## --Database--
db = SQLAlchemy(app)
db.create_all()