from datetime import datetime
import json
from bson import ObjectId

def generate_timestamp():
    datestr = "{:%Y-%m-%d %H:%M:%S}".format(datetime.now())
    return datestr

class JSONEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, ObjectId):
            return str(o)
        return json.JSONEncoder.default(self, o)
