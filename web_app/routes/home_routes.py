# web_app/routes/home_routes.py

from flask import Blueprint, request, render_template

home_routes = Blueprint("home_routes", __name__)

@home_routes.route("/")
@home_routes.route("/home")
def index():
    print("HOME...")
    return render_template("home.html")

@home_routes.route("/about")
def about():
    print("ABOUT...")
    return render_template("about.html")

@home_routes.route("/fail")
def fail():
    print("fail")
    return render_template("fail.html")

                           
@home_routes.route("/drivers")
def drivers():
    print("DRIVERS...")
    return render_template("drivers.html")

