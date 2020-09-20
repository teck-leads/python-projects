from flask import render_template
from myflaskproj import app

# Define a route to display a message with heading h1 as Welcome to MyFlaskProj

@app.route('/', methods=['GET'])
def homePage():
    return "<h1>Welcome to MyFlaskProj </h1>"
