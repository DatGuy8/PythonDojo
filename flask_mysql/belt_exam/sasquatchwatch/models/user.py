from sasquatchwatch.config.mysqlconnection import connectToMySQL
from flask import flash
import re

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
# PASS_REGEX = re.compile(r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)[a-zA-Z\d]{8,}$')
# ^^if I want extra password things here^^^


class User:
    def __init__(self, data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.password = data['password']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']


#================== after doing checks adds user into db=====================
    @classmethod
    def adduser(cls, data):
        query = 'INSERT INTO users (first_name, last_name, email, password, created_at, updated_at) VALUES ( %(first_name)s, %(last_name)s, %(email)s, %(password)s, NOW(), NOW() );'
        # returns userid number
        return connectToMySQL('sasquatch_schema').query_db(query, data)



# ====================== Checking if user signed up to log in OR Get user id=============================
    @classmethod
    def get_user_by_email(cls, data):
        query = 'SELECT * FROM users WHERE email = %(email)s ;'
        result = connectToMySQL('sasquatch_schema').query_db(query, data)

        if len(result) < 1:
            return False
        return cls(result[0])


#==================       get name from sighting here
    @classmethod
    def get_one_name(cls,data):
        query = 'SELECT * FROM users WHERE id = %(id)s;'
        results = connectToMySQL('sasquatch_schema').query_db(query,data)
        return cls(results[0])



# =======VALIDATION REGISTRATION======where to do checks and flash messages============================
    @staticmethod
    def validate_form(data):
        is_valid = True
        query = "SELECT * FROM users WHERE email = %(email)s;"
        results = connectToMySQL('sasquatch_schema').query_db(query, data)

# check email already in
        if len(results) >= 1:
            flash('Email Already Taken!', 'registration')
            is_valid = False

# checks email is valid
        if not EMAIL_REGEX.match(data['email']):
            flash("Invalid email address!", 'registration')
            is_valid = False

#checks first and last name for numbers
        if not data['first_name'].isalpha() or not data['last_name'].isalpha():
            flash('NO NUMBERS IN NAME!', 'registration')
            is_valid = False

# checks min 2 letters in first name
        if len(data['first_name']) < 2:
            flash('NEED A LONGER NAME BRO!', 'registration')
            is_valid = False

# checks min 2 letters in last name
        if len(data['last_name']) < 2:
            flash("LAST NAME NEED TO BE LONG THAN THAT!", 'registration')
            is_valid = False

#checks password is summited
        if len(data['password']) == 0:
            flash('SUMMIT A PASSWORD!', 'registration')
            is_valid = False

#must be longer than 8 characters
        if len(data['password']) < 8:
            flash('PASSWORD NEEDS TO BE AT LEAST 8 CHARACTERS', 'registration')
            is_valid = False

# checks if passords match
        if data['password'] != data['conpassword']:
            flash('PASSWORDS DO NOT MATCH!', 'registration')
            is_valid = False

        # if not PASS_REGEX.match(data['password']):
        #     flash('MUST CONTAIN ONE UPPERCASE LETTER AND A NUMBER IN PASSWORD also no special characters', 'registration')
            # is_valid = False

        return is_valid


