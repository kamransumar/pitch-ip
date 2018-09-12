from flask import Flask
from config import config_options
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask import Blueprint
from flask_uploads import UploadSet, configure_uploads, IMAGES

main = Blueprint('main', __name__)

login_manager = LoginManager()
login_manager.session_protection = 'strong'
login_manager.login_view = 'auth.login'

# bootstrap = Bootstrap()
db = SQLAlchemy()
bootstrap = Bootstrap()
# Initializing application
photos = UploadSet('photos', IMAGES)


def create_app(config_name):
    app = Flask(__name__)
    # ...
    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint, url_prefix='/authenticate')

    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    # Setting up configuration
    app.config.from_object(config_options[config_name])
    bootstrap.init_app(app)
    db.init_app(app)
    login_manager.init_app(app)
    # configure UploadSet
    configure_uploads(app, photos)

    return app
