from flask import Flask
app = Flask(__name__)
app.secret_key = "shhhhhh"
DB = "my_recipe"