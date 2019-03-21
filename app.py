# Creating a Web App From Scratch Using Python Flask and MySQL
# https://code.tutsplus.com/tutorials/creating-a-web-app-from-scratch-using-python-flask-and-mysql--cms-22972

from flask import Flask, render_template, json, request
 
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/showSignUp')
def showSignUp():
    return render_template('signup.html')

@app.route('/signUp', methods=['POST'])
def signUp():
    # Get Form Data
    _name = request.form['inputName']
    _email = request.form['inputEmail']
    _password = request.form['inputPassword']

    # validate the received values
    if _name and _email and _password:
        return json.dumps({'html':'<span>All fields good!</span>'})
    else:
        return json.dumps({'html':'<span>Enter the required fields</span>'})
