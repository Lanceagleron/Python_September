from flask_app import app
from flask import render_template, redirect, request, session
from flask import flash
from flask_app.models.user_model import User
from flask_app.models.recipe_model import Recipe


@app.route('/recipe/new')
def new_recipe_form():
    if 'user_id' not in session:
        return redirect('/')
    return render_template('new_recipe.html')

@app.route('/recipe/create', methods = ['POST'])
def process_recipe():
    if 'user_id' not in session:
        return redirect('/')
    if not Recipe.validator(request.form):
        return redirect('/recipes/new')
    data = {
        **request.form,
        'user_id': session['user_id']
    }
    Recipe.create(data)
    return redirect('/welcome')

@app.route('/recipe/<int:id>')
def view_recipe(id):
    user_data = {
        'id': session['user_id']
    }
    logged_user = User.get_by_id(user_data)
    one_recipe = Recipe.get_id({'id':id})
    return render_template("one_recipe.html", one_recipe=one_recipe, logged_user=logged_user)

@app.route('/recipe/<int:id>/edit')
def edit_recipe_form(id):
    if 'user_id' not in session:
        return redirect('/')
    recipe = Recipe.get_id({'id':id})
    if not int(session['user_id']) == recipe.user_id:
        flash("Whoa there, that's not yours, Hands off!")
        return redirect ('/welcome')
    one_recipe = Recipe.get_id({'id':id})
    return render_template("edit_recipe.html", one_recipe=one_recipe)

@app.route('/recipe/<int:id>/update', methods=['POST'])
def update_recipe(id):
    if 'user_id' not in session:
        return redirect('/')
    recipe = Recipe.get_id({'id':id})
    if not int(session['user_id']) == recipe.user_id:
        flash("Whoa there, that's not yours, Hands off!")
        return redirect ('/welcome')
    if not Recipe.validator(request.form):
        return redirect(f"/recipe/{id}/edit")
    data = {
        **request.form,
        'id':id
    }
    Recipe.update(data)
    return redirect('/welcome')

@app.route('/recipe/<int:id>/delete')
def delete_recipe(id):
    #will not allow users to delete when not logged in
    if 'user_id' not in session:
        return redirect('/')
    #prevents other users deleting your own stuff
    recipe = Recipe.get_id({'id':id})
    if not int(session['user_id']) == recipe.user_id:
        flash("Whoa there, that's not yours, Hands off!")
        return redirect ('/welcome')
    Recipe.delete({'id': id})
    return redirect('/welcome')