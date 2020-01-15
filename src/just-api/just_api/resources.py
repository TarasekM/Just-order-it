import datetime
import json
from bson.objectid import ObjectId
from flask import jsonify, make_response, request
from flask_restful import Api, Resource, reqparse

from just_api import mongo

api = Api()

item_arg_parser = reqparse.RequestParser()
item_arg_parser.add_argument(
    'name', dest='name', type=str, help='(str) Name of the menu item.')
item_arg_parser.add_argument(
    'price', dest='price', type=float, help='(float) Price of the menu item.')
item_arg_parser.add_argument(
    'tags', dest='tags', type=str, action='append', help='(list) Tags of menu item.')
item_arg_parser.add_argument(
    'ingredients', dest='ingredients', type=str, action='append', help='(list) Ingredients of menu item')

order_arg_parser = reqparse.RequestParser()
order_arg_parser.add_argument(
    'order_date', dest='order_date', type=str, help='(str) Date of the order.')
order_arg_parser.add_argument(
    'order_pickup_date', dest='order_pickup_date', type=str, help='(str) Date of the pickup order.' )
order_arg_parser.add_argument(
    'items', dest='items', type=str, action='append', help='(str) IDs of items in the order')
order_arg_parser.add_argument(
    'total_price', dest='total_price', type=float, help='(float) Total price of the order')


class Order(Resource):

    def get(self):
        return make_response(jsonify(list(mongo.db.order.find({}))), 200)

    def post(self):
        args = order_arg_parser.parse_args()
        args['order_date'] = datetime.datetime.now()
        args['order_pickup_date'] = ''
        inserted_id = mongo.db.order.insert_one(args).inserted_id
        return make_response(jsonify({'_id': inserted_id}), 201)


class SpecificOrder(Resource):

    def get(self, _id):
        item = mongo.db.order.find_one_or_404({'_id': _id})
        return make_response(jsonify(item), 200)

    def put(self, _id):
        args = item_arg_parser.parse_args()
        mongo.db.order.find_one_or_404({'_id': _id})
        mongo.db.order.find_one_and_update({"_id": _id},
                                          {"$set": args})
        return make_response(jsonify({'_id': _id}), 200)

    def delete(self, _id):
        mongo.db.order.find_one_or_404({'_id': _id})
        mongo.db.order.delete_one({'_id': _id})
        return make_response(jsonify({'_id': _id}), 200)


class MenuItem(Resource):

    def get(self, _id):
        item = mongo.db.menu.find_one_or_404({'_id': _id})
        return make_response(jsonify(item), 200)

    def put(self, _id):
        args = item_arg_parser.parse_args()
        mongo.db.menu.find_one_or_404({'_id': _id})
        mongo.db.menu.find_one_and_update({"_id": _id},
                                          {"$set": args})
        return make_response(jsonify({'_id': _id}), 200)

    def delete(self, _id):
        mongo.db.menu.find_one_or_404({'_id': _id})
        mongo.db.menu.delete_one({'_id': _id})
        return make_response(jsonify({'_id': _id}), 200)


class Menu(Resource):

    def get(self):
        return make_response(jsonify(list(mongo.db.menu.find({}))), 200)

    def post(self):
        args = item_arg_parser.parse_args()
        inserted_id = mongo.db.menu.insert_one(args).inserted_id
        return make_response(jsonify({'_id': inserted_id}), 201)


api.add_resource(MenuItem, '/menu/<ObjectId:_id>')
api.add_resource(Menu, '/menu')
api.add_resource(Order, '/order')
api.add_resource(SpecificOrder, '/order/<ObjectId:_id>')
