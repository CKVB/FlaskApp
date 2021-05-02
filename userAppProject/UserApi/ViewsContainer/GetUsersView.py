from Factory.Factory import Factory
from flask import jsonify


def get_all_users(*args):

    global_user_id, mysql = args

    is_admin_obj = Factory.build("IS_ADMIN")
    status = is_admin_obj.is_admin(mysql, global_user_id)
    if not status:
        return jsonify({"message": "Not Enough Permissions!"}), 403
    get_users_obj = Factory.build("GET_ALL_USERS")
    users = get_users_obj.get_all_users(mysql)
    if users:
        return jsonify({"users": users}), 200
    else:
        return jsonify({"message": "Empty Database!"}), 204
