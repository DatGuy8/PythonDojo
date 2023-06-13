from flask import Flask
app = Flask(__name__)
from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)

app.secret_key = 'k9324ju90vu023un8vuua9349u49djhvuh3'
