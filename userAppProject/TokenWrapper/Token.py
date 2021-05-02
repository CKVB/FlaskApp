from functools import wraps
import jwt
from userApp import app
from flask import request, jsonify


def token_required(function):
    @wraps(function)
    def add_feature(*args, **kwargs):
        token = None
        if "x-access-token" in request.headers:
            token = request.headers["x-access-token"]
        if not token:
            return jsonify({"message": "token is missing!"}), 401
        try:
            data = jwt.decode(token, app.config["SECRET_KEY"], algorithms="HS256")
            current_global_user_id = data["global_id"]
        except Exception as ex:
            return jsonify({"message": str(ex)})
        else:
            return function(current_global_user_id, *args, **kwargs)
    return add_feature
