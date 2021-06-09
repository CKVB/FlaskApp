from flask import jsonify
from ..models import User


def get_all_users(*args):
    current_user, = args
    if not current_user.admin:
        return jsonify({"message": "Not Enough Permissions!"}), 403
    users = User.query.all()
    output = []
    for user in users:
        user_data = {}
        user_data['global_user_id'] = user.global_user_id
        user_data['user_name'] = user.user_name
        user_data['user_password'] = user.user_password
        user_data['admin'] = user.admin
        output.append(user_data)
    if output:
        return jsonify({"users": output}), 200
    else:
        return jsonify({"message": "Empty Database!"}), 204
