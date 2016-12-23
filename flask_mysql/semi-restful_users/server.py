from flask import Flask, render_template, redirect, request, session, flash
from mysqlconnection import MySQLConnector
# from validation import email_val, name_val
from flask_bcrypt import Bcrypt

app = Flask(__name__)
app.secret_key = "blahblahblahWhat"

mysql = MySQLConnector(app,"semirestfulldb")

@app.route('/')
def index():
    query = "SELECT id, CONCAT_WS(' ',first_name,last_name) AS full_name, email, DATE_FORMAT(created_at,'%Y') as created_on FROM users"
    results = mysql.query_db(query)

    content = render_template('list.html',users=results)

    return render_template('index.html',content=content)

@app.route('/users/new')
def create_user():
    content = render_template('user_form.html')
    return render_template('index.html',content=content)

@app.route('/users/<id>')
def show_user(id):
    #validate id is a number
    query = "SELECT id, CONCAT_WS(' ',first_name,last_name) AS full_name, email, DATE_FORMAT(created_at,'%Y') as created_on FROM users WHERE id = :id"
    data = {'id' : id}
    results = mysql.query_db(query,data)
    #if there is a result, show
    if results:
        content = render_template('show_user.html',id=results[0]['id'],full_name=results[0]['full_name'],email=results[0]['email'],created_on=results[0]['created_on'])
        return render_template('index.html',content=content)
    else:
        return index()
    #else return to index and flash errors saying user does not exists

@app.route('/users/create',methods=['POST'])
def add_user():
    #validate here...

    if request.form['user_id'] != "":
        #do update here
        query = "UPDATE users SET first_name = :first_name, last_name = :last_name, email = :email, updated_at = NOW() WHERE id = :user_id"
        data = {
            'first_name' : request.form['first_name'],
            'last_name' : request.form['last_name'],
            'email' : request.form['email'],
            'user_id' : request.form['user_id']
        }
        mysql.query_db(query,data)
        return show_user(request.form['user_id'])
    else:
        #on successful validation, if statement
        query = "INSERT INTO users (first_name, last_name, email, created_at, updated_at) VALUES (:first_name, :last_name, :email, NOW(), NOW())"
        data = {
            'first_name' : request.form['first_name'],
            'last_name' : request.form['last_name'],
            'email' : request.form['email']
        }
        result = mysql.query_db(query,data)
        return show_user(result)

@app.route('/users/<id>/edit')
def edit_user(id):
    query = "SELECT id, first_name, last_name, email, DATE_FORMAT(created_at,'%Y') as created_on FROM users WHERE id = :id"
    data = {'id' : id}
    results = mysql.query_db(query,data)
    if results:
        content = render_template('user_form.html',id=results[0]['id'],first_name=results[0]['first_name'],last_name=results[0]['last_name'],email=results[0]['email'],created_on=results[0]['created_on'])
        return render_template('index.html',content=content)
    else:
        return index()

@app.route('/users/<id>/destroy')
def delete_user(id):
    #no error checking needed, if user does not exist still considered successful
    query = "DELETE FROM users WHERE id = :id"
    data = {'id' : id}
    mysql.query_db(query,data)
    return index()

app.run(debug=True)
