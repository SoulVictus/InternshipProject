from flask import Flask, request, flash, jsonify
import json
from DatabaseConnection import MongoDbConnectionClient
from werkzeug.utils import secure_filename
import os

testdb = MongoDbConnectionClient('mongodb+srv://testuser01:test12345@cluster0.hdufc.azure.mongodb.net/InternshipProjectDB?retryWrites=true&w=majority')

UPLOAD_FOLDER = os.getcwd()+"\\Server-files"
ALLOWED_EXTENSIONS = {'xml'}

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route("/files", methods=["GET"])
def get_file_list():
        return jsonify({"filelist": testdb.get_all_documents()})

@app.route("/files/<int:file_id>", methods=["GET"])
def get_specific_file(file_id):
        return testdb.get_document(file_id)


@app.route("/upload", methods=["POST"])
def upload_to_database():
        name = request.json["name"]
        path = request.json["path"]
        print("POST TEST")
        try:
                testdb.put_document_into_collection(name, path)
                return "201"
        except:
                return "400"

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route("/fileupload", methods=["POST"])
def upload_file():
        file = request.files['file']
        if "file" not in request.files:
             flash("No file part")
             return "1"
        if file.filename == '':
             flash("No selected file")
             return "0"
        if file and allowed_file(file.filename):
             filename = secure_filename(file.filename)
             file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
             testdb.put_document_into_collection(file.filename, app.config['UPLOAD_FOLDER'])
             return "200"
        return "2"

if __name__ == "__main__":
    app.secret_key = 'some secret key'
    app.run()

