from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager, Server
from flask_wtf.csrf import CsrfProtect

from app import create_app, db
from app.models import User

app = create_app('production')
app.secret_key = 'very secret'
CsrfProtect(app)

# csrf = CSRFProtect(app)


manager = Manager(app)
manager.add_command('server', Server)


migrate = Migrate(app, db)
manager.add_command('db', MigrateCommand)


@manager.shell
def add_shell_context():
    return {'db': db, 'User': User}


if __name__ == '__main__':
    manager.run()