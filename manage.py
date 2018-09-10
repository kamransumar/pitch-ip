from app import app, db
from flask_migrate import Migrate, MigrateCommand
from app.models import User, Comment, Pitch, Category
from flask_script import Manager, Server

manager = Manager(app)
migrate = Migrate(app, db)


@manager.shell
def make_shell_context():
    return dict(app=app, db=db, User=User, Comment=Comment, Pitch=Pitch, Category=Category)


if __name__ == '__main__':
    manager.run()
