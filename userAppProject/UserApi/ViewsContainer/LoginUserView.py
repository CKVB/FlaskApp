from Factory.Factory import Factory


def login(*args):
    app, mysql = args
    login_user_obj = Factory.build("LOGIN")
    response = login_user_obj.login(app, mysql)
    return response
