from flask import jsonify
from ..models import User, db


def delete_user(*args):
    current_user, global_user_id = args
    if not current_user.admin:
        return jsonify({"message": "Not Enough Permissions!"}), 403
    user = User.query.filter_by(global_user_id=global_user_id).first()
    if not user:
        return jsonify({"message": "User Not Found!"}), 404
    db.session.delete(user)
    db.session.commit()
    return jsonify({"message": 'User Deleted!'}), 204
