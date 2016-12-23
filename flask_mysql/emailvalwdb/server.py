from flask import Flask, render_template, redirect, flash, request, session
from mysqlconnection import MySQLConnector
import re

app = Flask(__name__)
app.secret_key = "SuperSecureKeyHere"

mysql = MySQLConnector(app, 'emailvaldb')

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9\.\+_-]+@[a-zA-Z0-9\._-]+\.[a-zA-Z]*$')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/add_email',methods=['POST'])
def add_email():
    error = False
    if len(request.form['email_address']) < 1:
        error = True
        flash('Email is empty','empty')
    if not EMAIL_REGEX.match(request.form['email_address']):
        error = True
        flash('Email is not valid!','invalid')

    # print error
    # return redirect('/')
    if not error:

        query = "INSERT INTO email_addresses (email, created_at, updated_at) VALUES (:email, NOW(), NOW())"

        data = {
            'email' : request.form['email_address']
        }

        flash("The email address you entered " + data['email'] + " is a VALID email address! Thank You!",'valid')

        mysql.query_db(query, data)

        query = "SELECT id, email, DATE_FORMAT(created_at, '%M %e, %Y, %l:%i %p') AS created_date FROM email_addresses ORDER BY created_at DESC"

        emails = mysql.query_db(query)

        return render_template('index.html',valid_emails=emails)
    else:
        return redirect('/')

@app.route('/remove/<email_id>',methods=['POST'])
def remove_email(email_id):
    # remove the email specified
    query = "DELETE FROM email_addresses WHERE id = :id"
    data = {
        'id' : email_id
    }
    mysql.query_db(query,data)
    # reload index page with remaining emails if any...
    query = "SELECT id, email, DATE_FORMAT(created_at, '%M %e, %Y, %l:%i %p') AS created_date FROM email_addresses ORDER BY created_at DESC"

    emails = mysql.query_db(query)

    return render_template('index.html',valid_emails=emails)

app.run(debug=True)
