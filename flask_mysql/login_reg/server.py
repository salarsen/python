from flask import Flask, render_template, redirect, request, session, flash
from mysqlconnection import MySQLConnector
from flask_bcrypt import Bcrypt
import re

app = Flask(__name__)

#things we need...
app.secret_key = "AVerySecretKey"
bcrypt = Bcrypt(app)
mysql = MySQLConnector(app,"loginandreg")

@app.route('/')
def index():
    return render_template('index.html')

#regex: anything but letters found, error

@app.route('/register',methods=['POST'])
def register():
    error = False

    NAME_REGEX = re.compile(r'[a-zA-Z_-]+$')
    #check first name
    if len(request.form['first_name']) < 2:
        error = True
        flash ('First name cannot be less than two characters','invalid')
    if not NAME_REGEX.match(request.form['first_name']):
        error = True
        flash ('Your first name can\'t contain any thing but letters silly','invalid')

    #check last name
    if len(request.form['last_name']) < 2:
        error = True
        flash ('Last name cannot be less than two characters','invalid')
    if not NAME_REGEX.match(request.form['last_name']):
        error = True
        flash ('Your last name can\'t contain any thing but letters silly','invalid')

    #regex: email verification stirng
    EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9\.\+_-]+@[a-zA-Z0-9\._-]+\.[a-zA-Z]*$')
    #check email
    if len(request.form['email_address']) < 1:
        error = True
        flash ('We would really like to spam your inbox, please provide your email','invalid')
    if not EMAIL_REGEX.match(request.form['email_address']):
        error = True
        flash ('This is not a valid email, try again!','invalid')

    #check password length
    if len(request.form['password']) < 8 or len(request.form['confirm_password']) < 8:
        error = True
        flash ('Password must be a minimum of 8 characters long','invalid')
    else: #check hash of password = hash of confirm password
        pw_hash = bcrypt.generate_password_hash(request.form['password'])
        if not bcrypt.check_password_hash(pw_hash,request.form['confirm_password']):
            error = True
            flash ('Passwords do not match','mismatch')

    if not error:
        # check if user is registered already, if so, error and tell them they are registered and login
        data = {
            'first_name' : request.form['first_name'],
            'last_name' : request.form['last_name'],
            'email_address' : request.form['email_address'],
            'pw_hash' : pw_hash
        }

        query = "SELECT * FROM users WHERE first_name = :first_name AND last_name = :last_name AND email = :email_address"

        check_result = mysql.query_db(query,data)

        if not check_result:
            query = "INSERT INTO users (first_name, last_name, email, pwd_hash, created_at, updated_at) VALUES (:first_name, :last_name, :email_address, :pw_hash, NOW(), NOW())"

            insert_result = mysql.query_db(query,data)

            if not insert_result:
                flash ('Error inserting new user','error')
                return render_template('index.html',first_name=request.form['first_name'],last_name=request.form['last_name'],email_address=request.form['email_address'])
            else:
                session['user_id'] = insert_result
                return redirect('/')
        else:
            flash ('This user already exists, please login!','error')
            return render_template('index.html',login_address=request.form['email_address'])
    else:
        return render_template('index.html',first_name=request.form['first_name'],last_name=request.form['last_name'],email_address=request.form['email_address'])

@app.route('/login',methods=['POST'])
def login():
    #probably should do some sanitation here...
    query = "SELECT * FROM users WHERE email = :email_address"
    data = {
        'email_address' : request.form['login_email'],
    }

    login_result = mysql.query_db(query,data)
    # print login_result
    if bcrypt.check_password_hash(login_result[0]['pwd_hash'],request.form['login_password']):
        session['user_id'] = login_result[0]['id']
        return redirect('/')
    elif login_result and not bcrypt.check_password_hash(login_result[0]['pwd_hash'],request.form['login_password']):
        flash('Incorrect password','invalid')
        return render_template('index.html',login_email=request.form['login_email'])
    else:
        flash('Unable to find this user','notfound')
        return redirect('/')
    # return redirect('/')

@app.route('/logout')
def logout():
    session.pop("user_id")
    return redirect('/')

app.run(debug=True)
