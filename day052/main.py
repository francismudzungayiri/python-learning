#### CREATING RESTFUL APIs

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_restful import Resource, Api, reqparse, fields, marshal_with, abort




app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
db = SQLAlchemy(app)
api = Api(app)


class UserModel(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(80), unique=True, nullable=False)
    
    def __repr__(self):
        return f"name = {self.username}, email = {self.email}"



user_args = reqparse.RequestParser()
user_args.add_argument

@app.route('/')
def index():
    return "<h1> FLASK REST API"


if __name__ =='__main__':
    app.run(debug=True)