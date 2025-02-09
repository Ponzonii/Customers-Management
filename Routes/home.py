from flask import Blueprint as Bp, render_template as rt

home = Bp("home", __name__)


@home.route("/")
def index():
    return rt("index.html")
