from flask import Flask, request, jsonify
import json
from DatabaseConnection import MongoDbConnectionClient

testdb = MongoDbConnectionClient('mongodb+srv://testuser01:test12345@cluster0.hdufc.azure.mongodb.net/InternshipProjectDB?retryWrites=true&w=majority')

app = Flask(__name__)


@app.route("/files", methods=["GET"])
def get_file_list():
        return jsonify({"filelist": testdb.get_all_documents()})

@app.route("/files/<int:file_id>", methods=["GET"])
def get_specific_file(file_id):
        return testdb.get_document(file_id)


@app.route("/upload", methods=["POST"])
def upload_to_database(name, path):
        return testdb.put_file_into_collection(name, path)

if __name__ == "__main__":
    app.run()

