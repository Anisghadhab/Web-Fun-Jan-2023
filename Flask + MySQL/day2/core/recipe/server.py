from flask import Flask
from flask_app import app
# ALWAYS IMPORT CONROLLERS
from flask_app.controllers import users
from flask_app.controllers import recipes


if __name__ == ("__main__"):
    app.run(debug = True)