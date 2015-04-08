# -*- coding: utf-8 -*-

from flask import Blueprint


website = Blueprint('website', __name__, template_folder='../templates/website')

from . import urls
