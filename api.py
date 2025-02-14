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
        for user in users:
            if(name == user["name"]):
                return user, 200
        return "User not found", 404

    def post(self, name):
        parser = reqparse.RequestParser()
        parser.add_argument("age")
        parser.add_argument("occupation")
        args = parser.parse_args()

        for user in users:
            if(name == user["name"]):
                return "User with name {} already exists".format(name), 400

        user = {
            "name": name,
            "age": args["age"],
            "occupation": args["occupation"]
        }
        users.append(user)
        return user, 200

    def put(self, name):
            parser = reqparse.RequestParser()
            parser.add_argument("age")
            parser.add_argument("occupation")
            args = parser.parse_args()

            for user in users:
                if(name == user["name"]):
                    user["age"] = args["age"]
                    user["occupation"] = args["occupation"]
                    return user, 200

            user = {
                "name": name,
                "age": args["age"],
                "occupation": args["occupation"]
            }
            users.append(user)
            return user, 201

    def delete(self, name):
        global users
        users = [user for user in users if user["name"] != name]
        return "{} is deleted".format(name), 200


api.add_resource(User, "/user/<string:name>")

app.run(debug=True)
# Debug is for developing only
