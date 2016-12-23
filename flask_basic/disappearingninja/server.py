from flask import Flask, render_template, redirect, session, request, flash

app = Flask(__name__)
app.secret_key = "disappearingninja"

@app.route('/')
def main_pg():
    return render_template('/index.html')

@app.route('/ninja')
def ninja_main():
    return render_template('/ninja.html')

@app.route('/ninja/<ninja_color>')
def ninja_color(ninja_color):
    if ninja_color == "blue" or ninja_color == "orange" or ninja_color == "purple" or ninja_color == "red":
        return render_template('/ninja_color.html',color=ninja_color)
    else:
        return render_template('/ninja_color.html',color="megan_fox")

app.run(debug=True)
