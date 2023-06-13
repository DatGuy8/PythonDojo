from flask import Flask, render_template, redirect, session, request


app = Flask(__name__)
app.secret_key = 'myprecious1'


@app.route('/')
def home():


    return render_template('index.html')

@app.route('/process', methods=['POST'])
def returninfo():
    print('GOT IT')
    session['userdata'] = request.form
    print(request.form)


    return redirect('/results')

@app.route('/results')
def results():
    x=session['userdata']
    print(session['userdata'])
    print('SESSION DATA')
    return render_template('results.html', name=x['username'], location=x['location'], language=x['language'], comments=x['comments'] )







if __name__ == "__main__":
    app.run(debug=True)
