# -*- coding: utf-8 -*-

from . import website
from . import views


website.add_url_rule('/', 'index', views.index)
