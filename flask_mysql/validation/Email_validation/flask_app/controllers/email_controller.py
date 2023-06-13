from flask_app import app
from flask_app.models.email import Email
from flask import render_template, redirect, request, session, flash, url_for, flash



@app.route('/')
def home():
    return render_template('home.html')


# =================================== COLLECT EMAIL ====================================
@app.route('/addemail', methods=['POST'])
def addemail():
    if not Email.validate_email(request.form):
        return redirect('/')
    
    data = {
        'email': request.form['email']
    }

    Email.add_email(data)


    return redirect('/showemails')


# ==================================== SHOW ALL EMAILS =================================
@app.route('/showemails')
def allemails():

    emails = Email.get_all()

    return render_template('showemail.html', emails = emails)