from typing_extensions import Required
from backend.models.user import User
from flask_restx import Resource, Namespace, fields

login_api = Namespace("login", description="Login related operations")

login_model = login_api.model(
    "Login", {
        "username": fields.String(Required=True),
        "password": fields.String(Required=True)
    })


@login_api.route("/")
class Login(Resource):

    @login_api.expect(login_model)
    def post(self):
        data = login_api.payload
        if not data:
            return "Enter Data"
        user = User.query.filter_by(username=data.get("username")).first()
        if user is not None and user.check_password(data.get("password")):
            return "Login successful"
        else:
            return "Invalid username or password"
