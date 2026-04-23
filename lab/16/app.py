from flask import Flask, jsonify, render_template, request
import mysql.connector


App = Flask(__name__)

import os
if os.environ.get("_A_A_"):
    from werkzeug.middleware.proxy_fix import ProxyFix
    App.wsgi_app = ProxyFix(App.wsgi_app, x_prefix=1)


# Database Configuration
# ======================

App.config["MYSQL_HOST"]        = "localhost"
App.config["MYSQL_USER"]        = "flaskuser"
App.config["MYSQL_PASSWORD"]    = "password123"
App.config["MYSQL_DB"]          = "l16_todo"


DatabaseConnectionPool = mysql.connector.pooling.MySQLConnectionPool(
    pool_name           = "Pool",
    pool_size           = 3,
    pool_reset_session  = True,
    host                = App.config["MYSQL_HOST"],
    user                = App.config["MYSQL_USER"],
    password            = App.config["MYSQL_PASSWORD"],
    database            = App.config["MYSQL_DB"],
)

def getDatabase():
    return DatabaseConnectionPool.get_connection()

# Application Routes
# ==================

@App.route("/")
def index():
    return render_template("index.html")


@App.route("/get_tasks", methods=["GET"])
def get_tasks():
    try:
        database = getDatabase()
        with database.cursor(dictionary=True) as cursor:
            cursor.execute("SELECT * FROM tasks")

            tasks = cursor.fetchall()

        return jsonify(tasks), 200
    except mysql.connector.Error as error:
        print(error)
        return jsonify({"MySQL Error": str(error)}), 500

    finally:
        database.close()


@App.route("/add_task", methods=["POST"])
def add_task():
    data = request.get_json()
    task = data.get("task")

    if task:
        database = getDatabase()
        cursor = database.cursor()
        cursor.execute("INSERT INTO tasks (task) VALUES (%s)", (task,))
        database.commit()
        cursor.close()
        database.close()
        return jsonify({"status": "success"})

    return jsonify({"status": "error"})


@App.route("/delete_task", methods = ["POST"])
def delete_task():
    data = request.get_json()
    id = data.get("id")

    database = getDatabase()
    cursor = database.cursor()
    cursor.execute("DELETE FROM tasks WHERE id = %s", (id,))

    database.commit()
    cursor.close()
    database.close()

    return jsonify({"status": "deleted"})

# Start Application
# =================
if __name__ == "__main__":
    App.run()

