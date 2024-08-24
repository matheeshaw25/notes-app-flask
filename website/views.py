from flask import Blueprint,render_template, request, flash , jsonify # blueprint of application --> contains urls | render_template will render an html page
from flask_login import  login_required , current_user
from .models import Note
from . import db
import json

views = Blueprint('views', __name__) # name of blueprint

@views.route('/',methods=['GET','POST']) #hit this route
@login_required
def home(): # call this function
    if request.method == 'POST':
        note = request.form.get('note')

        if len(note) < 1:
            flash('Note is too short!',category='error')
        else:
            new_note = Note(data=note , user_id = current_user.id)
            db.session.add(new_note)
            db.session.commit()
            flash('Note added!', category='success')

    return render_template("home.html", user=current_user) #user=current_user references the current user

@views.route('/delete-note',methods=['POST'])
def delete_note():
    note = json.loads(request.data)
    noteId = note['noteId']
    note = Note.query.get(noteId) #look for the node that has that id
    if note: # check if there is that note
        if note.user_id == current_user.id: #check user id
            db.session.delete(note)
            db.session.commit()
    
    return jsonify({})

