# -*- coding: utf-8 -*-
from __future__ import absolute_import, print_function

from flask import request, g

from . import Resource
from .. import schemas
from .database_wrapper import DatabaseWrapper

class KeysList(Resource):

    def get():

        db = DatabaseWrapper()

        return db.get_keys()