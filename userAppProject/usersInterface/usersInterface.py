from abc import ABCMeta, abstractmethod

class createUserInterface(metaclass = ABCMeta):
	@abstractmethod
	def create_user():
		pass

class deleteUserInterface(metaclass = ABCMeta):
	@abstractmethod
	def delete_user():
		pass

class getAllUsersInterface(metaclass = ABCMeta):
	@abstractmethod
	def get_all_users():
		pass

class getUserInterface(metaclass = ABCMeta):
	@abstractmethod
	def get_user():
		pass

class promoteUserInterface(metaclass = ABCMeta):
	@abstractmethod
	def promote_user():
		pass

class loginUserInterface(metaclass = ABCMeta):
	@abstractmethod
	def login():
		pass

class isAdminInterface(metaclass = ABCMeta):
	@abstractmethod
	def is_admin():
		pass