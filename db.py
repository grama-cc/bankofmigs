from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy(app)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True)
    email = db.Column(db.String(120), unique=True)
    balance = db.Column(db.Float())

    def __init__(self, username, email):
        self.username = username
        self.email = email

    def __repr__(self):
        return '<User: %r>' % self.username

class Transaction(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True)
    description = db.Column(db.String(120), unique=True)
    date = db.Column(db.DateTime())
    value = db.Column(db.Float, unique=True)

    def __init__(self, username, email):
        self.username = username
        self.email = email

    def __repr__(self):
        return '<User: %r>' % self.username
