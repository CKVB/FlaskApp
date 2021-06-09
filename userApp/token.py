from functools import wraps
from flask import request, jsonify
import jwt
import os
from .models import User


def token_required(function):
    @wraps(function)
    def add_feature(*args, **kwargs):
        token = None
        if 'x-access-token' in request.headers:
            token = request.headers['x-access-token']
        if not token:
            return jsonify({"message": "Token is missing!"}), 401
        try:
            data = jwt.decode(token, os.environ.get("SECRET_KEY"), algorithms="HS256")
            current_user = User.query.filter_by(global_user_id=data["global_user_id"]).first()
        except Exception as ex:
            return jsonify({"message": str(ex)})
        else:
            return function(current_user, *args, **kwargs)
    return add_feature
