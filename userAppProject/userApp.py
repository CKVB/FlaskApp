from flask import Flask
from flask_swagger_ui import get_swaggerui_blueprint

app = Flask(__name__)

from UserApi.views import user_api

swagger_url_prefix = '/swagger'
swagger_api_url = '/static/swagger_doc.yml'
swagger_ui_blueprint = get_swaggerui_blueprint(swagger_url_prefix, swagger_api_url)

app.register_blueprint(swagger_ui_blueprint, url_prefix=swagger_url_prefix)

app.register_blueprint(user_api)

if __name__ == '__main__':
    app.run()
