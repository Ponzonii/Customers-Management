# Import necessary modules from Flask
from flask import Blueprint as Bp, render_template as rt

# Create a Blueprint named "home"
home = Bp("home", __name__)


# Define a route for the home page
@home.route("/")
def index():
    # Render and return the "index.html" template
    return rt("index.html")
