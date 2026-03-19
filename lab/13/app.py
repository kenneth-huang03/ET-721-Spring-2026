"""
Kenneth Huang
March 17th, 2026
Lab 13 | Simple submission form to simulate a Full Stack App
"""

from flask import Flask, render_template, request
from flask_mysqldb import MySQL

FApp = Flask(__name__)

FApp.config["MYSQL_USER"] = "flaskuser"
FApp.config["MYSQL_HOST"] = "127.0.0.1"
FApp.config["MYSQL_PASSWORD"] = "password123"

FApp.config["MYSQL_DB"] = "employee_data"

DB = MySQL(FApp)

import os
if os.environ.get("_A_A_"):
    from werkzeug.middleware.proxy_fix import ProxyFix
    FApp.wsgi_app = ProxyFix(FApp.wsgi_app, x_prefix=1)


@FApp.route("/", methods=["get", "post"])
def index():
    message = ""

    if request.method == "POST":
        name = request.form["name"]
        age = request.form["age"]

        cursor = DB.connection.cursor()
        cursor.execute("INSERT INTO employee(name, age) VALUES (%s, %s)", (name, age))
        DB.connection.commit()
        cursor.close()

        message = "Data Inserted!"

    return render_template("index.html", message=message)


if __name__ == "__main__":
    FApp.run(debug=True)
