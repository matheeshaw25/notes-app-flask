from flask import Blueprint, render_template, request, flash # blueprint of application #request information from the route
# flash sends out flask messages to front end
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
        firstName = request.form.get('firstName')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')

        if len(email) < 4 :
            flash('Email must be greater than 4 characters', category='error') # category error because error message
        elif len(firstName) < 2 :
            flash('First name must be greater than 1 character', category='error')
        elif password1 != password2:
            flash('Passwords don\'t match', category='error')
        elif len(password1) < 7:
            flash('Password must be atleast 7 characters', category='error')
        else:
            # add user to database
            flash('Account Created !!', category='success') # category success because success message
            
    return render_template("sign_up.html")


