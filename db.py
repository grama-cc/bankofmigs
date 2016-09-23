from flask_sqlalchemy import SQLAlchemy
from api import app
db = SQLAlchemy(app)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True)
    email = db.Column(db.String(120), unique=True)
    balance = db.Column(db.Float())

    loans = db.relationship('Transaction', backref='sender', lazy='dynamic')
    debits = db.relantionship('Transaction', backref='receiver', lazy='dynamic')

    def __init__(self, username, email):
        self.username = username
        self.email = email

    def __repr__(self):
        return '<User: %r>' % self.username

class Transaction(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    sender_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    receiver_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    description = db.Column(db.String(120))
    date = db.Column(db.DateTime)
    value = db.Column(db.Float)

    def __init__(self, username, email):
        self.username = username
        self.email = email

    def __repr__(self):
        return '<User: %r>' % self.username
