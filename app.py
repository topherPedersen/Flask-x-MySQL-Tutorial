# Creating a Web App From Scratch Using Python Flask and MySQL
# https://code.tutsplus.com/tutorials/creating-a-web-app-from-scratch-using-python-flask-and-mysql--cms-22972

from flask import Flask, render_template, json, request
from flaskext.mysql import MySQL
from werkzeug import generate_password_hash, check_password_hash
 
app = Flask(__name__)
mysql = MySQL()

# MySQL Configurations
app.config['MYSQL_DATABASE_USER'] = 'UsernameGoesHERE'
app.config['MYSQL_DATABASE_PASSWORD'] = 'PasswordGoesHERE'
app.config['MYSQL_DATABASE_DB'] = 'bucket_list_db'
app.config['MYSQL_DATABASE_HOST'] = 'localhost' 
mysql.init_app(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/showSignUp')
def showSignUp():
    return render_template('signup.html')

@app.route('/signUp', methods=['POST'])
def signUp():
    try:
	    # Get Form Data
	    _name = request.form['inputName']
	    _email = request.form['inputEmail']
	    _password = request.form['inputPassword']

	    # validate the received values
	    if _name and _email and _password:
	        conn = mysql.connect()
	        cursor = conn.cursor()
	        _hashed_password = generate_password_hash(_password)
	        cursor.callproc('sp_createUser', (_name, _email, _hashed_password))
	        data = cursor.fetchall()
	        if len(data) is 0:
	            conn.commit()
	            return json.dumps({'message': 'User created successfully!'})
	        else:
	            return json.dumps({'error': str(data[0])})
	    else:
	        return json.dumps({'html':'<span>Enter the required fields</span>'})
    except Exception as e:
        return json.dumps({'error': str(e)})
    finally:
        cursor.close()
        conn.close()
