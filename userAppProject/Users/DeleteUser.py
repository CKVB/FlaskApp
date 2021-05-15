from usersInterface.usersInterface import deleteUserInterface


class DeleteUser(deleteUserInterface):
    def delete_user(self, global_id, mysql):
        cursor = mysql.cursor()
        sql_query = "delete from users where guid = %s"
        values = [global_id]
        status = cursor.execute(sql_query, values)
        if not status:
            mysql.commit()
            return True
        return None
