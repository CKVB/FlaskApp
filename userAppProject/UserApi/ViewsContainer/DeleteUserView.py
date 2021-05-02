from Factory.Factory import Factory
from flask import jsonify


def delete_user(*args):

    current_global_user_id, delete_user_id, mysql = args

    is_admin_obj = Factory.build("IS_ADMIN")
    response = is_admin_obj.is_admin(mysql, current_global_user_id)
    if response:
        delete_user_obj = Factory.build("DELETE_USER")
        status = delete_user_obj.delete_user(delete_user_id, mysql)
        if status:
            return jsonify({"message": "User Deleted!"}), 204
        else:
            return jsonify({"message": "User Not Found!"}), 404
    else:
        return jsonify({"message": "Not Enough Permissions!"}), 403
