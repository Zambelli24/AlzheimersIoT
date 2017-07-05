# -*- coding: utf-8 -*-
from __future__ import absolute_import, print_function

from flask import request, g

from . import Resource
from .. import schemas
from .helper_methods import HelperMethods
from .database_wrapper import DatabaseWrapper

class ViewDataSince(Resource):

    def get(key, timestamp):
        db = DatabaseWrapper()
        checked_key = db.check_key_in_enabled_list(key)
        checked_time = int(HelperMethods.check_time(timestamp))

        ret_list = []

        return db.get_data_since(checked_key, checked_time)

