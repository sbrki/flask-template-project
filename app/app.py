import os
import flask
import database


app = flask.Flask(__name__)


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

