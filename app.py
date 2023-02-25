from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.secret_key = "Secret Key"


@app.route('/')
@app.route('/home')
def home():

    return "hello world"


if __name__ == '__main__':
    app.run()
