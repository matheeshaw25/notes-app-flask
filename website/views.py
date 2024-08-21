from flask import Blueprint,render_template # blueprint of application --> contains urls | render_template will render an html page
from flask_login import  login_required , current_user

views = Blueprint('views', __name__) # name of blueprint

@views.route('/') #hit this route
@login_required
def home(): # call this function
    return render_template("home.html", user=current_user) #user=current_user references the current user

