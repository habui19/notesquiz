from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager

app = Flask(__name__)
app.config['SECRET_KEY'] = '67b20c96fb2395a6c78716ffa2af036c'
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://ctsxwecfbwedhx:aac5c85e397b15803b364c1a3f3d807f670909b036659274925b809e683d5306@ec2-54-221-215-228.compute-1.amazonaws.com:5432/d36lsv3hrqqv7'
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'
login_manager.login_message_category = 'info'

from notesquiz import routes