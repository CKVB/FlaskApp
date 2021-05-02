from usersInterface.usersInterface import getAllUsersInterface


class GetUsers(getAllUsersInterface):
    def get_all_users(self, mysql):
        sql_query = "select * from users"
        cursor = mysql.connection.cursor()
        cursor.execute(sql_query)
        users_data = cursor.fetchall()
        users_info = []
        if users_data:
            for user in users_data:
                user_data = {}
                user_data["user_id"] = user[0]
                user_data["global_id"] = user[1]
                user_data["user_name"] = user[2]
                user_data["user_password"] = user[3]
                user_data["admin"] = user[4]
                users_info.append(user_data)
            return users_info
        else:
            return None
