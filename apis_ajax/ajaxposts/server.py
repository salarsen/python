from flask import Flask, render_template, redirect, request, flash, jsonify
from mysqlconnection import MySQLConnector

app = Flask(__name__)
mysql = MySQLConnector(app,"ajaxposts")

@app.route('/')
def index():
    query = "SELECT description, created_at FROM posts"
    results = mysql.query_db(query)
    return render_template('index.html',posts=results)

@app.route('/posts/create',methods=['POST'])
def add_post():
    new_post = request.form
    query = "INSERT INTO posts (description,created_at,updated_at) VALUES ('{}',NOW(),NOW())".format(new_post['description'])
    mysql.query_db(query)
    return_query = "SELECT * FROM posts"
    posts = mysql.query_db(return_query)
    return jsonify(posts)

app.run(debug=True)
