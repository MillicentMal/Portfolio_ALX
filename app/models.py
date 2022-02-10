from app.app import db 
from flask_login import  login_required, LoginManager, UserMixin, login_manager, login_user, current_user, logout_user
from flask import Flask, request, session, render_template, url_for, flash, get_flashed_messages, message_flashed


class Seller(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(256), unique=True)
    email = db.Column(db.String(30), unique=True)
    location = db.Column(db.String(30), unique=True)
    flexibility = db.Column(db.String(30), unique=True)
    username = db.Column(db.String(30), unique=True)
    phone = db.Column(db.Integer, nullable=False)
    work =  db.relationship('Work', backref='seller', cascade="all, delete-orphan",  lazy=True)
    type_work = db.Column(db.String(50), nullable=False)
    folder = db.Column(db.String(256), unique=True)

class Work(db.Model):
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(256), unique=True)
    price = db.Column(db.Integer, nullable=False)
    description = db.Column(db.String(100))
    seller_id = db.Column(db.Integer, db.ForeignKey('seller.id'))
    img =  db.Column(db.String(100))


class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(256), unique=True)
    email = db.Column(db.String(30), unique=True)
    username = db.Column(db.String(30), unique=True)
    password = db.Column(db.String(256), nullable=False)

# ROUTES 