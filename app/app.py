import os
import flask
import models
import tools
from flask_admin import Admin
from flask_admin.contrib.peewee import ModelView

app = flask.Flask(__name__)

# Add the Flask-Admin endpoint (/admin/)
admin = Admin(app, name="App", template_mode='bootstrap3')
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

