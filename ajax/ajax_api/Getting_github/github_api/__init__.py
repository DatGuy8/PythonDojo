from flask import Flask
app = Flask(__name__)
from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)

app.secret_key = 'iwehjnvu23uh4dkvjashru3h4889fsvhi34y8348927vjkndjh'
