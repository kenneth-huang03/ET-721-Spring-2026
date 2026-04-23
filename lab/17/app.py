import os
import mysql.connector
from flask import Flask, render_template, request, jsonify
from werkzeug.utils import secure_filename

App = Flask(__name__)

if os.environ.get("_A"):
    from werkzeug.middleware.proxy_fix import ProxyFix
    App.wsgi_app = ProxyFix(App.wsgi_app, x_prefix=1)



# File Acceptance/Storage Configuration
# ====================================================
ALLOWED_EXTENSIONS = ("png", "jpg", "jpeg", "gif")

App.config["UPLOAD_FOLDER"] = "static/uploads"
App.config["MAX_CONTENT_LENGTH"] = 16 * 1024 * 1024


# MySQL Configuration/Helpers
# ====================================================
DATABASE_CONFIG = {
    "host": "localhost",
    "user": "flaskuser",
    "password": "password123",
    "database": "image_app",
}


def get_database_connection():
    return mysql.connector.connect(**DATABASE_CONFIG)

def file_is_allowed(file_name):
    return '.' in file_name and file_name.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


# App Pages
# ====================================================
@App.route('/', methods = ["GET"])
def index_GET():
    connection = get_database_connection()
    cursor = connection.cursor(dictionary = True)
    cursor.execute("SELECT * FROM images ORDER BY uploaded_at DESC")
    
    images = cursor.fetchall()

    cursor.close()
    connection.close()

    return render_template("index.html", images = images)


@App.route("/upload", methods = ["POST"])
def upload_POST():
    if 'image' not in request.files:
        return jsonify({"error": "No image file provided"}), 400
    
    file = request.files["image"]

    if file.filename == '':
        return jsonify({"error": "Image file is missing name"}), 400

    if not (file or file_is_allowed(file.filename)):
        return jsonify({"error": "Image file type is not allowed"}), 400

    filename = secure_filename(file.filename)
    filepath = os.path.join(App.config["UPLOAD_FOLDER"], filename)

    file.save(filepath)
        
    connection = get_database_connection()
    cursor = conneciton.cursor()

    cursor.execute("INSERT INTO images (filename) VALUES (%s)", (filename,))
    connection.commit()

    cursor.close()
    connection.close()

    return jsonify({"message": "Image file uploaded successfully"}), 201    


if __name__ == "__main__":
    App.run(debug = True)
