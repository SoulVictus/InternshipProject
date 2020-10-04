from pymongo import MongoClient
import gridfs
from datetime import datetime
import json
from utils import generate_timestamp, JSONEncoder


class MongoDbConnectionClient:
    def __init__(self, connectionstring):
        self.client = MongoClient(connectionstring)
        self.db = self.client.InternshipProjectDB
        self.fs = gridfs.GridFS(self.db)

    def put_file_into_database(self,name, file):
        self.fs.put(file, filename=name, upload=generate_timestamp())
    
    def list_all_files(self):
        data = self.fs.list()
        return data

