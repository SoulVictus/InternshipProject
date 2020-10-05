from pymongo import MongoClient
import gridfs
from datetime import datetime
import json
from utils import generate_timestamp


class MongoDbConnectionClient:
    def __init__(self, connectionstring):
        self.__client = MongoClient(connectionstring)
        self.__db = self.__client.InternshipProjectDB
        self.__fs = gridfs.GridFS(self.__db)

    def put_file_into_database(self,name, file):
        if self.__fs.exists({"filename": name}):
            fileToDeleteID = self.__fs.find_one({"filename": name})._id
            self.__fs.delete(fileToDeleteID)
            self.__fs.put(file, filename=name, uploadDateCET=generate_timestamp())
        else:
            self.__fs.put(file, filename=name, uploadDateCET=generate_timestamp())
    
    def list_all_files(self):
        data = self.__fs.list()
        return data


