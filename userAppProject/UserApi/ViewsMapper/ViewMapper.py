from UserApi.ViewsContainer.CreateUserView import create_new_user
from UserApi.ViewsContainer.DeleteUserView import delete_user
from UserApi.ViewsContainer.GetUsersView import get_all_users
from UserApi.ViewsContainer.GetUserView import get_user
from UserApi.ViewsContainer.IndexView import index
from UserApi.ViewsContainer.LoginUserView import login
from UserApi.ViewsContainer.PromoteUserView import promote_user

mapper = {
    "CREATE_NEW_USER": create_new_user,
    "DELETE_USER": delete_user,
    "GET_USERS": get_all_users,
    "GET_USER": get_user,
    "INDEX": index,
    "LOGIN": login,
    "PROMOTE_USER": promote_user
}


def get_view(view_name, *args):
    return mapper.get(view_name)(*args)
