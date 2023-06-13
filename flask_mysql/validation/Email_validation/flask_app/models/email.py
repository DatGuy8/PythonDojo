from flask_app.config.mysqlconnection import connectToMySQL

from flask import flash
import re

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$') 

class Email:
    def __init__(self, data):
        self.id = data['id']
        self.email = data['email']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']



# ========================== Get All Emails===================================
    @classmethod
    def get_all(cls):
        query = 'SELECT * FROM emails;'
        results = connectToMySQL('email_schema').query_db(query)
        emails = []
        for email in results:
            emails.append(cls(email))
        
        return emails


# ============================== ADD EMAIL ==================================
    @classmethod
    def add_email(cls, data):
        query = 'INSERT INTO emails ( email, created_at, updated_at ) VALUES ( %(email)s, NOW(), NOW() );'
        return connectToMySQL('email_schema').query_db(query, data)

# =========================== Valdiation of Email ===========================
    @staticmethod
    def validate_email(data):
        is_valid = True
        query = 'SELECT * FROM emails WHERE email = %(email)s;'
        results = connectToMySQL('email_schema').query_db(query, data)

        if not EMAIL_REGEX.match(data['email']):
            flash('invalid email address!')
            is_valid = False
        if len(results) >= 1:
            flash('Email already in DATABASE')
            is_valid = False


        return is_valid