# -*- coding: utf-8 -*-

###
### DO NOT CHANGE THIS FILE
###
### The code is auto generated, your change will be overwritten by
### code generating.
###
from __future__ import absolute_import

from .api.view_data_since import ViewDataSince
from .api.add_key import AddKey
from .api.view_most_recent_data import ViewMostRecentData
from .api.add_data import AddData
from .api.keys_list import KeysList


routes = [
    dict(resource=ViewDataSince, urls=['/view_data_since'], endpoint='view_data_since'),
    dict(resource=AddKey, urls=['/add_key'], endpoint='add_key'),
    dict(resource=ViewMostRecentData, urls=['/view_most_recent_data'], endpoint='view_most_recent_data'),
    dict(resource=AddData, urls=['/add_data'], endpoint='add_data'),
    dict(resource=KeysList, urls=['/keys_list'], endpoint='keys_list'),
]