import json

from flask import Flask, request
from flask.ext.cors.extension import CORS
from flask.wrappers import Response
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
CORS(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:@localhost:3306/bankofmigs'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
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


@app.route("/user/<int:username>")
def user(user_id):
    user = User.query.filter_by(id=user_id).first()
    return {'id': user.id, 'username': user.username, 'email': user.email, 'balance': user.balance}

@app.route("/users/")
def users():
    data = []
    users = User.query.all()
    for u in users:
        data.append({'id': u.id, 'username': u.username, 'balance': u.balance})
    return Response(response=json.dumps(data), status=200, mimetype="application/json")

@app.route("/transaction/", methods=['GET', 'POST'])
def transaction():
    if request.method == 'POST':
        sender_username = request.form.get('sender', None)
        receiver_username = request.form.get('receiver', None)

        sender = User.query.filter_by(username=sender_username).first()
        if not sender:
            sender = User(sender_username)
        receiver = User.query.filter_by(username=receiver_username).first()
        if not receiver:
            receiver = User(receiver_username)

        amount = float(request.form.get('amount'))
        transaction = Transaction()
        transaction.sender = sender_username
        transaction.receiver = receiver_username
        transaction.value = amount
        sender.balance = sender.balance or float(0)
        receiver.balance = receiver.balance or float(0)

        sender.balance -= amount
        receiver.balance += amount

        db.session.add(sender)
        db.session.add(receiver)
        db.session.add(transaction)
        db.session.commit()
    else:
        pass
    return Response(response={}, status=200, mimetype="application/json")


@app.route("/transactions/", methods=['GET'])
def transactions():
    data = []
    transactions = Transaction.query.all()
    for t in transactions:
        data.append({'sender': t.sender, 'receiver': t.receiver, 'amount': t.amount})
    return Response(response=json.dumps(data), status=200, mimetype="application/json")

if __name__ == "__main__":
    app.run()
