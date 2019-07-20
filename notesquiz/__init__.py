from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager

app = Flask(__name__)
app.config['SECRET_KEY'] = '67b20c96fb2395a6c78716ffa2af036c'
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://jxwgwrbrkgzzja:d1532973b717fdd5b207fc4c4245b16cc5c17ebb48b4cf952a6c525e8b3e21b1@ec2-23-21-115-109.compute-1.amazonaws.com:5432/d2irs2rjm5rttq'
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'
login_manager.login_message_category = 'info'

from notesquiz import routes
