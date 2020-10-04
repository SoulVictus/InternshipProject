from flask import Flask, request, flash, jsonify
import json
from DatabaseConnection import MongoDbConnectionClient
from werkzeug.utils import secure_filename
import os

testdb = MongoDbConnectionClient('mongodb+srv://testuser01:test12345@cluster0.hdufc.azure.mongodb.net/InternshipProjectDB?retryWrites=true&w=majority')

ALLOWED_EXTENSIONS = {'xml','txt'}

app = Flask(__name__)

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route("/upload", methods=["POST"])
def upload_file():
        file = request.files['file']
        if "file" not in request.files:
             flash("No file part")
             return "1"
        if file.filename == '':
             flash("No selected file")
             return "1"
        if file and allowed_file(file.filename):
             filename = secure_filename(file.filename)
             testdb.put_file_into_database(filename, file)
             return "201"
        return "2"

@app.route("/files", methods=["GET"])
def get_file():
        return jsonify({"filelist": testdb.list_all_files()})


if __name__ == "__main__":
    app.secret_key = 'some secret key'
    app.run()

