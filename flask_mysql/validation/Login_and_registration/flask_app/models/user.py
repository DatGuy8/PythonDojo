from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
import re

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
PASS_REGEX = re.compile(r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)[a-zA-Z\d]{8,}$')

class User:
    def __init__(self, data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.password = data['password']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def adduser(cls, data):  # after doing checks adds user into db
        query = 'INSERT INTO users (first_name, last_name, email, password, created_at, updated_at) VALUES ( %(first_name)s, %(last_name)s, %(email)s, %(password)s, NOW(), NOW() );'
        # returns userid number
        return connectToMySQL('user_login').query_db(query, data)


# ====================== Checking if user signed up to log in OR Get user id=============================
    @classmethod
    def get_user_by_email(cls, data):
        query = 'SELECT * FROM users WHERE email = %(email)s ;'
        result = connectToMySQL('user_login').query_db(query, data)

        if len(result) < 1:
            return False
        return cls(result[0])

# ====================where to do checks and flash messages============================
    @staticmethod
    def validate_form(data):
        is_valid = True
        query = "SELECT * FROM users WHERE email = %(email)s;"
        results = connectToMySQL('user_login').query_db(query, data)
        if len(results) >= 1:
            flash('Email Already Taken!', 'registration')
            is_valid = False
        if not EMAIL_REGEX.match(data['email']):
            flash("Invalid email address!", 'registration')
            is_valid = False
        if not data['first_name'].isalpha() or not data['last_name'].isalpha():
            flash('NO NUMBERS IN NAME!', 'registration')
            is_valid = False
        if len(data['first_name']) <= 2:
            flash('NEED A LONGER NAME BRO!', 'registration')
            is_valid = False
        if len(data['last_name']) < 2:
            flash("LAST NAME NEED TO BE LONG THAN THAT!", 'registration')
            is_valid = False
        if len(data['password']) == 0:
            flash('SUMMIT A PASSWORD!', 'registration')
            is_valid = False
        if not PASS_REGEX.match(data['password']):
            flash('MUST CONTAIN ONE UPPERCASE LETTER AND A NUMBER IN PASSWORD also no special characters', 'registration')
            is_valid = False
        if len(data['password']) < 8 or len(data['password']) > 20:
            flash('PASSWORD NEEDS TO BE BETWEEN 8-20 CHARACTERS!', 'registration')
            is_valid = False
        if data['password'] != data['conpassword']:
            flash('PASSWORDS DO NOT MATCH!', 'registration')
            is_valid = False

        return is_valid
