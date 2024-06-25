from flask_restx import Namespace, Resource, fields
from backend.models.user import User
from datetime import datetime
from http import HTTPStatus

movie_api = Namespace("movies",  description="movie list")
post_movie = movie_api.model("post movie", {
    "title": fields.String(required=True),
    "description": fields.String(required=True),
    "fee": fields.String(required=True),

})


@movie_api.route("/")
class Return_all_movies(Resource):
    """movie routes"""

    def get(self):
        data = movie_api.payload
