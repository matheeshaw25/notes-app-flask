from . import db # . = wbesite(package)
from flask_login import UserMixin
from sqlalchemy.sql import func

class Note(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    data = db.Column(db.String(10000))
    date = db.Column(db.DateTime(timezone=True), default=func.now()) #func returns the current date and time based on the database server's clock
    user_id = db.Column(db.Integer, db.ForeignKey('user.id')) #user_classname.id - lowercase in foreignkey


class User(db.Model, UserMixin):
    id = db.Column(db.Integer , primary_key=True)
    email = db.Column(db.String(150), unique=True) #unique=True - cant use the same email more than once
    password = db.Column(db.String(150))
    first_name = db.Column(db.String(150))
    notes = db.relationship('Note') # everytime a note is created, add into user relationship ID


    