from flask_app import app
from flask import render_template, request, session, redirect
from flask_app.models.dojo_model import Dojo
from flask_app.models.ninja_model import Ninja

@app.route('/ninjas/new')
def new_ninja_form():
    all_dojos = Dojo.get_all()
    return render_template('new_ninja.html', all_dojos=all_dojos)

@app.route('/ninja/create', methods=['POST'])
def create_new_ninja():
    Ninja.create(request.form)
    return redirect('/')