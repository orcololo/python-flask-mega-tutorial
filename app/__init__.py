from flask import Flask

app = Flask(__name__)
app.config['DEBUG'] = True
app.config['SECRET_KEY'] = 'youreweaksasuskeyoulackofhashes'
from app import routes
