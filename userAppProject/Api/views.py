from flask import render_template, request, jsonify, make_response, Blueprint, render_template
from Database.Database import Connection
from Users.Factory import Factory
from functools import wraps
from userApp import app
from werkzeug.security import check_password_hash
import jwt
import datetime
 
api = Blueprint("api", __name__)
mysql = Connection.get_connection(app)

def token_required(function):
	@wraps(function)
	def add_feature(*args, **kwargs):
		token = None
		if "x-access-token" in request.headers:
			token = request.headers["x-access-token"]
		if not token:
			return jsonify({"message":"token is missing!"}), 401
		try:
			auth = request.authorization
			if not auth or not auth.username:
				return make_response("Could Not Verity",401)
			cursor = mysql.connection.cursor()
			sql_query = "select guid from users where uname = %s"
			values = [auth.username]
			cursor.execute(sql_query, values)
			current_global_user_id = cursor.fetchone()[0]

			data = jwt.decode(token,app.config["SECRET_KEY"],algorithms="HS256")
		
		except Exception as ex:
			return jsonify({"message":str(ex)})
		else:
			if data["global_id"] != current_global_user_id:
				return jsonify({"message":"Invalid Token!"})
			else:
				return function(current_global_user_id, *args, **kwargs)
	return add_feature

@api.route("/user", methods = ["POST"])
def create_new_user(global_user_id):
	create_user_obj = Factory.build("CREATE_USER")
	status = create_user_obj.create_user(mysql)
	if status:
		return jsonify({"message":"user created!"})
	else:
		return jsonify({"message":"failed to create user!"})

@api.route("/users", methods = ["GET"])
@token_required
def get_all_users(global_user_id):
	is_admin_obj = Factory.build("IS_ADMIN")
	status = is_admin_obj.is_admin(mysql, global_user_id)
	if not status:
		return jsonify({"message":"Not Enough Permissions!"})
	get_users_obj = Factory.build("GET_ALL_USERS")
	users = get_users_obj.get_all_users(mysql)
	if users:
		return jsonify({"users":users})
	else:
		return jsonify({"message":"Empty Database!"})

@api.route("/user/<current_user_id>", methods = ["GET"])
@token_required
def get_user(current_global_user_id, current_user_id):
	get_user_obj = Factory.build("GET_USER")
	user_data = get_user_obj.get_user(current_user_id, mysql)
	if user_data:
		return jsonify({"user":user_data})
	else:
		return jsonify({"message":"user not found!"})

@api.route("/user/<delete_user_id>", methods = ["DELETE"])
@token_required
def delete_user(current_global_user_id, delete_user_id):
	is_admin_obj = Factory.build("IS_ADMIN")
	response = is_admin_obj.is_admin(mysql, current_global_user_id)
	if response:
		delete_user_obj = Factory.build("DELETE_USER")
		status = delete_user_obj.delete_user(delete_user_id, mysql)
		if status:
			return jsonify({"message":"User Deleted!"})
		else:
			return jsonify({"message":"User Not Found!"})
	else:
		return jsonify({"message":"Not Enough Permissions!"})

@api.route("/user/<promote_user_id>", methods = ["PUT"])
@token_required
def promote_user(current_global_user_id, promote_user_id):
	is_admin_obj = Factory.build("IS_ADMIN")
	response = is_admin_obj.is_admin(mysql, current_global_user_id)
	if response:
		promote_user_obj = Factory.build("PROMOTE_USER")
		status = promote_user_obj.promote_user(promote_user_id, mysql)
		if status:
			return jsonify({"message":"User Promoted!"})
		else:
			return jsonify({"message":"User Not Found!"})
	else:
		return jsonify({"message":"Not Enough Permissions!"})

@api.route("/login", methods = ["GET"])
def login():
	login_user_obj = Factory.build("LOGIN") 
	response = login_user_obj.login(app, mysql)
	return response