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
            documentList.append(JSONEncoder().encode(document))
        return str(documentList)
        
    def get_document(self, id):
        document = self.collection.find_one({"id": id})
        jsonStr = JSONEncoder().encode(document)
        return str(jsonStr)

    def put_file_into_collection(self, name, path):
        documentAmount = self.collection.count_documents({})
        document = {
            "id": documentAmount+1,
            "name": name,
            "path": path,
            "timestamp": generate_timestamp(),
            "md5": generate_md5("test")
        }
        self.collection.insert_one(document).inserted_id

