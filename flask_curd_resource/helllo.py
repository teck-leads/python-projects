from flask import Flask
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

class Hello(Resource):
  def get(self):
    return {'message': 'Welcome to python flask restful Play ground!!!'},201, {'response_header1': 'some-message'}

api.add_resource(Hello, '/',
                 '/home/',
                 '/index/'
                 )

if __name__ == '__main__':
    app.run()