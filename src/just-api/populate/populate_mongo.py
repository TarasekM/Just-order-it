""" Simple script to populate orders collection in the mongo db.

"""
import json
import os
from pathlib import Path
from pprint import pprint
from random import randint

from pymongo import MongoClient

ORDERS_DATA_JSON = Path(os.path.realpath(
    __file__)).parent / Path('orders.json')
MENU_ITEMS_DATA_JSON = Path(os.path.realpath(
    __file__)).parent / Path('menu_items.json')
DATABASE = 'mydb'

if __name__ == '__main__':
    MONGO_URI = os.environ.get('DEV_MONGO_URI')
    if MONGO_URI is None:
        raise Exception('No mongo db URI provided!')
    with open(MENU_ITEMS_DATA_JSON, 'r') as menu_items_file:
        menu_items = json.load(menu_items_file)
    mongo = MongoClient('mongodb://mongodb:27017/mydb')

    print('Inserting menu items')
    menu_result = mongo[DATABASE].menu.insert_many(menu_items)
    print('Inserted:', mongo[DATABASE].menu.count_documents({}))
    pprint(list(mongo[DATABASE].menu.find({})))

    with open(ORDERS_DATA_JSON, 'r') as orders_file:
        orders = json.load(orders_file)

    last_index_of_orders = len(orders) - 1
    for order in orders:
        start = randint(0, last_index_of_orders)
        end = start + randint(1, 5)
        order.update({'items': menu_result.inserted_ids[start:end]})

    print('Inserting orders')
    result = mongo[DATABASE].orders.insert_many(orders)
    print('Inserted:', mongo[DATABASE].orders.count_documents({}))
    pprint(list(mongo[DATABASE].orders.find({})))
