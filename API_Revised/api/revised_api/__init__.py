# -*- coding:utf-8 -*-
from __future__ import absolute_import

from flask import Blueprint, Flask
import flask_restful as resful

from .routes import routes
from .validators import security

@security.scopes_loader
def current_scopes():
    return []

bp = Blueprint('', __name__, static_folder='static')
api = resful.Api(bp, catch_all_404s=True)

for route in routes:
    api.add_resource(route.pop('resource'), *route.pop('urls'), **route)

app = Flask(__name__)
app.register_blueprint(bp)
