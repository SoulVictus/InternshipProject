from datetime import datetime
import json
from bson import ObjectId

def generate_timestamp():
    datestr = "{:%Y-%m-%d %H:%M:%S}".format(datetime.now())
    return datestr

ALLOWED_EXTENSIONS = {'xml'}

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS
