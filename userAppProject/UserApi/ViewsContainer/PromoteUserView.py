from Factory.Factory import Factory
from flask import jsonify


def promote_user(*args):

    current_global_user_id, promote_user_id, mysql = args

    is_admin_obj = Factory.build("IS_ADMIN")
    response = is_admin_obj.is_admin(mysql, current_global_user_id)
    if response:
        promote_user_obj = Factory.build("PROMOTE_USER")
        status = promote_user_obj.promote_user(promote_user_id, mysql)
        if status:
            return jsonify({"message": "User Promoted!"}), 204
        else:
            return jsonify({"message": "User Not Found!"}), 404
    else:
        return jsonify({"message": "Not Enough Permissions!"}), 403
