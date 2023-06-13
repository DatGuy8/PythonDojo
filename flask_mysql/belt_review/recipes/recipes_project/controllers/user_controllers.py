from recipes_project import app
from flask import render_template, redirect, request, session, flash, url_for, flash
from recipes_project.models.user import User
from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)

@app.route('/')
def home():
    return render_template('homepage.html')


@app.route('/createuser', methods=['POST'])     #collects registration form here
def add_user():                                 #needs to do validation and password hashing
    if not User.validate_form(request.form):
        return redirect('/')
    pwhash = bcrypt.generate_password_hash(request.form['password'])      # creates hash password from the form
    data = {
        'first_name' : request.form['first_name'],
        'last_name' : request.form['last_name'],
        'email' : request.form['email'],
        'password' : pwhash                                         #add hash pasword into data
    }
    user = User.adduser(data)
    print('GOT USERS DATA:', user)
    return redirect('/')               #need to redirect to a sucessful creation page or maybe back to main page



@app.route('/login', methods=['POST'])      #collects login info
def login():                                #check email and password
    data = {
        'email': request.form['email']
        }
    registered_user = User.get_user_by_email(data)                           # Need to check if email is registered AND returns false if not in db
    if not registered_user:                                                   # if not registered in db
        flash('Invalid Email/Password', 'login') 
        return redirect('/')
    if not bcrypt.check_password_hash(registered_user.password, request.form['password']):   # Checks password correct
        flash('Invalid Email/Password', 'login')
        return redirect('/')
    session['userid'] = registered_user.id
    session['first_name'] = registered_user.first_name
    return redirect('/recipes')             # needs to return to sucessful login page also needs session storage of userid




@app.route('/logout')       #Clears session and send back to login page
def logout():
    session.clear()
    return redirect('/')