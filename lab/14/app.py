"""
Kenneth Huang
Thursday, March 19th, 2026
Lab 14 | Mini Blog App using Flask
"""
from flask import Flask, redirect, render_template, request, url_for
from flask_mysqldb import MySQL

FApp = Flask(__name__)

FApp.config["MYSQL_USER"] = "flaskuser"
FApp.config["MYSQL_HOST"] = "127.0.0.1"
FApp.config["MYSQL_PASSWORD"] = "password123"

FApp.config["MYSQL_DB"] = "blogDB"

DB = MySQL(FApp)


@FApp.route("/")
def index():
    return render_template("index.html")

@FApp.route("/add_blog", methods=["POST"])
def add_blog():
    username = request.form["username"]
    email = request.form["email"]
    title = request.form["title"]
    content = request.form["content"]

    DBCursor = DB.connection.cursor()

    DBCursor.execute("INSERT IGNORE INTO users (username, email) VALUES (%s, %s)", (username, email))
    DB.connection.commit()

    uid = DBCursor.lastrowid

    if uid == 0:
        DBCursor.execute("SELECT id FROM users WHERE email = %s", (email,))
        uid = DBCursor.fetchone()[0]

    DBCursor.execute("INSERT INTO blog (user_id, title, content) VALUES (%s, %s, %s)", (uid, title, content))
    DB.connection.commit()

    DBCursor.close()

    return redirect("/ET721/blogs")

@FApp.route("/blogs")
def blogs():
    DBCursor = DB.connection.cursor()
    DBCursor.execute("SELECT blog.id, users.username, blog.title, blog.content, blog.created_At FROM blog JOIN users ON blog.user_id = users.id")

    all = DBCursor.fetchall()

    DBCursor.close()

    return render_template("blogs.html", blogs=all)


if __name__ == "__main__":
    import os
    if os.environ.get("_A_A_"):
        from werkzeug.middleware.proxy_fix import ProxyFix
        FApp.wsgi_app = ProxyFix(FApp.wsgi_app, x_prefix=1)
    
    FApp.run(debug=True)
