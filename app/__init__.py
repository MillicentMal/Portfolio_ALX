import os
from flask_login import  login_required, LoginManager, UserMixin, login_manager, login_user, current_user, logout_user
from flask import Flask, request, session, render_template, url_for, flash, get_flashed_messages, message_flashed
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import PY3, Bcrypt
from sqlalchemy.orm import relationship
from flask_wtf import Form
from wtforms import StringField, PasswordField, validators
from werkzeug.utils import redirect, secure_filename
from wtforms.fields.numeric import IntegerField
from wtforms.fields.simple import EmailField, SubmitField, FileField







app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///storage.db'

# Secret Key!
app.config['SECRET_KEY'] = "my super secret key that no one is supposed to know"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
# Initialize The Database
db = SQLAlchemy(app)
with app.app_context():
    db.create_all()

UPLOAD_FOLDER =  '/static/uploads/'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
bcrypt = Bcrypt(app)

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'
login_manager.login_message = "Login to Continue"



def getApp():
    return app

from app import routes
