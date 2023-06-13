from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import app
from flask import render_template, session, redirect, request
from flask_app.models.user import User


@app.route('/')
def home():
    return render_template('index.html')    #page with form


@app.route('/process', methods=['POST'])      #info from form comes here
def getinfo():                                  #gonna want to insert into database here
    
    if not User.validate_info(request.form):         #Checks inputs
        return redirect('/')
    print('GOT THE INFO')
    print(request.form)
    if 'userdata' in session:
        session.clear()
        session['userdata'] = request.form
    else:
        session['userdata'] = request.form
    data = {
        'name': request.form['name'],
        'location': request.form['location'],
        'language': request.form['language'],
        'comment': request.form['comment'],
    }
    User.add_user(data)
    return redirect('/results')

@app.route('/results')
def showinfo():
    print(session['userdata'])
    return render_template('results.html')


