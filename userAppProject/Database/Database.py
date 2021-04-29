from flask_mysqldb import MySQL
import os 

class Connection:
	def get_connection(app):
		app.config["SECRET_KEY"] = os.environ.get("SECRET_KEY")
		app.config["MYSQL_HOST"] = os.environ.get("MYSQL_HOST")
		app.config["MYSQL_USER"] = os.environ.get("MySQL_USER")
		app.config["MYSQL_PASSWORD"] = os.environ.get("MYSQL_PASSWORD")
		app.config["MYSQL_DB"] = os.environ.get("MYSQL_DB")
		return MySQL(app)