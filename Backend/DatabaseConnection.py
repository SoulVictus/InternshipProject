from pymongo import MongoClient
from datetime import datetime
import json
from utils import generate_md5, generate_timestamp, JSONEncoder


class MongoDbConnectionClient:
    def __init__(self, connectionstring):
        self.client = MongoClient(connectionstring)
        self.db = self.client.InternshipProjectDB
        self.collection = self.db.FilesCollection

    def get_all_documents(self):
        documentList = []
        for document in self.collection.find():
            #JSONEncoder().encode() encode MongoDB's ObjectId into string
            documentList.append(json.loads(JSONEncoder().encode(document)))
        return documentList
        
    def get_document(self, id):
        document = self.collection.find_one({"id": id})
        #JSONEncoder().encode() encode MongoDB's ObjectId into string
        jsonStr = json.loads(JSONEncoder().encode(document))
        return jsonStr

    def put_file_into_collection(self, name, path):
        documentAmount = self.collection.count_documents({})
        document = {
            "id": documentAmount+1,
            "name": name,
            "path": path,
            "timestamp": generate_timestamp(),
            "md5": generate_md5(name)
        }
        self.collection.insert_one(document).inserted_id

testdb = MongoDbConnectionClient('mongodb+srv://testuser01:test12345@cluster0.hdufc.azure.mongodb.net/InternshipProjectDB?retryWrites=true&w=majority')

print(testdb.get_document(1))