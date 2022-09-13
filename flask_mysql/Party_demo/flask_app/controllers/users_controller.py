import imp
from flask_app import app
from flask import render_template, redirect, request, session
from flask import flash
from flask_bcrypt import Bcrypt
from flask_app.models.user_model import User

bcrypt = Bcrypt(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/user/register', methods=['POST'])
def register():
    if not User.validate(request.form):
        return redirect('/')
    hashed_pass = bcrypt.generate_password_hash(request.form['password'])
    data = {
        **request.form,
        'password':hashed_pass
    }
    id = User.create(data)
    session['user_id'] = id
    return redirect('/welcome')

@app.route('/user/login', methods=['POST'])
def login():
    #see if the username/email provided exist in the database
    data = {'email' : request.form['email']}
    user_in_db = User.get_by_email(data)
    #if user is not registered
    if not user_in_db:
        flash('Invalid login info', 'log')
        return redirect('/')
    #if the user exists, check password!
    if not bcrypt.check_password_hash(user_in_db.password, request.form['password']):
        flash('Invalid login info', 'log')
        return redirect('/')
    #log them in
    session['user_id'] = user_in_db.id
    return redirect('/welcome')

@app.route('/user/logout')
def logout():
    del session['user_id']
    return redirect('/')

@app.route('/welcome')
def welcome():
    if 'user_id' not in session:
        return redirect('/')
    return "logged in, Good Stuff"