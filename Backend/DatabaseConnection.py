from pymongo import MongoClient
import gridfs
from datetime import datetime
import json
from utils import generate_timestamp


class MongoDbConnectionClient:
    def __init__(self, connectionstring):
        self.client = MongoClient(connectionstring)
        self.db = self.client.InternshipProjectDB
        self.fs = gridfs.GridFS(self.db)

    def put_file_into_database(self,name, file):
        if self.fs.exists({"filename": name}):
            fileToDeleteID = self.fs.find_one({"filename": name})._id
            self.fs.delete(fileToDeleteID)
            self.fs.put(file, filename=name, uploadDateCET=generate_timestamp())
        else:
            self.fs.put(file, filename=name, uploadDateCET=generate_timestamp())
    
    def list_all_files(self):
        data = self.fs.list()
        return data


