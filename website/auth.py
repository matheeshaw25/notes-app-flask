from flask import Blueprint, render_template, request, flash, redirect, url_for # blueprint of application #request information from the route
# flash sends out flask messages to front end

from .models import User
from werkzeug.security import generate_password_hash, check_password_hash
from . import db

auth = Blueprint('auth', __name__)

# Contains all the auth related stuff
# LOGIN
@auth.route('/login', methods=['GET','POST'])
def login():
    # data = request.form #request data entered in the form
    # print(data) #print form data
    return render_template("login.html",boolean = True)

#LOGOUT
@auth.route('/logout')
def logout():
    return "<p>Logout</p>"

#SIGN UP
@auth.route('/sign-up', methods=['GET','POST'])
def sign_up():
    if request.method == 'POST':

        #capture info from sign up form
        email = request.form.get('email')
        first_name = request.form.get('firstName')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')

        if len(email) < 4 :
            flash('Email must be greater than 4 characters', category='error') # category error because error message
        elif len(first_name) < 2 :
            flash('First name must be greater than 1 character', category='error')
        elif password1 != password2:
            flash('Passwords don\'t match', category='error')
        elif len(password1) < 7:
            flash('Password must be atleast 7 characters', category='error')
        else:
            # add user to database
            new_user = User(email=email, first_name=first_name , password=generate_password_hash(password1, method='pbkdf2:sha256')) #define all fields in models.py
            db.session.add(new_user)
            db.session.commit()
            flash('Account Created !!', category='success') # category success because success message
            return redirect(url_for('views.home')) #blueprint-name.function-name
        
    return render_template("sign_up.html")


