from flask import Blueprint
from Database.Database import Connection
from TokenWrapper.Token import token_required
from UserApi.ViewsMapper.ViewMapper import get_view
from userApp import app

user_api = Blueprint("user_api", __name__)
mysql = Connection.get_connection(app)


@user_api.route("/")
def index_view():
    return get_view("INDEX")


@user_api.route("/user", methods=["POST"])
def create_new_user_view():
    return get_view("CREATE_NEW_USER", mysql)


@user_api.route("/users", methods=["GET"])
@token_required
def get_all_users_view(global_user_id):
    return get_view("GET_USERS", global_user_id, mysql)


@user_api.route("/user/<required_user_id>", methods=["GET"])
@token_required
def get_user_view(current_global_user_id, required_user_id):
    return get_view("GET_USER", current_global_user_id, required_user_id, mysql)


@user_api.route("/user/<delete_user_id>", methods=["DELETE"])
@token_required
def delete_user_view(current_global_user_id, delete_user_id):
    return get_view("DELETE_USER", current_global_user_id, delete_user_id, mysql)


@user_api.route("/user/<promote_user_id>", methods=["PUT"])
@token_required
def promote_user_view(current_global_user_id, promote_user_id):
    return get_view("PROMOTE_USER", current_global_user_id, promote_user_id, mysql)


@user_api.route("/login", methods=["GET"])
def login_view():
    return get_view("LOGIN", app, mysql)
