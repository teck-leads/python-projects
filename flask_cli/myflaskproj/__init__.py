from flask import Flask

app = Flask(__name__)

#from myflaskproj import projectapp
from myflaskproj.commands import power, repeat
app.cli.add_command(power)
app.cli.add_command(repeat)  