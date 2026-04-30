import sqlite3
from flask import Flask, flash, redirect, render_template, request, session, url_for


App = Flask(__name__)
App.secret_key = "development_secret_key"


if __import__("os").environ.get("_A"):
    from werkzeug.middleware.proxy_fix import ProxyFix
    App.wsgi_app = ProxyFix(App.wsgi_app, x_prefix=1)


# Database
# ===============================================
def get_database_connection():
    connection = sqlite3.connect("flask_auth.db")
    connection.row_factory = sqlite3.Row
    return connection


# Routes
# ===============================================
@App.route('/')
def home():
    return redirect(url_for("login_GET"))


@App.route("/login", methods = ["GET"])
def login_GET():
    return render_template("login.html")


@App.route("/login", methods = ["POST"])
def login_POST():
    connection = get_database_connection()

    cursor = connection.cursor()
    cursor.execute("SELECT username FROM users WHERE email = ? AND password = ?", (request.form["email"], request.form["password"]))

    user = cursor.fetchone()

    connection.close()

    if user:
        session["username"] = user[0]
        return redirect(url_for("dashboard"))
    else:
        flash("Invalid Email or Password")
        return redirect(url_for("login_GET"))


@App.route("/signup", methods = ["GET"])
def signup_GET():
    return render_template("signup.html")


@App.route("/signup", methods = ["POST"])
def signup_POST():
    connection = get_database_connection()

    cursor = connection.cursor()

    try:
        cursor.execute(
            "INSERT INTO users (username, email, password) VALUES (?, ?, ?)", 
            (request.form["username"], request.form["email"], request.form["password"])
        )

        connection.commit()
        flash("Account created!")
        return redirect(url_for("login_GET"))
    except sqlite3.IntegrityError:
        flash("Email already exists!")
        return redirect(url_for("signup_GET"))
    finally:
        connection.close()


@App.route("/logout")
def logout():
    del session["username"]
    return redirect(url_for("login_GET"))


@App.route("/dashboard")
def dashboard():
    if "username" in session:
        return render_template("dashboard.html", username = session["username"])
    return redirect(url_for("login_GET"))


if __name__ == "__main__":
    App.run(debug=True)
