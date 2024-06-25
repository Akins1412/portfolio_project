from flask_restx import Namespace, Resource, fields
from backend.models.admin_model import Admin
from backend.models.movie import Movie
from datetime import datetime


admin_api = Namespace("admin", description="all admin operations")


admin_model = admin_api.model("Admin", {
    "username": fields.String(required=True),
    "email": fields.String(required=True),
    "password": fields.String(required=True)
})


@admin_api.route("/register")
class Create_Admin(Resource):

    @admin_api.expect(admin_model)
    def post(self):
        data = admin_api.payload
        if not data:
            return "enter valid credentials"

        check_username = Admin.query.filter_by(
            username=data.get("username")).first()
        check_email = Admin.query.filter_by(
            email=data.get("email")).first()
        if check_username or check_email:
            return "Username or email has been used"

        admin = Admin(username=data.get("username"), email=data.get("email"))
        admin.set_password(data.get("password"))
        admin.save()

        return "Created"


# @admin_api.route("/movies")
# class Post_Movies(Resource):
#     @admin_api.doc(params={'id': 'An ID'})
#     def post(self):
#         data1 = admin_api.param
#         print(data1)
#         data = Movie(title="first Movie",
#                      release_date=datetime.utcnow(), description="A year of the Dragon", movie_fee=300)
#         data.save()
#         return "addded"
