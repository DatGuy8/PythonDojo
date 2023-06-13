from recipes_project.config.mysqlconnection import connectToMySQL
from flask import flash
from recipes_project.models.user import User

class Recipe:
    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.description= data['description']
        self.instruction = data['instruction']
        self.date_made = data['date_made']
        self.under_30 = data['under_30']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.user_id = data['user_id']
        self.users = []

#=====================GETS all Recipes in db and returns it to controller==================
    @classmethod
    def get_all_with_users(cls):
        query = 'SELECT * FROM recipes LEFT JOIN users ON recipes.user_id = users.id;'
        results = connectToMySQL('recipes_db').query_db(query)

        recipes = []
        for dict in results:
            recipe = cls(dict)
            user_data = {
                'id': dict['users.id'],
                'first_name' : dict['first_name'],
                'last_name' : dict['last_name'],
                'email' : dict['email'],
                'password' : dict['password'],
                'created_at' : dict['users.created_at'],
                'updated_at' : dict['users.updated_at']
            }

            user = User(user_data)
            recipe.user = user
            recipes.append(recipe)
        return recipes
        #=======================THIS RETURNS THE RECIPE WITH USER DATA==============================================


# ==============insert recipe into database=========================
    @classmethod
    def add_recipe(cls, data):
        query = 'INSERT INTO recipes(name, description, instruction, date_made, under_30, created_at, updated_at, user_id) VALUES( %(name)s, %(description)s , %(instruction)s , %(date_made)s , %(under_30)s , NOW(), NOW(), %(user_id)s );'
        return connectToMySQL('recipes_db').query_db(query,data)

#=================get info from one recipe========================
    @classmethod
    def get_one(cls, data):
        query = 'SELECT * FROM recipes LEFT JOIN users ON recipes.user_id = users.id WHERE recipes.id = %(id)s;'
        results = connectToMySQL('recipes_db').query_db(query, data)
        recipe = cls(results[0]) #gives the one row and makes of instance of recipe
        # print(results)
        # print(recipe)
        # print('==================')
        user_data = {
                'id': results[0]['users.id'],
                'first_name' : results[0]['first_name'],
                'last_name' : results[0]['last_name'],
                'email' : results[0]['email'],
                'password' : results[0]['password'],
                'created_at' : results[0]['users.created_at'],
                'updated_at' : results[0]['users.updated_at']
            }
        user = User(user_data)   #add the user part of the row and makes a user instance
        recipe.user = user      #adds the two instances together into one row
        return recipe