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
