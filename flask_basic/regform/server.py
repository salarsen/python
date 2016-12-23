from flask import Flask, render_template, redirect, session, request, flash
import datetime #for hacker version
import re

app = Flask(__name__)
app.secret_key = "registrationform"

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9\.\+_-]+@[a-zA-Z0-9\._-]+\.[a-zA-Z]*$')

@app.route('/')
def main_pg():
    #do stuff here
    return render_template('/index.html')

@app.route('/process',methods=['POST'])
def process_info():
	#Spencer, this looks great! Your use of error as a boolean works quite well.
    error = False
    if len(request.form['email']) < 1:
        error = True
        flash(u'Email is empty','empty')
		#You don't necessarily need to make the flash messages unicode, but it doesn't hurt anything.
		#I really like the CSS you put on your flash messages!
    elif not EMAIL_REGEX.match(request.form['email']):
        error = True
        flash(u'Email is not valid','invalid')
    if len(request.form['first_name']) < 1:
        flash(u'First name is empty','empty')
        error = True
    if len(request.form['last_name']) < 1:
        flash(u'Last name is empty','empty')
        error = True
    if (request.form['password'] != request.form['confirm_pwd']):
        flash(u'Password does not match','match')
        error = True
    elif(len(request.form['password']) < 1 or len(request.form['confirm_pwd']) < 1):
        flash(u'Password cannot be empty','empty')
        error = True

    if not error:
        flash(u'Information Submitted Successfully!','submitted')

    return redirect('/')
app.run(debug=True)
#This looks really good. Great job!
