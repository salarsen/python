from flask import Flask, render_template, redirect, request, flash, jsonify
from mysqlconnection import MySQLConnector

app = Flask(__name__)
mysql = MySQLConnector(app,"ajaxnotesdb")

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/load_notes')
def load_notes():
    query = "SELECT * FROM notes"
    notes = mysql.query_db(query)
    return render_template('load_notes.html',notes=notes)


@app.route('/new_note',methods=['POST'])
def add_note():
    print "new_note"
    note_details = request.form
    query = "INSERT INTO notes (title, created_at, updated_at) VALUES ('{}',NOW(),NOW())".format(note_details['title'])
    result = mysql.query_db(query)
    print "added note " + str(result)
    # return render_template('load_notes.html',notes=notes)
    return redirect('/load_notes')

@app.route('/update',methods=['POST'])
def update_info():
    info_update = request.form
    if 'title' in info_update and 'description' in info_update:
        print "updating title and description"
        query = "UPDATE notes SET title = '{}',description = '{}',updated_at = NOW() WHERE id = '{}'".format(info_update['title'],info_update['description'],info_update['id'])
    elif 'title' in info_update and not 'description' in info_update:
        print "updating title only"
        query = "UPDATE notes SET title ='{}', updated_at = NOW() where id = '{}'".format(info_update['title'],info_update['id'])
    elif not 'title' in info_update and 'description' in info_update:
        print "updating description only"
        query = "UPDATE notes SET description ='{}', updated_at = NOW() where id = '{}'".format(info_update['description'],info_update['id'])
    mysql.query_db(query)
    return redirect('/load_notes')

@app.route('/delete',methods=['POST'])
def remove_notes():
    print "deleting note: " + request.form['id']
    query = "DELETE FROM notes WHERE id = '{}'".format(request.form['id'])
    mysql.query_db(query)
    # return redirect('/load_notes')
    return redirect('/load_notes')

app.run(debug=True)
