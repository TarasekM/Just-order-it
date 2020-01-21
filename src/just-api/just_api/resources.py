import datetime
import json

from bson.objectid import ObjectId
from flask import jsonify, make_response, request
from flask_restful import Api, Resource

from just_api import mongo
from just_api.arg_parsers import item_arg_parser, order_arg_parser

api = Api()


class Orders(Resource):
    """ Restaurant orders resource class.

    Methods
    -------
    get
        Returns all orders of the restaurant as json.
    post
        Creates new specific order, writes it to the database and returns id.

    """

    def get(self):
        return make_response(jsonify(list(mongo.db.order.find({}))), 200)

    def post(self):
        args = order_arg_parser.parse_args()
        args['order_date'] = datetime.datetime.now()
        args['order_pickup_date'] = ''
        inserted_id = mongo.db.order.insert_one(args).inserted_id
        return make_response(jsonify({'_id': inserted_id}), 201)


class SpecificOrder(Resource):
    """ Specific order resource class.

    Methods
    -------
    get
        Returns information about the order with the given id as json.
    put
        Updates information about the order with the given id, returns id.
    delete
        Deletes the order by the given id and returns id.

    """

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


class ClosedOrders(Resource):
    """ Restaurant orders resource class.

    Methods
    -------
    get
        Returns all orders of the restaurant as json.
    post
        Creates new specific order, writes it to the database and returns id.

    """

    def get(self):
        # TODO: get all closed orders from mongo
        return make_response(jsonify(list(mongo.db.order.find({}))), 200)


class WaitingOrders(Resource):
    """ Restaurant orders resource class.

    Methods
    -------
    get
        Returns all orders of the restaurant as json.
    post
        Creates new specific order, writes it to the database and returns id.

    """

    def get(self):
        # TODO: get all waiting orders from mongo
        return make_response(jsonify(list(mongo.db.order.find({}))), 200)


class Menu(Resource):
    """ Restaurant menu resource class.

    Methods
    -------
    get
        Returns all items from current menu of the restaurant as json.
    post
        Creates new menu item, writes it to the database and returns id.

    """

    def get(self):
        return make_response(jsonify(list(mongo.db.menu.find({}))), 200)

    def post(self):
        args = item_arg_parser.parse_args()
        inserted_id = mongo.db.menu.insert_one(args).inserted_id
        return make_response(jsonify({'_id': inserted_id}), 201)


class MenuItem(Resource):
    """ Restaurant menu item resource class.

    Methods
    -------
    get
        Returns information about the item with the given id as json.
    put
        Updates information about the item with the given id, returns id.
    delete
        Delete the item by the given id and returns id.

    """

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


api.add_resource(Orders, '/orders')
api.add_resource(SpecificOrder, '/orders/<ObjectId:_id>')
api.add_resource(ClosedOrders, '/orders/closed')
api.add_resource(WaitingOrders, '/orders/waiting')
api.add_resource(MenuItem, '/menu/<ObjectId:_id>')
api.add_resource(Menu, '/menu')
