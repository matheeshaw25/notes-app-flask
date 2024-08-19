from flask import Blueprint,render_template # blueprint of application --> contains urls | render_template will render an html page

views = Blueprint('views', __name__) # name of blueprint

@views.route('/') #hit this route
def home(): # call this function
    return render_template("home.html")

