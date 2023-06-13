from flask import Flask, render_template, request, redirect
# import the class from friend.py
from friend import Friend
app = Flask(__name__)



@app.route("/")
def index():
    # call the get all classmethod to get all friends
    friends = Friend.get_all()
    print(friends)
    return render_template("index.html", myfriends = friends)

@app.route('/createuser')
def create():
    return render_template('friendform.html')

@app.route('/savefriend', methods=['POST'])
def savehomie():
    homie = request.form
    data = {
        'fname': homie['fname'],
        'lname': homie['lname'],
        'occ': homie['occ']
    }
    x = Friend.save(data)
    print(x)
    return redirect('/')




if __name__ == "__main__":
    app.run(debug=True)