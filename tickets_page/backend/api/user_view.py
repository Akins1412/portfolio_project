from flask_restx import Resource, Namespace

user_api = Namespace("users", description="User related operations")


@user_api.route("/")
class Get_users(Resource):

  def get(self):
    return "it works"
