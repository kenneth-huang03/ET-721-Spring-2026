"""
Kenneth Huang
Lab 11 | Intro to Flask
March 10th, 2026
"""
from flask import Flask, render_template

# Create the Flask Object
app = Flask(__name__)

# THIS FOLLOWING BLOCK IS SO I CAN WORK WITH FLASK ON MY VPS IM SORRY
import os
if os.environ.get("_A_A_"):
    from werkzeug.middleware.proxy_fix import ProxyFix
    app.wsgi_app = ProxyFix(app.wsgi_app, x_prefix=1)
# END BLOCK

# Set the routing for pages
# the @Flask.route(route) decorator is used to acheive this
@app.route("/")
def index():
    name = "Kenneth Huang"
    fruits = ["Apple", "Orange", "Grapes"]
    fruit = "Orange"
    return render_template("index.html", username=name, fruitlist=fruits, f=fruit)

@app.route("/about")
def about():
    images = ["pexels-anna-shakhrai-129681881-36237468.jpg", "pexels-gaby-lopez-301814849-36374114.jpg", "pexels-umar-faruq-1662051319-34932322.jpg"]
    return render_template("about.html", images=images)

@app.route("/quotes")
def quotes(): 
    return render_template("quotes.html")

if __name__ == "__main__":
    app.run()
