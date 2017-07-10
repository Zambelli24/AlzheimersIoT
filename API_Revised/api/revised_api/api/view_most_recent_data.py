# -*- coding: utf-8 -*-
from __future__ import absolute_import, print_function

from flask import request, g

from . import Resource
from .. import schemas
from .helper_methods import HelperMethods
from .database_wrapper import DatabaseWrapper

class ViewMostRecentData(Resource):

    def get(key):

        db = DatabaseWrapper()

        if not db.check_key_is_enabled(key):
            raise Exception('The specified key does not exist')

        return db.get_most_recent_data(key)
