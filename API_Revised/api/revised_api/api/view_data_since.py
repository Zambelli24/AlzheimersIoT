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

        if not db.check_key_is_enabled(key):
            raise Exception('The specified key does not exist')

        checked_time = HelperMethods.check_time(timestamp)

        return db.get_data_since(key, checked_time)

