from flask.json import JSONEncoder
from bson.objectid import ObjectId


class JSONEncoderImproved(JSONEncoder):
    def default(self, obj):
        if isinstance(obj, ObjectId):
            return str(obj)
        else:
            return super().default(obj)
