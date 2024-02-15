from flask import Flask
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database.db"

db = SQLAlchemy(app)




class User(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(20), nullable= False)
    surname = db.Column(db.String(20), nullable= False)
    email = db.Column(db.String(40), nullable= False)
    password = db.Column(db.String, nullable= False)

