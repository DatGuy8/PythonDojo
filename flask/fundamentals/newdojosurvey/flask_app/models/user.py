from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash

class User:
    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.location = data['location']
        self.language = data['language']
        self.comment = data['comment']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def get_all(cls):
        query = 'SELECT * FROM users;'
        results = connectToMySQL('dojo_survey_schema').query_db(query)
        users = []
        for user in results:
            users.append( cls(user) )
        return users


#=================INSERT FORM DATA=====================
    @classmethod
    def add_user(cls, data):
        query = 'INSERT INTO dojos (name, location, language, comment, created_at, updated_at) VALUES ( %(name)s, %(location)s, %(language)s, %(comment)s, NOW(), NOW() );'
        return connectToMySQL('dojo_survey_schema').query_db(query, data)

#=================Checks if input in form is enough================
    @staticmethod
    def validate_info(data):
        is_valid = True
        if len(data['name']) < 3:
            flash('First name must have more than 3 characters!')
            is_valid = False
        if len(data['location']) <= 1:
            flash('MUST CHOOSE LOCATION')
            is_valid = False
        if len(data['language']) <= 1:
            flash('MUST CHOSE LANGUAGE')
            is_valid = False
        if len(data['comment']) < 1:
            flash('MUST LEAVE A COMMENT!')
            is_valid = False
        return is_valid


