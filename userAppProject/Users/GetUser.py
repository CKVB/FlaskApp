from usersInterface.usersInterface import getUserInterface


class GetUser(getUserInterface):
    def get_user(self, global_id, mysql):
        cursor = mysql.connection.cursor()
        sql_query = "select * from users where guid = %s"
        values = [global_id]
        cursor.execute(sql_query, values)
        user_data = cursor.fetchone()
        if user_data:
            user_info = {}
            user_info["user_id"] = user_data[0]
            user_info["global_id"] = user_data[1]
            user_info["user_name"] = user_data[2]
            user_info["user_password"] = user_data[3]
            user_info["admin"] = user_data[4]
            return user_info
        else:
            return None
