from flask import request, jsonify
import jwt
import os
import datetime
from werkzeug.security import check_password_hash
from ..models import User


def login():
    auth = request.authorization
    user_data = User.query.filter_by(user_name=auth.username).first()
    if not user_data:
        return jsonify({"message": "User Not Found!"}), 404
    if check_password_hash(user_data.user_password, auth.password):
        token = jwt.encode({"global_user_id": user_data.global_user_id, "exp": datetime.datetime.utcnow() + datetime.timedelta(minutes=30)}, os.environ.get("SECRET_KEY"),  algorithm="HS256")
        return jsonify({"token": token}), 200
    else:
        return jsonify({"message": "Invalid Credentials!"}), 401