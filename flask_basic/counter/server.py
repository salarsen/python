from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = "NotARealSecret"

@app.route('/')
def homepage():
    if 'counter' not in session:
        session['counter'] = 1
        session['fullcircle'] = 0
    else:
        if session['fullcircle'] == 0:
            session['counter'] += 1
        else:
            session['fullcircle'] = 0
    return render_template('index.html')

@app.route('/ninjas')
def ninjas_add():
    if 'counter' not in session:
        session['counter'] = 2
        session['fullcircle'] = 1
    else:
        session['counter'] += 2
        session['fullcircle'] = 1
    return redirect('/')

@app.route('/hackers')
def hacker_reset():
    session['counter'] = 1
    session['fullcircle'] = 1
    return redirect('/')

app.run(debug=True)
