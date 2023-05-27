import json
from flask import Flask, request
from flask_cors import CORS
from utils.utility import driverRequired
from .admin import admin
from .drivers import drivers

app = Flask('__name__')
CORS(app)

app.register_blueprint(admin)
app.register_blueprint(drivers)

@app.route('/')
def home():
    return 'roti-7 server in up here'


