from flask import Flask
from app.config import DevConfig
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

login_manager = LoginManager()
login_manager.session_protection = 'strong'
login_manager.login_view = 'auth.login'

# bootstrap = Bootstrap()
db = SQLAlchemy()
bootstrap = Bootstrap()
# Initializing application
app = Flask(__name__)

# Setting up configuration
app.config.from_object(DevConfig)
bootstrap.init_app(app)
db.init_app(app)
login_manager.init_app(app)


def create_app(config_name):
    # ...
    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint, url_prefix='/authenticate')


from . import views
