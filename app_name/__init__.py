from flask import Flask
import models, views



app = Flask(__name__, instance_relative_config=True)


# Load Dev or Production config
app.config.from_object("config.Dev")
# Production and sensitive data (overwrites Dev/Production config)
app.config.from_pyfile('config.py')


