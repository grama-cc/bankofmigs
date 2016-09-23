from flask_sqlalchemy import SQLAlchemy
from api import app
db = SQLAlchemy(app)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True)
    balance = db.Column(db.Float(), default=0)

    def __init__(self, username):
        self.username = username

    def __repr__(self):
        return '<User: %r>' % self.username

class Transaction(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    sender = db.Column(db.String(120))
    receiver = db.Column(db.String(120))
    date = db.Column(db.DateTime)
    amount = db.Column(db.Float)

    def __init__(self):
        pass

    def __repr__(self):
        return '<User: %r>' % self.username
