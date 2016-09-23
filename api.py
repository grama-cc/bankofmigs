from flask import Flask, request
from flask.wrappers import Response

app = Flask(__name__)

@app.route("/user/<int:username>")
def user(user_id):
    from db import User
    user = User.query.filter_by(id=user_id).first()
    return {'id': user.id, 'username': user.username, 'email': user.email, 'balance': user.balance}

@app.route("/transaction/", methods=['GET', 'POST'])
def transaction():
    from db import User, Transaction, db
    if request.method == 'POST':
        sender_username = request.form.get('sender', None)
        receiver_username = request.form.get('receiver', None)

        sender = User.query.filter_by(username=sender_username).first()
        if not sender:
            sender = User(sender_username)
        receiver = User.query.filter_by(id=receiver_username).first()
        if not receiver:
            receiver = User(receiver_username)

        amount = request.form.get('amount')
        transaction = Transaction()
        transaction.sender = sender_username
        transaction.receiver = receiver_username
        transaction.value = amount
        sender.balance -= amount
        receiver.balance += amount

        db.session.add(sender)
        db.session.add(receiver)
        db.session.commit()
    else:
        pass
    return Response(response={}, status=200, mimetype="application/json")


@app.route("/transactions/", methods=['GET'])
def transactions():
    return "BAL"

if __name__ == "__main__":
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:@localhost:3306/bankofmigs'
    app.run(debug=True)
