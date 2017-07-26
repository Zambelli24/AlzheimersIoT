# -*- coding: utf-8 -*-
from __future__ import absolute_import, print_function

from flask import request, g

from . import Resource
from .. import schemas
import time
from .helper_methods import HelperMethods
from .database_wrapper import DatabaseWrapper
import json

class AddData(Resource):

    def post(key, timestamp, data):

        db = DatabaseWrapper()

        if not db.check_key_is_enabled(key):
            raise Exception('The specified key does not exist')

        checked_time = HelperMethods.check_time(timestamp)

        data = json.loads(data)

        db.post_new_data(key, data, timestamp)

        return "Data uploaded successfully"


