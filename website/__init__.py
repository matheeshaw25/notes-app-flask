from flask import Flask

def create_app():
    app = Flask(__name__) #name of the file
    app.config['SECRET_KEY'] = 'hjkhjklop' #random letters

    return app

