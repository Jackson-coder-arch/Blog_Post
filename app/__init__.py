# from flask import Flask
# from flask_bootstrap import Bootstrap
# from config import config_options
# from flask_sqlalchemy import SQLAlchemy
# from flask_login import LoginManager
# from flask_uploads import UploadSet,configure_uploads,IMAGES
# from flask_mail import Mail


# login_manager = LoginManager()
# login_manager.session_protection = 'strong'
# login_manager.login_view = 'auth.login'

# bootstrap = Bootstrap()
# db = SQLAlchemy()

# photos = UploadSet('photos',IMAGES)
# mail = Mail()

# def create_app(config_name):

#     app = Flask(__name__)


#     # Creating the app configurations

#     app.config.from_object(config_options[config_name])
#     # config_options[config_name].init_app(app)

#     # Initializing flask extensions
#     bootstrap.init_app(app)
#     db.init_app(app)
#     login_manager.init_app(app)

#     mail.init_app(app)

#     # configure UploadSet
#     configure_uploads(app,photos)

#     # Registering the blueprint
#     from .main import main as main_blueprint
#     app.register_blueprint(main_blueprint)
#     from .auth import auth as auth_blueprint
#     app.register_blueprint(auth_blueprint,url_prefix = '/authenticate')

#     # setting config
#     from app.requests import configure_request
#     configure_request(app)
    
#     return app









from flask import Flask
from flask_bootstrap import Bootstrap
from flask_login import LoginManager
from flask_mail import Mail
from flask_sqlalchemy import SQLAlchemy

from config import Config

app = Flask(__name__)
db = SQLAlchemy(app)
login_manager = LoginManager()
login_manager.init_app(app)
bootstrap = Bootstrap(app)
mail = Mail(app)
login_manager.login_view = 'auth.login'
login_manager.session_protection = 'strong'
login_manager.login_message_category = 'info'


def create_app():
    app.config.from_object(Config)
    from .auth import auth as auth_blueprint
    from .main import main as main_blueprint
    app.register_blueprint(auth_blueprint)
    app.register_blueprint(main_blueprint)
    return app
