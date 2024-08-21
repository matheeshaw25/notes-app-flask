from flask import Blueprint, render_template, request, flash, redirect, url_for # blueprint of application #request information from the route
# flash sends out flask messages to front end

from .models import User
from werkzeug.security import generate_password_hash, check_password_hash
from . import db
from flask_login import login_user, login_required , logout_user , current_user

auth = Blueprint('auth', __name__)

# Contains all the auth related stuff
# LOGIN
@auth.route('/login', methods=['GET','POST'])
def login():
    # data = request.form #request data entered in the form
    # print(data) #print form data

    if request.method == 'POST':
        email = request.form.get('email') # capture email
        password = request.form.get('password') #capture password

        #check email
        user = User.query.filter_by(email=email).first() #User is model name , filter all users that have specific email
        if user: # if user exists
            if check_password_hash(user.password, password):#if both passwords are same
                flash('Logged in successfully',category='success')
                login_user(user, remember=True)# login user and remebers user is logged in until session expires
                return redirect(url_for('views.home'))
            else:
                flash('Incorrect Password, try again',category='error') # if password incorrect
        else:
            flash('Email does not exist', category='error')  # if user does not exist      


    return render_template("login.html",user=current_user)# user=current_user to display correct navbar when authenticated

#LOGOUT
@auth.route('/logout')
@login_required #cannot access this route without login
def logout():
    logout_user()
    return redirect(url_for('auth.login'))

#SIGN UP
@auth.route('/sign-up', methods=['GET','POST'])
def sign_up():
    if request.method == 'POST':

        #capture info from sign up form
        email = request.form.get('email')
        first_name = request.form.get('firstName')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')

        user = User.query.filter_by(email=email).first() # checks if the user email exists
        if user:
            flash('Email already exists', category='error')
        elif len(email) < 4 :
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
            login_user(user, remember=True)# login user and remebers user is logged in until session expires
            flash('Account Created !!', category='success') # category success because success message
            return redirect(url_for('views.home')) #blueprint-name.function-name
        
    return render_template("sign_up.html",user=current_user)# user=current_user to display correct navbar when authenticated


