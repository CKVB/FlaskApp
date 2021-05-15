import mysql.connector
import os


class Connection:
    def get_connection(app):
        app.config["SECRET_KEY"] = os.environ.get("SECRET_KEY")
        config = {
            'user': os.getenv("USER"),
            'host': os.getenv("HOST"),
            'port': os.getenv("PORT"),
            'password': os.getenv("PASSWORD"),
            'database': os.getenv("DATABASE")
        }
        connection = mysql.connector.connect(**config)
        return connection
