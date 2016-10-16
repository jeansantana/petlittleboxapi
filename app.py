from flask import Flask
# from from flask_restful import reqparse, abort, Api, Resource, fields, marshal_with, marshal
from flask_restful import Api, Resource

app = Flask(__name__)
api = Api(app)

class Home(Resource):
    def get(self):
        return 'Wellcome to petlittlebox API'

api.add_resource(Home, '/')

if __name__ == '__main__':
    app.run()
