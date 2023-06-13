
from flask import Flask, render_template, redirect, session, request
app = Flask(__name__)
app.secret_key = 'boomshakalacka'


@app.route('/')
def home():
    if 'counter' in session:
        session['counter'] += 1
        session['pagevisits'] += 1
        return render_template('index.html')
    else:
        session['counter'] = 1
        session['pagevisits'] = 1
        return render_template('index.html')


@app.route('/plus2', methods=["POST"])
def add2():
    session['counter'] += 1
    return redirect('/')


@app.route('/destroy_session')
def destroy():
    session.clear()
    return redirect('/')

@app.route('/howmany', methods=['POST'])
def howmanyby():
    session['counter'] += int(request.form['num'])-1
    return redirect('/')

if __name__ == "__main__":
    app.run(debug=True)
