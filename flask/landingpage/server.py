from flask import Flask, render_template  # Import Flask to allow us to create our app.
app = Flask(__name__)    # Global variable __name__ tells Flask whether or not we are running the file
                         # directly, or importing it as a module.
@app.route('/')          # The "@" symbol designates a "decorator" which attaches the following
                         # function to the '/' route. This means that whenever we send a request to
                         # localhost:5000/ we will run the following "hello_world" function.
def index():
    return render_template('index.html')  # Return 'Hello World!' to the response.

@app.route('/ninjas')
def ninjas():
    return render_template('/ninjas.html')

@app.route('/dojos/dojo')
def dojos():
    return render_template('/dojos/dojos.html')

app.run(debug=True)
