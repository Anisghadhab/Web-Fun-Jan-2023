from flask_app import app
from flask import render_template, request, redirect, session, flash
from flask_app.models import user
from flask_app.models import recipe

from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)


# LOGIN PAGE
@app.route('/')
def show_form():
    
    return render_template('register_login.html')

# REGISTER method
@app.route("/users/create", methods=['POST'])
def user_create():
    
    if not user.User.validate(request.form):
        return redirect ('/')
    # HASH THE PASSWORD
    pw_hash = bcrypt.generate_password_hash(request.form['password'])
    data = {
        **request.form,
        'password' : pw_hash
    }
    # Create a user
    user_id = user.User.create(data)
    # Store user id in session
    session["user_id"] = user_id
    return redirect("/recipes")
    # LOGIN

@app.route("/users/login", methods = ["POST"])
def login():
    
    data = {
        "email" : request.form["email"]
    }
    user_in_db = user.User.get_by_email(data)
    # if email not found
    if not user_in_db:
        flash("invalid credentials ", "log")
        return redirect ('/')

    # check password
    if not bcrypt.check_password_hash(user_in_db.password, request.form["password"]):
        flash("invalide credentials","log")
        return redirect('/')
    
    # ALL GOOD up to here
    session['user_id'] = user_in_db.id
    session['user_name'] = user_in_db.first_name
    return redirect('/recipes')



    # logout 
@app.route('/logout')
def logout():
        
    session.clear()
    return redirect('/')