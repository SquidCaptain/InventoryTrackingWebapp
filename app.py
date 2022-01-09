from flask import Flask 

app = Flask(__name__)

@app.route("/")
def index():
    return "main page"

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
    return "view"

## something added