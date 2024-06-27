from flask_restx import Namespace, Resource, fields
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
        from backend.models.movie import Movie

        """Return all movies"""

        movies = Movie.query.all()
        if not movies:
            return "No Movie in Available"
        return [{movie.id: movie.to_json()} for movie in movies], HTTPStatus.OK


@movie_api.route("/<int:movie_id>")
class Return_all_movies(Resource):
    """movie routes"""

    def get(self, movie_id):
        from backend.models.movie import Movie

        """Return a movies"""

        movie = Movie.query.get(movie_id)
        if not movie:
            return "No Movie in Available"
        return {movie.id: movie.to_json()}, HTTPStatus.OK


@movie_api.route("/post")
class Post_movie(Resource):
    @movie_api.expect(post_movie)
    def post(self):
        from backend.models.movie import Movie

        data = movie_api.payload

        if not data:
            return "Failed"

        movie = Movie(title=data["title"],
                      release_date=datetime.now(),
                      description=data["description"],
                      movie_fee=int(data["fee"]))
        movie.save()

        return "Created", HTTPStatus.CREATED
