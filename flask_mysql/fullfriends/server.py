from flask import Flask, render_template, redirect, request, session, flash
from mysqlconnection import MySQLConnector
import re

app = Flask(__name__)
app.secret_key = "SomeSecretGoesHere"

mysql = MySQLConnector(app, "fullfriendsdb")

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9\.\+_-]+@[a-zA-Z0-9\._-]+\.[a-zA-Z]*$')

@app.route('/')
def index():
    query = "SELECT id, CONCAT_WS(' ',first_name, last_name) AS friend_name, email_address, DATE_FORMAT(created_at, '%M %e, %Y, %l:%i %p') AS created_date, DATE_FORMAT(updated_at, '%M %e, %Y, %l:%i %p') AS updated_date FROM friends ORDER BY created_at DESC"

    friends = mysql.query_db(query)
    return render_template('index.html',friends_info = friends)

@app.route('/friends',methods=['POST'])
def create():
    error = False
    if len(request.form['first_name']) < 1:
        error = True
        flash ('First name cannot be empty!', 'empty')
    if len(request.form['last_name']) < 1:
        error = True
        flash ('Last name cannot be empty!','empty')
    if len(request.form['email_address']) < 1:
        error = True
        flash('Email is empty','empty')
    if not EMAIL_REGEX.match(request.form['email_address']):
        error = True
        flash('Email is not valid!','invalid')

    if not error:
        # lets check if friend already exists in database, if they do redirect to edit page
        query = "SELECT * FROM friends WHERE first_name = :first_name AND last_name = :last_name"
        data = {
            'first_name' : request.form['first_name'],
            'last_name' : request.form['last_name'],
            'email_address' : request.form['email_address']
        }
        found_friend = mysql.query_db(query, data)
        if found_friend:
            return render_template('edit.html',edit_friend=found_friend)
        else:
            #lets add this friend now
            query = "INSERT INTO friends (first_name, last_name, email_address, created_at, updated_at) VALUES (:first_name, :last_name, :email_address, NOW(), NOW())"
            # data define above
            mysql.query_db(query,data)
            # do not need to fetch data for index since it's loading that already, flash a success message however!
            flash("Successfully added " + data['first_name'] + " " + data['last_name'] + " (" + data['email_address'] + ") to the database!",'success')
            return redirect('/')
    else:
        return redirect('/')

@app.route('/friends/<id>/edit')
def edit_friend(id):
    query = "SELECT * FROM friends WHERE id = :id"
    print id
    data = {
        'id' : id
    }
    friend = mysql.query_db(query,data)
    if friend:
        return render_template('edit.html',edit_friend=friend)
    else:
        flash ('Unable to find this friend','notfound')
        return redirect('/')

@app.route('/friends/<id>', methods=['POST'])
def update_friend(id):
    # verify inputs then update, otherwise redirecterror = False
    # ideally we would build an update string here rather than updating whole row, that way we only update the things that have been modified
    error = False
    if len(request.form['first_name']) < 1:
        error = True
        flash ('On edit: First name cannot be empty!', 'empty')
    if len(request.form['last_name']) < 1:
        error = True
        flash ('On edit: Last name cannot be empty!','empty')
    if len(request.form['email_address']) < 1:
        error = True
        flash('On edit: Email is empty','empty')
    if not EMAIL_REGEX.match(request.form['email_address']):
        error = True
        flash('On edit: Email is not valid!','invalid')

    if not error:
        query = "UPDATE friends SET first_name = :first_name, last_name = :last_name, email_address = :email_address, updated_at = NOW() WHERE id = :id"
        data = {
            'id' : id,
            'first_name' : request.form['first_name'],
            'last_name' : request.form['last_name'],
            'email_address' : request.form['email_address']
        }
        mysql.query_db(query,data)
        flash("Successfully updated " + data['first_name'] + " " + data['last_name'] + " (" + data['email_address'] + ") in the database!",'success')
        return redirect('/')
    else:
        # query = "SELECT * FROM friends WHERE id = :id"
        # data = {
        #     'id' : id
        # }
        # friend = mysql.query_db(query,data)
        # return render_template('edit.html',edit_friend=friend)
        return redirect('/')

@app.route('/friends/<id>/delete')
def destroy(id):
    query = "DELETE FROM friends WHERE id = :id"
    data = {
        'id' : id
    }
    mysql.query_db(query,data)
    flash ('Sucessfully removed your friend','success')
    return redirect('/')

app.run(debug=True)
