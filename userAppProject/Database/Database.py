import mysql.connector


class Connection:
    def get_connection(app):
        app.config["SECRET_KEY"] = "pl33nkmlaf1b391d1998b68ijaw2y3"
        config = {
            'user': 'root',
            'host': 'mysql_db',
            'port': '3306',
            'password': 'ckvb1998',
            'database': 'usersDataBase'
        }
        connection = mysql.connector.connect(**config)
        return connection
