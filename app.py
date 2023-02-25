from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.secret_key = "Secret Key"

#SqlAlchemy Database Configuration With Mysql
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://admin:admin12345@database-1.cl7j5j2rhsoe.us-west-2.rds.amazonaws.com/flaskaws'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

@app.route('/')
@app.route('/home')
def home():

    return "hello world"


if __name__ == '__main__':
    app.run()
