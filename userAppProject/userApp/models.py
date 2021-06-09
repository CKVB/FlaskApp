from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    global_user_id = db.Column(db.String(200))
    user_name = db.Column(db.String(30), unique=True)
    user_password = db.Column(db.String(200))
    admin = db.Column(db.Boolean)
