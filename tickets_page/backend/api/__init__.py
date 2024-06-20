from flask import Blueprint
from flask_restx import Api
from backend.api.user_view import user_api

blueprint = Blueprint('api', __name__)
api = Api(blueprint)

api.add_namespace(user_api)
