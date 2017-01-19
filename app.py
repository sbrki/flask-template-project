import flask
import models


app = flask.Flask(__name__, instance_relative_config=True)


# Load Dev or Production config
app.config.from_object("config.Dev")

# Production and sensitive data (overwrites Dev/Production config)
app.config.from_pyfile('config.py')


@app.route("/")
def index():
	return flask.render_template("index.html")

if __name__ == "__main__":
	app.run()

