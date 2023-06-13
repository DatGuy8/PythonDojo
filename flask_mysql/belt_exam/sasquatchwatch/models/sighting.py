from sasquatchwatch.config.mysqlconnection import connectToMySQL
from sasquatchwatch.models.user import User
from flask import flash

class Sighting:
    def __init__(self, data):
        self.id = data['id']
        self.location = data['location']
        self.description= data['description']
        self.date_seen = data['date_seen']
        self.sasquatches = data['sasquatches']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.user_id = data['user_id']


#===========Get all sightings with user name to display on dashboard page
    @classmethod
    def sightings_with_user(cls):
        query = 'SELECT * FROM sightings LEFT JOIN users ON sightings.user_id = users.id;'

        results = connectToMySQL('sasquatch_schema').query_db(query)

        sightings = []
        for dict in results:
            sighting = cls(dict)
            user_data = {
                'id' : dict['users.id'],
                'first_name' : dict['first_name'],
                'last_name' : dict['last_name'],
                'email' : dict['email'],
                'password' : dict['password'],
                'created_at' : dict['users.created_at'],
                'updated_at' : dict['users.updated_at']
            }
            user = User(user_data)
            sighting.user = user
            sightings.append(sighting)
        return sightings
        # goes back to sightings controller to give info on sightings

# ===========Get one sighting=================
    @classmethod
    def get_one(cls, data):
        query = '''
            SELECT * FROM sightings WHERE id = %(id)s;
        '''
        results = connectToMySQL('sasquatch_schema').query_db(query, data)
        return cls(results[0])



#============Add sighting into db=================
    @classmethod
    def addsighting(cls,data):
        query = '''
            INSERT INTO sightings ( location, description, date_seen, sasquatches, created_at, updated_at, user_id)
            VALUES ( %(location)s, %(description)s, %(date_seen)s, %(sasquatches)s, NOW(), NOW(), %(user_id)s );
        '''
        return connectToMySQL('sasquatch_schema').query_db(query, data)



#========= Edit Post==================
    @classmethod
    def update_sight(cls,data):
        query = '''
            UPDATE sightings
            SET location = %(location)s,
            description = %(description)s,
            date_seen = %(date_seen)s,
            sasquatches = %(sasquatches)s,
            updated_at = NOW()             
            WHERE id = %(id)s;
        '''
        # stupid comma after now() cost me like an hour! 
        return connectToMySQL('sasquatch_schema').query_db(query, data)

# -===========DELETE SIGHT =====================
    @classmethod
    def delete_sight(cls,data):
        query = 'DELETE FROM sightings WHERE id = %(id)s;'
        return connectToMySQL('sasquatch_schema').query_db(query, data)


#=============check form data for adding inserting data===========
    @staticmethod
    def validate_sight(data):
        is_valid = True

# requiring fields to be populated
        if len(data['location']) < 1 or len(data['description']) < 1 or len(data['date_seen']) < 1:
            flash('All Fields Required!', 'report')
            is_valid = False
        
# requires sasquatches to be more than 1
        if len(data['sasquatches']) < 1 or int(data['sasquatches']) < 1:
            flash('You didnt see any??? WHAT YOU REPORTING!', 'report')
            is_valid = False

        return is_valid

