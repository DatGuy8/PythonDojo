from sasquatchwatch import app
from flask import render_template, redirect, request, session, flash, url_for, flash
from sasquatchwatch.models.user import User
from sasquatchwatch.models.sighting import Sighting



# ==========successful login page with all sightings=========
@app.route('/dashboard')
def loggedin():

    if 'userid' not in session:
        flash('Please LOG IN!', 'login')
        return redirect('/')         # sends user back to login page if not in session

    sightings = Sighting.sightings_with_user()

    return render_template('dashboard.html', sightings = sightings)


#===========Create sight page=====================================================================
@app.route('/createsight')
def reportpage():

    if 'userid' not in session:
        flash('Please LOG IN!', 'login')
        return redirect('/')         # sends user back to login page if not in session


    return render_template('reportpage.html')



# =========Collects info from reportpage============================================================
@app.route('/addsight', methods=['POST'])
def add_in_sight():

#             need to validate form data
    if not Sighting.validate_sight(request.form):
        return redirect('/createsight')

#             info is good now add into db
    data = {
        **request.form,
        'user_id' : session['userid']
    }
    Sighting.addsighting(data)

    return redirect('/dashboard')


# ============ render EditPage ============================================================
@app.route('/editpage/<int:sightid>')
def editpage(sightid):

    if 'userid' not in session:
        flash('Please LOG IN!', 'login')
        return redirect('/')         # sends user back to login page if not in session

#        Now need to get specific sighting
    data = {
        'id': sightid
    }
    sighting = Sighting.get_one(data)
    print(sighting.user_id)

#       checks to see if right user is signed in to edit that sighting if not return to dash     
    if session['userid'] != sighting.user_id:
        return redirect('/dashboard')

    return render_template('editpage.html', sighting = sighting)


# ==============Collects edit form===============================
@app.route('/editsight/<int:sightid>', methods=['POST'])
def edit_sight(sightid):
    # validate information
    if not Sighting.validate_sight(request.form):
        return redirect('/editpage/'+str(sightid))

    data = {
        **request.form,
        'id': sightid
    }
    Sighting.update_sight(data)

    return redirect('/dashboard')



# =============view sight page==============
@app.route('/viewsight/<int:sightid>')
def displaysighting(sightid):

    if 'userid' not in session:
        flash('Please LOG IN!', 'login')
        return redirect('/')         # sends user back to login page if not in session
    
    data = {
        'id' : sightid
    }

    # gets sighting data
    sighting = Sighting.get_one(data)

    user_data = {
        'id': sighting.user_id
    }

    user = User.get_one_name(user_data)    
    return render_template('viewsight.html', sighting= sighting, user= user)


# =========delete sighting=============
@app.route('/delete/<int:sightid>')
def deletesight(sightid):

    if 'userid' not in session:
        flash('Please LOG IN!', 'login')
        return redirect('/')         # sends user back to login page if not in session

    data = {
        'id': sightid
    }

    Sighting.delete_sight(data)
    return redirect('/dashboard')