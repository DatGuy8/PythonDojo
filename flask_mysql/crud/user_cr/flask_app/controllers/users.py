from flask_app import app
from flask import render_template, redirect, request, session, flash
from flask_app.models.user import User

@app.route("/")
def home():

    return render_template("index.html")

@app.route('/create')
def create():

    return render_template('create.html')

@app.route('/createuser', methods=['POST'])
def adduser():
    
    User.adduser(request.form)

    return redirect('/users')

@app.route('/users')
def showusers():
    users = User.get_all()
    return render_template('read_all.html', users = users)

@app.route('/profile/<int:userid>')
def displayuser(userid):
    data = {
        'id': userid
    }
    
    user = User.getprofile(data)
    
    return render_template('profilepage.html', user = user)

@app.route('/delete/<int:userid>')
def deleteuser(userid):
    data = {
        'id': userid
    }
    User.deleteuser(data)
    return redirect('/users')

@app.route('/edit/<int:userid>')
def edituserpage(userid):
    data = {
        'id': userid
    }
    user = User.getprofile(data)

    return render_template('editpage.html', user = user)

@app.route('/edited/<int:userid>', methods=['POST'])
def edited(userid):
    data = {
        'id': userid,
        'first_name': request.form['first_name'],
        'last_name': request.form['last_name'],
        'email': request.form['email']

    }
    User.editprofile(data)
    return redirect('/users')