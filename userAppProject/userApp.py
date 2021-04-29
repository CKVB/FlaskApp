from flask import Flask

app = Flask(__name__)

from Api.views import api
from Site.views import site

app.register_blueprint(api)
app.register_blueprint(site)

if __name__ == '__main__':
	app.run()