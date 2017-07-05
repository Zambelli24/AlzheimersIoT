# -*- coding: utf-8 -*-
from __future__ import absolute_import, print_function

from flask import request, g

from . import Resource
from .. import schemas
import string
from .helper_methods import HelperMethods
from .database_wrapper import DatabaseWrapper

class AddKey(Resource):

    def post(key):

        db = DatabaseWrapper()

        if HelperMethods.check_incorrect_key_format(key):
            raise Exception('The key is not in the specified format.')

        if db.check_key_is_enabled(key):
            return "The specified key has already been enabled"

        db.add_key(key)

        return "Key successfully enabled"
