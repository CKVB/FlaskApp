from usersInterface.usersInterface import isAdminInterface


class IsAdmin(isAdminInterface):
    def is_admin(self, mysql, global_user_id):
        cursor = mysql.cursor()
        sql_query = "select admin from users where guid = %s"
        values = [global_user_id]
        cursor.execute(sql_query, values)
        data = cursor.fetchone()[0]
        return data
