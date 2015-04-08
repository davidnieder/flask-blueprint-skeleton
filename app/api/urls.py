# -*- coding: utf-8 -*-

from . import api
from . import views


api.add_url_rule('/', 'hello', views.hello)
