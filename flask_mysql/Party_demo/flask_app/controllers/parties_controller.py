from flask_app import app
from flask import render_template, redirect, request, session
from flask import flash
from flask_app.models.user_model import User
from flask_app.models.party_model import Party

@app.route('/parties/new')
def new_party_form():
    if 'user_id' not in session:
        return redirect('/')
    # logged_user = User.get_by_id({'id':session['user_id']})
    return render_template("new_parties.html")

@app.route('/parties/create',methods = ['POST'])
def process_party():
    if 'user_id' not in session:
        return redirect('/')
    if not Party.validator(request.form):
        return redirect('/parties/new')
    data = {
        **request.form,
        'user_id': session['user_id']
    }
    Party.create(data)
    return redirect('/welcome')