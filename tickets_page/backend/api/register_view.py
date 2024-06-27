from flask_restx import Namespace, Resource, fields
from datetime import datetime
from http import HTTPStatus

register_api = Namespace("register",  description="register a user")

reg = register_api.model("register", {
    "username": fields.String(required=True),
    "email": fields.String(required=True),
    "password": fields.String(required=True)

})


@register_api.route("/")
class Return_all_movies(Resource):
    """movie routes"""

    @register_api.expect(reg)
    def post(self):
        from backend.models.user import User

        data = register_api.payload
        if not data:
            return "Enter a valid data", 404
        try:
            print(data)
            user = User(username=data.get("username"),
                        email=data.get("email"))
            user.set_password(data.get("password"))
            user.save()
        except Exception as e:
            return f"Error {e}"

        return "Created"
