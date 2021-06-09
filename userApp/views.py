from flask import Blueprint
from flask_swagger_ui import get_swaggerui_blueprint
from .routes.getView import get_view
from .models import User, db
from .token import token_required


swagger_url_prefix = "/swagger"
swagger_file_path = "/static/swagger_doc.yml"
swagger_ui = get_swaggerui_blueprint(swagger_url_prefix, swagger_file_path)

user_api = Blueprint("user_api", __name__)


@user_api.route('/login', methods=["GET"])
def login():
    return get_view("LOGIN")


@user_api.route("/")
def index():
    user = User.query.filter_by(user_name="king@mail.com").first()
    if not user:
        new_user = User(global_user_id="a3a4268f-3e2c-4dda-862a-25ce8533a940", user_name="king@mail.com", user_password="sha256$W9WC0zo4$6b6568dc9c88b913967cc5147fab2401c7ee5a813cd08e4757031b3126dd3d1d", admin=True)
        db.session.add(new_user)
        db.session.commit()
    return "Hello!"


@user_api.route("/users", methods=["GET"])
@token_required
def get_all_users(current_user):
    return get_view("GET_ALL_USERS", current_user)


@user_api.route("/user", methods=["POST"])
def create_user():
    return get_view("CREATE_USER")


@user_api.route("/user/<global_user_id>", methods=["GET"])
@token_required
def get_user(current_user, global_user_id):
    return get_view("GET_USER", current_user, global_user_id)


@user_api.route('/user/<global_user_id>', methods=['PUT'])
@token_required
def promote_user(current_user, global_user_id):
    return get_view("PROMOTE_USER", current_user, global_user_id)


@user_api.route('/user/<global_user_id>', methods=['DELETE'])
@token_required
def delete_user(current_user, global_user_id):
    return get_view("DELETE_USER", current_user, global_user_id)
