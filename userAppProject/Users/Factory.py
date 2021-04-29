from Users.AdminUser import IsAdmin
from Users.CreateUser import CreateUser
from Users.DeleteUser import DeleteUser
from Users.GetAllUsers import GetUsers
from Users.GetUser import GetUser
from Users.LoginUser import Login
from Users.PromoteUser import PromoteUser

class Factory:
	mappers = {
		"IS_ADMIN" : IsAdmin,
		"CREATE_USER" : CreateUser,
		"DELETE_USER" : DeleteUser,
		"GET_ALL_USERS" : GetUsers,
		"GET_USER" : GetUser,
		"LOGIN" : Login,
		"PROMOTE_USER" : PromoteUser,
	}
	@classmethod
	def build(cls, mapper):
		return cls.mappers[mapper]()