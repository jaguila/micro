from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy

#application object
app = Flask(__name__)
app.config.from_object('config')
#creating database
db = SQLAlchemy(app)

#app is the folder that contains our views  and models
from app import views, models