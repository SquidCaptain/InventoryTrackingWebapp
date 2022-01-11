from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from models import Item

from config import Config
#from orderedList import *

app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)
##data = OrderedList()
search = ""
items = Item.query.all()

## Routes

@app.route("/")
@app.route("/home")
def home_page():
    items = Item.query.all()
    return render_template("home.html", items=items)

@app.route("/input")
def input():
    return "input"

@app.route("/edit")
def edit():
    return "edit"

@app.route("/delete")
def delete():
    return "delete"

@app.route("/view")
def view():
    search = request.args.get('search')
    return render_template("view.html")

@app.route("/challenge")
def challenge():
    return "challenge"
