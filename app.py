from flask import Flask, render_template
from orderedList import *

app = Flask(__name__)
data = OrderedList()


@app.route("/")
def home_page():
    return render_template("home.html")

@app.route("/input")
def input():
    return "input"

@app.route("/edit")
def edit():
    return "edit"

@app.route("/delete")
def delete():
    return "delete"

@app.route("/view/<id>/<name>")
def view(id, name):
    return "viewing id, name"

@app.route("/challenge")
def challenge():
    return "challenge"
