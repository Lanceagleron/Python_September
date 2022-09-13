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
    id = Party.create(data)
    return redirect(f'/parties/{id}')

@app.route("/parties/<int:id>")
def show_party(id):
    one_party = Party.get_by_id({'id':id})
    return render_template("one_party.html", one_party=one_party)

@app.route("/parties/<int:id>/edit")
def edit_party_form(id):
    if 'user_id' not in session:
        return redirect('/')
    party = Party.get_by_id({'id':id})
    if not int(session['user_id']) == party.user_id:
        flash("Whoa there, that's not yours, Hands off!")
        return redirect ('/welcome')
    one_party = Party.get_by_id({'id':id})
    return render_template("edit_party.html", one_party=one_party)

@app.route('/parties/<int:id>/update', methods=['POST'])
def update_party(id):
    if 'user_id' not in session:
        return redirect('/')
    party = Party.get_by_id({'id':id})
    if not int(session['user_id']) == party.user_id:
        flash("Whoa there, that's not yours, Hands off!")
        return redirect ('/welcome')
    if not Party.validator(request.form):
        return redirect(f"/parties/{id}/edit")
    data = {
        **request.form,
        'id':id
    }
    Party.update(data)
    return redirect('/welcome')

@app.route('/parties/<int:id>/delete')
def delete_party(id):
    #will not allow users to delete when not logged in
    if 'user_id' not in session:
        return redirect('/')
    #prevents other users deleting your own stuff
    party = Party.get_by_id({'id':id})
    if not int(session['user_id']) == party.user_id:
        flash("Whoa there, that's not yours, Hands off!")
        return redirect ('/welcome')
    Party.delete({'id': id})
    return redirect('/welcome')

@app.route("/my_parties")
def my_parties():
    if 'user_id' not in session:
        return redirect('/')
    one_user = User.get_by_id({'id':session['user_id']})
    return render_template("my_parties.html", logged_user=one_user)