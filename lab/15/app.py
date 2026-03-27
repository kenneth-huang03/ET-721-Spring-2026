"""
Kenneth Huang
Tuesday, March 24th, 2026
Lab 15 | REST API and Unit Tests in a Flask Application
"""
from flask import Flask, jsonify, redirect, render_template, request

FApp = Flask(__name__)
URI = "https://knei.dev/ET721"

counter = 0

items = {}

@FApp.route("/")
def index():
    return render_template("index.html", uri=URI)

@FApp.route("/items", methods=["POST"])
def  create_item():
    data = request.get_json()

    global counter
    counter += 1
    # Please never use this in an actual database, if you 
    # delete something all the sudden you have stuff with the same id or overwriting 
    # each other
    # counter = str(len(items))

    items[str(counter)] = data

    return jsonify({"id": counter, "item": data}), 201

@FApp.route("/items", methods=["GET"])
def get_items():
    return jsonify(items)

@FApp.route("/items/<item_id>", methods=["DELETE", "GET", "PUT"])
def handle_item(item_id):
    item = items.get(item_id)
    if request.method == "GET":
        if not item:
            return jsonify({"message": "Error: Item Not Found"}), 404
        return jsonify(item), 200
    elif request.method == "PUT":
        if not item:
            return render_template("error.html", message="NOT FOUND", item = item), 404

        data = request.get_json()
        if not data:
            return jsonify({"message": "Error: Invalid Input"}), 400

        items[item_id] = data
        return render_template("update.html", item_id = item_id, item = data)
    elif request.method == "DELETE":
        deleted = items.pop(item_id)
        return render_template("delete.html", item_id = item_id, item = deleted)


if __name__ == "__main__":
    import os
    if os.environ.get("_A_A_"):
        from werkzeug.middleware.proxy_fix import ProxyFix
        FApp.wsgi_app = ProxyFix(FApp.wsgi_app, x_prefix=1)
    
    FApp.run(debug=True)
