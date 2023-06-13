

import random
from flask import Flask, render_template, redirect, session, request, url_for


app = Flask(__name__)
app.secret_key = 'myprecious'

@app.route('/')
def home():
    if 'randomnum' in session:
        print(f'Random Number is: {session["randomnum"]}')
        return render_template('index.html')
    else :
        session['randomnum'] = random.randint(1,100)
        print(f'Random Number is: {session["randomnum"]}')
        return render_template('index.html')



@app.route('/yourguess', methods=['POST'])
def guesspage():
    guess = int(request.form['guess'])
    rando = int(session['randomnum'])
    if guess == rando:
        session.clear()
        session['randomnum'] = random.randint(1,100)
        print(session['randomnum'])
        return render_template('guess.html', num=guess, x=0)
    elif guess > rando:
        return render_template('guess.html', x=1)
    else:
        return render_template('guess.html', x=2)






if __name__ == "__main__":
    app.run(debug=True)
