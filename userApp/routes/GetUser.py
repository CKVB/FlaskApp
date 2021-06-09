from flask import jsonify
from ..models import User


def get_user(*args):
    current_user, global_user_id = args
    if not current_user.admin:
        return jsonify({"message": "Not Enough Permissions!"}), 403
    user = User.query.filter_by(global_user_id=global_user_id).first()
    if not user:
        return jsonify({"message": "User Not Found!"}), 404
    user_data = {}
    user_data['global_user_id'] = user.global_user_id
    user_data['user_name'] = user.user_name
    user_data['user_password'] = user.user_password
    user_data['admin'] = user.admin
    return jsonify({"user": user_data}), 200
