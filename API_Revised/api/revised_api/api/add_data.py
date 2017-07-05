# -*- coding: utf-8 -*-
from __future__ import absolute_import, print_function

from flask import request, g
from redis import Redis

from . import Resource
from .. import schemas
import time
from .helper_methods import HelperMethods
from .database_wrapper import DatabaseWrapper

class AddData(Resource):

    def post(key, timestamp, data):

        db = DatabaseWrapper()

        checked_key = db.check_key_in_enabled_list(key)

        checked_time = HelperMethods.check_time(timestamp)

        db.post_new_data(key, data, timestamp)

        return "Data uploaded successfully"


