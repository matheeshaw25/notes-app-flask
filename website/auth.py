from flask import Blueprint, render_template# blueprint of application

auth = Blueprint('auth', __name__)

# Contains all the auth related stuff
# LOGIN
@auth.route('/login')
def login():
    return render_template("login.html",boolean = True)

#LOGOUT
@auth.route('/logout')
def logout():
    return "<p>Logout</p>"

#SIGN UP
@auth.route('/sign-up')
def sign_up():
    return render_template("sign_up.html")


