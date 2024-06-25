
from backend.models.user import User
from flask_restx import Resource, Namespace, fields
from flask_jwt_extended import create_access_token, jwt_required
from backend.models.admin_model import Admin
from http import HTTPStatus

auth = Namespace("auth", description="Login related operations")

login_model = auth.model(
    "Login", {
        "username": fields.String(Required=True),
        "password": fields.String(Required=True)
    })


@auth.route("/login")
class Login(Resource):

    @auth.expect(login_model)
    def post(self):
        data = auth.payload
        if not data:
            return "Enter Data"
        user = User.query.filter_by(username=data.get("username")).first()
        if user is not None and user.check_password(data.get("password")):
            return {"access token": create_access_token(identity=user.to_json())}
        else:
            return "Invalid username or password", HTTPStatus.NOT_FOUND


@auth.route("/admin")
class Admin_login(Resource):

    @auth.expect(login_model)
    @jwt_required()
    def post(self):
        data = auth.payload
        if not data:
            return "Enter Data"
        admin = Admin.query.filter_by(username=data.get("username")).first()
        if admin is not None and admin.check_password(data.get("password")):
            return {"access token": create_access_token(identity=admin.to_json())}, HTTPStatus.OK
        else:
            return "Invalid username or password", HTTPStatus.NOT_FOUND
