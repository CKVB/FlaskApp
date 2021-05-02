from usersInterface.usersInterface import createUserInterface
from flask import request
from werkzeug.security import generate_password_hash
import uuid


class CreateUser(createUserInterface):
    def create_user(self, mysql):
        user_data = request.get_json()
        global_user_id = str(uuid.uuid4())
        user_name = user_data["user_name"]
        user_password = generate_password_hash(user_data["user_password"], method="sha256")
        admin = False

        sql_query = "insert into users (guid,uname,upsw,admin) values (%s, %s, %s, %s)"
        values = [global_user_id, user_name, user_password, admin]
        cursor = mysql.connection.cursor()
        status = cursor.execute(sql_query, values)
        mysql.connection.commit()
        return status
