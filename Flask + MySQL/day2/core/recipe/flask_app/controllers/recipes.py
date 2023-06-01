from flask_app import app
from flask import render_template, request, redirect, session, flash
from flask_app.models.recipe import Recipe
from flask_app.models.user import User

from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)


@app.route('/recipes')
def dash():
    
    # route guard
    if 'user_id' not in session:
        return redirect('/')
    
    data = {
        "id" : session['user_id']
    }
    
    User.get_by_id(data)
    all_recipes = Recipe.get_all_with_users()
    print(all_recipes)
    return render_template('recipes.html', user = User.get_by_id(data),all_recipes=all_recipes)

@app.route('/recipes/new')
def recipe():
    
    return render_template('new_recipe.html')

@app.route('/recipes/create', methods=['POST'])
def new_recipe():
    if not Recipe.validate_recipe(request.form):
        return redirect('/recipes/new')
    print("=======",request.form)
    data = {
        **request.form,
        'user_id' : session['user_id']
    }
    Recipe.create_recipe(data)
    return redirect('/recipes')

@app.route("/recipes/<int:user_id>/edit")
def show_one_recipe(user_id):
    data = {
        "id" : user_id
    }
    one_recipe = Recipe.get_recipe_by_id(data)
    return render_template("edit_recipe.html",one_recipe=one_recipe )

@app.route('/recipes/<int:user_id>/update', methods=['POST'])
def update_recipe(user_id):
    if not Recipe.validate_recipe(request.form):
        return redirect('/recipes/'+str(user_id)+'/edit')
    data = {
        **request.form,
        "id" : user_id
    }
    Recipe.update(data)
    return redirect('/recipes')
    
@app.route("/recipes/<int:recipe_id>/destroy")
def delete_recipe(recipe_id):
    data = {
        "id" : recipe_id
    }
    Recipe.delete(data)
    return redirect("/recipes")

@app.route('/recipes/<int:recipe_id>')
def show_recipe(recipe_id):
    data = {
        "id" : recipe_id
    }
    one_user = User.get_by_id({'id':session['user_id']})
    one_recipe = Recipe.get_recipe_by_id(data)
    # name = session['user_name']
    
    
    return render_template("show_recipe.html",one_recipe=one_recipe,one_user=one_user)

