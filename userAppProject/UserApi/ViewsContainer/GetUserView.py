from Factory.Factory import Factory
from flask import jsonify


def get_user(*args):

    current_global_user_id, required_user_id, mysql = args

    is_admin_obj = Factory.build("IS_ADMIN")
    is_admin_response = is_admin_obj.is_admin(mysql, current_global_user_id)
    if is_admin_response or current_global_user_id == required_user_id:
        get_user_obj = Factory.build("GET_USER")
        user_data = get_user_obj.get_user(required_user_id, mysql)
        if user_data:
            return jsonify({"user": user_data}), 200
        else:
            return jsonify({"message": "user not found!"}), 404
    else:
        return jsonify({"message": "Not Enough Permissions!"}), 403
