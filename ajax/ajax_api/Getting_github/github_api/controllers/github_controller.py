from github_api import app
from flask import render_template, redirect, request, session, flash, flash

@app.route('/')
def home():
    return render_template('home.html')