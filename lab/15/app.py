"""
Kenneth Huang
Tuesday, March 24th, 2026
Lab 15 | REST API and Unit Tests in a Flask Application
"""
from flask import Flask, jsonify, redirect, render_template, request

FApp = Flask(__name__)
URI = "http://127.0.0.1:5000" 


items = {}

@FApp.route("/")
def index():
    return render_template("index.html", uri=URI)

@FApp.route("/items", methods=["POST"])
def  create_item():
    data = request.get_json()

    item_id = str(len(items)+1) # Please never use this in an actual database, if you 
    # delete something all the sudden you have stuff with the same id or overwriting 
    # each other

    items[item_id] = data

    return jsonify({"id": item_id, "item": data}), 201

@FApp.route("/items", methods=["GET"])
def get_items():
    return jsonify(items)

@FApp.route("/items/<item_id>", methods=["GET"])
def get_one_item(item_id):
    item = items.get(item_id)
    if not item:
        return jsonify({"message": "Error: Item Not Found"}), 404

    return jsonify(item), 200


if __name__ == "__main__":
    import os
    if os.environ.get("_A_A_"):
        from werkzeug.middleware.proxy_fix import ProxyFix
        FApp.wsgi_app = ProxyFix(FApp.wsgi_app, x_prefix=1)
    
    FApp.run(debug=True)
