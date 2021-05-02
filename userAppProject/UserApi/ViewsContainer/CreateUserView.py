from Factory.Factory import Factory
from flask import jsonify


def create_new_user(*args):

    mysql, = args

    create_user_obj = Factory.build("CREATE_USER")
    status = create_user_obj.create_user(mysql)
    if status:
        return jsonify({"message": "user created!"}), 201
    else:
        return jsonify({"message": "failed to create user!"}), 400
