# -*- coding: utf-8 -*-

from flask import Flask

from config import config_map


def create_app(config='default'):
    app = Flask(__name__)
    app.config.from_object(config_map[config])

    from .website import website
    app.register_blueprint(website)

    return app
