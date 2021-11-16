from app import app
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
from app.models import User


class EditProfileForm(Form):
    name = StringField('Name',  validators=[validators.input_required(), validators.Length(min=1, max=50)])
    email = EmailField('Email',  validators=[validators.input_required(), validators.Length(min=1, max=50)])
    username = StringField('Username',  validators=[validators.input_required(), validators.Length(min=1, max=50)])
    submit = SubmitField("Update Account Details")

class Reset(Form):
    username = StringField('Username',  validators=[validators.input_required(), validators.Length(min=1, max=50)])
    password = PasswordField('password',  validators=[validators.input_required()])
    confirm= PasswordField('Confirm',  validators=[validators.input_required(), validators.Length(min=1, max=50), validators.EqualTo('password',
                             message="Passwords must match")])
    submit = SubmitField("RESET")
    
class EditProduct(Form):
    name = StringField('Name',  validators=[validators.input_required(), validators.Length(min=1, max=50)])
    price = IntegerField('Price',  validators=[validators.input_required(), validators.Length(min=1, max=50)])
    description = StringField('description',  validators=[validators.input_required(), validators.Length(min=1, max=50)])
    submit = SubmitField("Update")

    
class Addwork(Form):
    name = StringField('Name',  validators=[validators.input_required(), validators.Length(min=1, max=50)])
    price = StringField('price',  validators=[validators.input_required(), validators.Length(min=1, max=50)])
    description = StringField('Description',  validators=[validators.input_required(), validators.Length(min=1, max=50)])
    file = FileField("Image")
    submit = SubmitField("Add Work")

    
class Registration(Form):
    phone = StringField('Phone',  validators=[validators.input_required(), validators.Length(min=1, max=50)])
    type_work = StringField("Type of Service", validators=[validators.input_required()])
    location = StringField("Location in Kigali", validators=[validators.input_required()])
    flexibility = StringField("Mobile or Salon: Can you travel for customers or they come to you. ", validators=[validators.input_required()])
    submit = SubmitField("Register")


class Signup(Form):
    name = StringField('Name',  validators=[validators.input_required(), validators.Length(min=1, max=50)])
    email = StringField('Email',  validators=[validators.input_required(), validators.Length(min=1, max=50)])
    username = StringField('Username',  validators=[validators.input_required(), validators.Length(min=1, max=50)])
    
    password = PasswordField('password',  validators=[validators.input_required()])
    confirm= PasswordField('Confirm',  validators=[validators.input_required(), validators.Length(min=1, max=50), validators.EqualTo('password',
                             message="Passwords must match")])
    submit = SubmitField("Register")




