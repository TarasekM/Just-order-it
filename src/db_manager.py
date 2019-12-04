from pymongo import MongoClient


class DbManager(object):

    def __init__(self, database_name, host='localhost', port=27017, document_class=dict):
        self.database_name = database_name
        self.client = MongoClient(host=host, port=port, document_class=document_class)

    def add(self, data):
        db = self.client[self.database_name]
        order = db.order
        result = order.insert_one(data)
        return result
