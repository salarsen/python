from flask import Flask, render_template, request, redirect, session

app = Flask(__name__)
app.secret_key = "hellothere"

@app.route('/') # set default

def main_pg():
    if 'name' not in session:
        session['name'] = 0
        session['comments'] = 0
    return render_template('index.html')

@app.route('/submitted', methods=['POST'])

def show_info():
    name = request.form['name']
    comments = request.form['comments']
    session['name'] = 0
    session['comments'] = 0
    if name == "": # basic validation to check if empty
        session['name'] = 1
    if comments == "":
        session['comments'] = 1
    if len(comments) > 120:
        session['comments'] = -1

    if session['name'] == 1 or session['comments'] == 1 or session['comments'] == -1:
        return redirect('/')
    else:
        session.pop('name')
        session.pop('comments')
        dojo_loc = request.form['dojo_loc']
        fav_lang = request.form['fav_lang']
        return render_template('/submitted.html',name=name,dojo_loc=dojo_loc,fav_lang=fav_lang,comments=comments)

app.run(debug=True)
