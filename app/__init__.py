from flask import Flask
from flask_bootstrap import Bootstrap
from config import config_options
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_mail import Mail


# login Hellper classes
login_manager = LoginManager()
login_manager.session_protection = 'strong'
login_manager.login_view = 'auth.login'
# Upload files



# database
db = SQLAlchemy()
bootstrap = Bootstrap()
mail = Mail()

def create_app(config_name):

    app = Flask(__name__)
    mail.init_app(app)

    # app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    # Creating the app configurations
    app.config.from_object(config_options[config_name])

        # Initializing flask extensions
    bootstrap.init_app(app)
    db.init_app(app)
    login_manager.init_app(app)

    # Registering the blueprint
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    
    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint, url_prefix='/authenticate')



    # setting config

    return app
