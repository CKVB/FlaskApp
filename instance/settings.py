import os

SECRET_KEY = os.environ.get("SECRET_KEY")
FLASK_ENV = os.environ.get("FLASK_ENV")
SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') #.replace("://", "ql://", 1)
SQLALCHEMY_TRACK_MODIFICATIONS = os.environ.get("SQLALCHEMY_TRACK_MODIFICATIONS") in ("True")
SQLALCHEMY_ECHO = os.environ.get("SQLALCHEMY_ECHO") in ("True")
