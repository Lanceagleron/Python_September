from flask_app import app
from flask import render_template, request, session, redirect
from flask_app.models.dog_model import Dog

@app.route('/')
def index():
    all_dogs = Dog.get_all()
    print(all_dogs)
    return render_template('index.html', all_dogs = all_dogs)

@app.route('/dogs/<int:id>')
def one_dog(id):
    one_dog = Dog.get_one({'id':id})
    return render_template('one_dog.html', one_dog=one_dog)

@app.route('/dogs/new')
def new_dog_form():
    return render_template('dogs_new.html')


@app.route('/dogs/create', methods=['POST'])
def create_dog():
    Dog.create(request.form)
    return redirect('/')

@app.route('/dogs/<int:id>/edit')
def edit_dog_form(id):

    data = {
        'id':id
    }
    this_dog = Dog.get_one(data)
    return render_template("dogs_edit.html", this_dog=this_dog)

@app.route('/dogs/<int:id>/update', methods=['POST'])
def update_dog(id):
    data = {
        **request.form, #quick wat to copy the contents of request.form into this disctionary
        'id':id
    }
    Dog.update(data)
    return redirect('/')

@app.route('/dogs/<int:id>/delete')
def delete_dog(id):
    data = {
        'id':id
    }
    Dog.delete(data)
    return redirect('/')