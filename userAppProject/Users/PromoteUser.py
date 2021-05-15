from usersInterface.usersInterface import promoteUserInterface


class PromoteUser(promoteUserInterface):
    def promote_user(self, global_id, mysql):
        cursor = mysql.cursor()
        sql_query = "update users set admin = %s where guid = %s"
        values = [True, global_id]
        status = cursor.execute(sql_query, values)
        if not status:
            mysql.commit()
            return True
        else:
            return False
