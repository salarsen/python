from flask import Flask, render_template, request, redirect, session
import random
import datetime

app = Flask(__name__)
app.secret_key = "SuperSecureKeyHere"

@app.route('/')
def main_pg():
    if "goldcount" not in session:
        session['goldcount'] = 0
        session['activities'] = []
    return render_template('/index.html')

@app.route('/process_money',methods=['POST'])
def process():
    options[request.form['building']]()
    return redirect('/')

@app.route('/reset')
def resetgame():
    session['activities'] = []
    session['goldcount'] = 0
    return redirect('/')

def farm():
    earnings = random.randrange(10,21)
    session['goldcount'] += earnings
    session['activities'].insert(0,["green","Earned " + str(earnings) + " gold from the farm (" + str(datetime.datetime.now().strftime("%m/%d/%Y %I:%M%p")) + ")"])

def cave():
    earnings = random.randrange(5,11)
    session['goldcount'] += earnings
    session['activities'].insert(0,["green","Earned " + str(earnings) + " gold from the cave (" + str(datetime.datetime.now().strftime("%m/%d/%Y %I:%M%p")) + ")"])

def house():
    earnings = random.randrange(2,6)
    session['goldcount'] += earnings
    session['activities'].insert(0,["green","Earned " + str(earnings) + " gold from the house (" + str(datetime.datetime.now().strftime("%m/%d/%Y %I:%M%p")) + ")"])

def casino():
    earnings = random.randrange(0,51)
    session['goldcount'] -= earnings
    session['activities'].insert(0,["red","Entered a casino and lost " + str(earnings) + " gold... Ouch ... (" + str(datetime.datetime.now().strftime("%m/%d/%Y %I:%M%p")) + ")"])

options = {"farm" : farm, "cave" : cave, "house" : house, "casino" : casino,}

app.run(debug=True)
