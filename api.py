from flask import Flask, request
from flask_restful import Resource, Api
from json import dumps
from flask.ext.jsonpify import jsonify

app = Flask(__name__)
api = Api(app)

class Test(Resource):
    def get(self):
        return {'test': [1,2,5]} 


api.add_resource(Test, '/test')


if __name__ == '__main__':
     app.run(port='8500')