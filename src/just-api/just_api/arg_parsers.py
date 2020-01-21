from flask_restful.reqparse import RequestParser


item_arg_parser = RequestParser()
item_arg_parser.add_argument(
    'name', dest='name', type=str, help='(str) Name of the menu item.')
item_arg_parser.add_argument(
    'price', dest='price', type=float, help='(float) Price of the menu item.')
item_arg_parser.add_argument(
    'tags', dest='tags', type=str, action='append', help='(list) Tags of menu item.')
item_arg_parser.add_argument(
    'ingredients', dest='ingredients', type=str, action='append', help='(list) Ingredients of menu item')

order_arg_parser = RequestParser()
order_arg_parser.add_argument(
    'items', dest='items', type=str, action='append', help='(list) IDs of items in the order')
