from flask import Flask
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SECRET_KEY'] = '3MPH8oY2EAgbLVy7RBMinwcBntggi7qeG3'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///flaskytsqlite.db'
db = SQLAlchemy(app)


from justsmthpy import routes