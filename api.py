from flask import Flask
from flask_restful import Api, Resource, reqparse
# Flask, Api and Resource are classses
# reqparse is request parsing interface

app = Flask(__name__)
api = Api(app)

users = [
    {
        "name": "Nicholas",
        "age": 42,
        "occupation": "Network Engineer"
    },
    {
        "name": "Jane",
        "age": 50,
        "occupation": "Occupational Therapist"
    },
    {
        "name": "Steven",
        "age": 35,
        "occupation": "Builder"
    },
]

class User(Resource):
    def get(self, name):

    def post(self, name):

    def put(self, name):

    def delete(self, name):
