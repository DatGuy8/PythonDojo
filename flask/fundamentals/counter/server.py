
from flask import Flask, render_template, redirect, session


app = Flask(__name__)
app.secret_key = 'myprecious1'


@app.route('/', methods=['POST', 'GET'])
def hello():
    if 'visits' in session:
        session['visits'] += 1
    else:
        session['visits'] = 1
    print("VISIT INFO")
    print(session['visits'])
    return render_template('index.html', num=session['visits'])

@app.route('/upby2', methods=['POST'])
def raiseby2():
    session['visits'] += 1
    return redirect('/')

@app.route('/destroy_session')
def reset():
    if 'visits' in session:
        print('session exists')
        session.pop('visits')
    else:
        print('nope')
    return redirect('/')

@app.route('/howmany', methods=['POST', 'GET'])
def howmany():
    return redirect('/')

if __name__ == "__main__":
    app.run(debug=True)


