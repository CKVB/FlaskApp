from usersInterface.usersInterface import loginUserInterface
from flask import request, jsonify
from werkzeug.security import check_password_hash
import jwt
import datetime


class Login(loginUserInterface):
    def login(self, app, mysql):
        auth = request.authorization
        cursor = mysql.cursor()
        sql_query = "select guid,upsw from users where uname = %s"
        values = [auth.username]
        cursor.execute(sql_query, values)
        user_data = cursor.fetchone()
        if user_data:
            global_user_id, user_password = user_data
            if not check_password_hash(user_password, auth.password):
                return jsonify({"message": "Invalid Credentials!"}), 401
            else:
                token = jwt.encode({"global_id": global_user_id, "exp": datetime.datetime.utcnow()+datetime.timedelta(minutes=10)}, app.config["SECRET_KEY"], algorithm="HS256")
                return jsonify({"token": token}), 200
        else:
            return jsonify({"message": "User Not Found!"}), 404
