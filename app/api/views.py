# -*- coding: utf-8 -*-

from flask import jsonify


def hello():
    return jsonify(message='hello api')
