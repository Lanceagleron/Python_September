from flask_app import app
from flask import render_template, request, session, redirect
from flask_app.models.user_model import User

@app.route('/')
def index():
    return redirect ('/users')

@app.route('/users')
def users():
    all_users = User.get_all()
    return render_template('index.html', all_users=all_users)

@app.route('/users/new')
def new_user_form():
    return render_template('create.html')

@app.route('/users/create', methods=['POST'])
def create_user():
    User.create(request.form)
    return redirect('/')

@app.route('/users/<int:id>')
def show_user(id):
    one_user = User.get_one({'id':id})
    return render_template('show_user.html', one_user = one_user)

@app.route('/users/<int:id>/edit')
def edit_user_form(id):
    data = {
        'id':id
    }
    this_user = User.get_one(data)
    return render_template('edit.html', this_user=this_user)

@app.route('/users/<int:id>/update', methods=['POST'])
def update_user(id):

    data = {
        **request.form, #quick wat to copy the contents of request.form into this disctionary
        'id':id
    }
    User.update(data)
    return redirect('/')

@app.route('/users/<int:id>/delete')
def delete_user(id):
    data = {
        'id':id
    }
    User.delete(data)
    return redirect('/')