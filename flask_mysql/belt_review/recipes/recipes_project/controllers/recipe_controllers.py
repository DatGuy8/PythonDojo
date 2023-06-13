from recipes_project import app
from flask import render_template, redirect, request, session, flash, url_for, flash
from recipes_project.models.user import User
from recipes_project.models.recipe import Recipe


#======================Dashboard After login need to get recipe data =====================================================
@app.route('/recipes')
def loggedin():                 #successful login page where people already logged in can access
    if 'userid' not in session:
        flash('PLEASE LOG IN!', 'login')        # checks to see if userid is in session if not send back to login page with flash
        return redirect('/')

    recipes = Recipe.get_all_with_users()
    print(recipes)
    return render_template('dashboard.html', recipes = recipes)     #render loggedin page if in session or logined in first time




# =================from dashboard====> send to form for recipe ALSO SHOW ALL RECIPES=============
@app.route('/recipes/new')
def recipeform():
    
# get all data from recipes, need to have a join function and return the data========================



    return render_template('recipeform.html')


# ============================Grabs form data from recipeform.html=========================
@app.route('/createrecipe', methods=['POST'])
def addrecipe():


    data = {
        'name': request.form['name'],
        'description': request.form['description'],
        'instruction': request.form['instruction'],
        'date_made': request.form['date_made'],
        'under_30': request.form['under_30'],
        'user_id': session['userid']
    }

    Recipe.add_recipe(data)

    return redirect('/recipes')

# ==================================Gets recipe id from dashboard.html view recipe tag================
@app.route('/recipe/<int:recipeid>')
def showrecipe(recipeid):
    data = {
        'id': recipeid
    }
    recipe = Recipe.get_one(data)
    
    return render_template('/showrecipe.html', recipe=recipe)    #add in recipe= recipe