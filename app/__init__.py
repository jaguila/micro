from flask import Flask

#application object
app = Flask(__name__)
app.config.from_object('config')


from app import views