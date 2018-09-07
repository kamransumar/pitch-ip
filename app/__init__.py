from flask import Flask
from .config import DevConfig
from flask_bootstrap import Bootstrap

# bootstrap = Bootstrap()

# Initializing application
app = Flask(__name__)

# Setting up configuration
app.config.from_object(DevConfig)

bootstrap = Bootstrap(app)

from . import views
