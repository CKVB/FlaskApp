from flask import Flask
from .models import db


def create_app(configuration_file="settings.py"):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_pyfile(configuration_file)
    db.init_app(app)
    with app.app_context():
        from .views import user_api, swagger_ui
        app.register_blueprint(user_api)
        app.register_blueprint(swagger_ui)
        db.create_all()
        return app
