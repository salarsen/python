from flask import Flask, render_template, request, redirect

app = Flask(__name__)

@app.route('/') # set default

def main_pg():
    return render_template('index.html')

@app.route('/submitted', methods=['POST'])

def show_info():
    name = request.form['name']
    if name == "": # basic validation to check if empty
         name = "You can't be nameless!"
    dojo_loc = request.form['dojo_loc']
    fav_lang = request.form['fav_lang']
    comments = request.form['comments']
    return render_template('/submitted.html',name=name,dojo_loc=dojo_loc,fav_lang=fav_lang,comments=comments)

app.run(debug=True)
