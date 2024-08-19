from flask import Flask

def create_app():
    app = Flask(__name__) #name of the file
    app.config['SECRET_KEY'] = 'hjkhjklop' #random letters

    from .views import views # import views
    from .auth import auth # import auth

    # REGISTER THE BLUEPRINTS
    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')  

    return app

