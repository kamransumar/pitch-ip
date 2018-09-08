from flask import Flask
from .config import DevConfig
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy

# bootstrap = Bootstrap()
db = SQLAlchemy()
bootstrap = Bootstrap()
# Initializing application
app = Flask(__name__)

# Setting up configuration
app.config.from_object(DevConfig)
bootstrap.init_app(app)
db.init_app(app)

from . import views
