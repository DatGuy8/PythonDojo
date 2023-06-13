
from flask import Flask, redirect, url_for, render_template, request
app = Flask(__name__)   

a = 1


@app.route('/')
def home():
    return render_template('index.html')

@app.route('/whatsup/<name>')
def welcome(name):
    return render_template('index.html', name=name)

@app.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        print(request.form)
        user = request.form['nm']
        return redirect(url_for('user', usr=user))
    else:
        return render_template('login.html')

@app.route('/<usr>')
def user(usr):
    return f'<h1>{usr}</h1>'

@app.route('/admin')
def admin():
    if a >= 1:
        print('here')
        return redirect(url_for('welcome', name ='admin!'))
    else :
        return 'Welcome Bugger'






if __name__=="__main__":  
    app.run(debug=True)   
