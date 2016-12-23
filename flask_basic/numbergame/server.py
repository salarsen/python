from flask import Flask, render_template, request, redirect, session
import random

app = Flask(__name__)
app.secret_key = "ThisIsSoSecure"

@app.route('/')
def homepage():
    # session['answer'] = int(random.randrange(1,101))
    # session['guess'] = int(0)
    # session['result'] = int(0)
    if 'answer' not in session:
        session['answer'] = random.randrange(1,101)
        session['guess'] = 0
        session['result'] = 0 # 1 too high, 0 default, -1 too low, 2 found, reset
    return render_template('index.html')

@app.route('/guess', methods=['POST'])
def aguess():
    session['guess'] = request.form['guess']
    print session['guess']
    print session['answer']
    print int(session['guess']) == int(session['answer'])
    if 'answer' not in session:
        session['answer'] = random.randrange(1,101)
    elif int(session['guess']) > int(session['answer']):
        session['result'] = 1
    elif int(session['guess']) < int(session['answer']):
        session['result'] = -1
    elif int(session['guess']) == int(session['answer']):
        session['result'] = 2
    else:
        session['result'] = 0
    return redirect('/')

@app.route('/reset')
def reset_game():
    session.pop('guess')
    session.pop('answer')
    session.pop('result')
    return redirect('/')

app.run(debug=True)
