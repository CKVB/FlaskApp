from flask import request, jsonify
from ..models import User, db
from werkzeug.security import generate_password_hash
import uuid


def create_user():
    data = request.get_json()
    user = User.query.filter_by(user_name=data["user_name"]).first()
    if not user:
        hashed_password = generate_password_hash(data["user_password"], method="sha256")
        try:
            new_user = User(global_user_id=str(uuid.uuid4()), user_name=data["user_name"], user_password=hashed_password, admin=False)
        except Exception as ex:
            return jsonify({"message": str(ex)})
        else:
            db.session.add(new_user)
            db.session.commit()
            return jsonify({"message": "User Created!"}), 201
    else:
        return jsonify({"message": "user name is already taken!"}), 409