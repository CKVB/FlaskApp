from .Login import login
from .GetAllUsers import get_all_users
from .CreateUser import create_user
from .GetUser import get_user
from .PromoteUser import promote_user
from .DeleteUser import delete_user

view_mapper = {
    "LOGIN": login,
    "GET_ALL_USERS": get_all_users,
    "CREATE_USER": create_user,
    "GET_USER": get_user,
    "PROMOTE_USER": promote_user,
    "DELETE_USER": delete_user
}


def get_view(view, *args):
    return view_mapper.get(view)(*args)
