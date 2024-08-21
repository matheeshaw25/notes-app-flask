from flask import Flask
from flask_sqlalchemy import SQLAlchemy #import SQLAlchemy
from os import path
from flask_login import LoginManager # helps us manage all login related things


db = SQLAlchemy() # database object
DB_NAME = "database.db"

def create_app():
    app = Flask(__name__) #name of the file
    app.config['SECRET_KEY'] = 'hjkhjklop' #random letters
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}' #sql alchemy is stored in sqlite location
    db.init_app(app) # initialize database (this is the "app" we are going to use with the database)




    from .views import views # import views
    from .auth import auth # import auth

    # REGISTER THE BLUEPRINTS
    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')  

    # IMPORT MODELS
    from .models import User, Note

    create_database(app)

    login_manager = LoginManager() #create LoginManager object
    login_manager.login_view = 'auth.login' #flask redirect if not logged in --> to auth.login route
    login_manager.init_app(app) #tells loginmanager which app we are using

    @login_manager.user_loader
    def load_user(id):
        return User.query.get(int(id))

    return app

# def create_database(app):
#     if not path.exists('website/' + DB_NAME): #check if dabatase exists
#         db.create_all(app=app) # if it does exists create it
#         print('Created Database!')

def create_database(app):
    if not path.exists('website/' + DB_NAME):  # Check if the database file does not exist
        with app.app_context():  # Ensure the app context is available
            db.create_all()  # Create all tables
        print('Created Database!')                                                                                           