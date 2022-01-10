from flask import Flask, render_template, request
from orderedList import *

app = Flask(__name__)
data = OrderedList()
search = "all"

@app.route("/")
@app.route("/home")
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

@app.route("/view")
def view():
    search = request.args.get('search')
    return render_template("view.html")

@app.route("/challenge")
def challenge():
    return "challenge"
