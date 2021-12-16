from project.appp import app
from flask import render_template


@app.route("/")
def index():
    return render_template("index.html")

@app.route("/about")
def about():
    return "about"

@app.route("/json")
def json():
    return 
