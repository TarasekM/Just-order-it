import os
from typing import Dict, Union

from flask import Flask
from flask_pymongo import BSONObjectIdConverter, PyMongo

from .config import configs

mongo = PyMongo()


def create_app(config_name: str = None,
               config_dict: Dict[str, Union[str, int]] = None) -> Flask:
    app = Flask(__name__, instance_relative_config=True)

    from just_api.json_encoder import JSONEncoderImproved
    app.json_encoder = JSONEncoderImproved

    if config_name:
        app.config.from_object(configs[config_name])
        configs[config_name].init_app(app)
    elif config_dict:
        app.config.from_mapping(config_dict)

    mongo.init_app(app)
    if mongo.db.last_order_id.find_one({}) is None:
        mongo.db.last_order_id.insert_one({'order_id': 0})
    from .resources import api
    app.url_map.converters['ObjectId'] = BSONObjectIdConverter
    api.init_app(app)

    return app
