from flask import Flask
from config import Config
from flask_bootstrap import Bootstrap

#Instantiating the app as a Flask object, getting configuration from config.py
app= Flask(__name__)
app.config.from_object(Config)
bootstrap=Bootstrap(app)

from app import routes
