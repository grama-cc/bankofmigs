from flask import Flask
app = Flask(__name__)

@app.route("/user/")
def user():
    return "Hello World!"

@app.route("/transaction/")
def transaction():
    return "Hello World!"

if __name__ == "__main__":
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://migs:migs@192.168.1.26/bank-of-migs-dev'
    app.run()
