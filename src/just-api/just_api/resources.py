from bson.objectid import ObjectId
from flask import jsonify, make_response, request
from flask_restful import Api, Resource, reqparse

from just_api import mongo

api = Api()

item_arg_parser = reqparse.RequestParser()
item_arg_parser.add_argument(
    'name', dest='name', type=str, help='Name of the menu item.')
item_arg_parser.add_argument(
    'price', dest='price', type=int, help='Price of the menu item.')


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
