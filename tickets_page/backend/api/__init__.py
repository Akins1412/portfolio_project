from flask import Blueprint
from flask_restx import Api
from backend.api.user_view import user_api
from backend.api.login_view import login_api
from backend.api.movie_view import movie_api

blueprint = Blueprint('api', __name__, url_prefix="/api/v1")
api = Api(blueprint)

api.add_namespace(user_api)
api.add_namespace(login_api)
api.add_namespace(movie_api)
