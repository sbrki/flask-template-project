import os
import flask
import models
import tools
from flask_basicauth import BasicAuth
from flask_admin import Admin
from flask_admin.contrib.peewee import ModelView
from flask_wtf import FlaskForm             # Not actually used in this project, but handy
from wtforms import StringField             # same as ^
from wtforms.validators import DataRequired # same as ^

app = flask.Flask(__name__)

# Basicauth configuration, for using the flask-admin interface
app.config["BASIC_AUTH_USERNAME"]="admin"
app.config["BASIC_AUTH_PASSWORD"]="1234" # Change this, seriously
basic_auth = BasicAuth(app)

# Add the Flask-Admin endpoint (/admin/)
admin = Admin(app, name="App", template_mode='bootstrap3')
# A workaround that enables use of basicauth
class ModelView(ModelView):
    def is_accessible(self):
        if not basic_auth.authenticate():
            raise AuthException('Not authenticated.')
        else:
            return True
    def inaccessible_callback(self, name, **kwargs):
        return redirect(basic_auth.challenge())
from werkzeug.exceptions import HTTPException, Response
class AuthException(HTTPException):
    def __init__(self, message):
        super().__init__(message, Response(
            "You could not be authenticated. Please refresh the page.", 401,
            {'WWW-Authenticate': 'Basic realm="Login Required"'})
        )

# Add your flask-admin models here!
admin.add_view(ModelView(models.Example))



@app.before_first_request
def prepare_database():
    """
    Prepares the database (connection) before the first request is recieved.
    """
    models.db.connect()
    models.try_create_tables()


@app.route("/")
def index():
	return flask.render_template("bs3.html")


if __name__ == "__main__":
	DEBUG = False
	if os.environ.get("DEBUG") != None:
		if os.environ.get("DEBUG").lower() == "true":
			DEBUG = True

	app.run(
		host="0.0.0.0",
		port=80,
		debug=DEBUG
		)

