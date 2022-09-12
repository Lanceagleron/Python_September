from flask_app import app
from flask import render_template, request, session, redirect
from flask_app.models.dojo_model import Dojo
from flask_app.models.ninja_model import Ninja

@app.route('/')
def index():
    return redirect ('/dojos')

@app.route('/dojos/create', methods=['POST'])
def create_dojo():
    Dojo.create(request.form)
    return redirect('/')

@app.route('/dojos')
def dojos():
    all_dojos = Dojo.get_all()
    return render_template('index.html',all_dojos=all_dojos)

@app.route('/dojos/<int:id>')
def one_dojo(id):
    one_dojo = Dojo.get_one_with_ninjas({'id':id})
    print(one_dojo)
    return render_template('one_dojo.html', one_dojo=one_dojo)



