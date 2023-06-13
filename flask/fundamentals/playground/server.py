import numbers
from flask import Flask, render_template


app = Flask(__name__)

@app.route('/')
def hello():
    return 'HELLO'

@app.route('/play')
def blueboxes():
    return render_template('index.html',times=3, phrase = 'blue')

@app.route('/play/<num>')
def multipleboxes(num):
    return render_template('index.html', times = int(num), phrase = 'blue')

@app.route('/play/<num>/<color>')
def boxandcolors(num,color):
    return render_template('index.html', times = int(num), phrase = color)

if __name__=="__main__":
    app.run(debug=True)