from hashlib import md5
from datetime import datetime
import json
from bson import ObjectId

def generate_md5(str_to_hash):
    result = md5(bytes(str_to_hash, "utf-8"))
    return result.hexdigest()

def generate_timestamp():
    datestr = "{:%Y-%m-%d %H:%M:%S}".format(datetime.now())
    return datestr

class JSONEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, ObjectId):
            return str(o)
        return json.JSONEncoder.default(self, o)
