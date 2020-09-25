from flask import request, json, Response, Blueprint
from flask import render_template
from flask_cors import CORS, cross_origin
from ..models.StudentModel import StudentModel, StudentSchema

#Add your code here
student_api = Blueprint('student', __name__)
student_schema = StudentSchema()

# Create routes to add a student to the database.

@student_api.route('/add', methods=['POST'])
def create():
  req_data = request.get_json()
  data = student_schema.load(req_data)

  student = StudentModel(data)
  student.save()

  resp_data = student_schema.dumps(student)
  message = {'message': 'Added student to the list'}
  return custom_response(message ,201)

# Create routes to list all the added students
@student_api.route('/', methods=['GET'])
def get_all():
  students = StudentModel.get_all_students()
  resp = student_schema.dump(students, many=True)
  return custom_response(resp, 200)

@student_api.route('/test', methods=['GET'])
def get_one_user1():
  return "test is working"

def custom_response(res, status_code):
  """
  Custom Response Function
  """
  return Response(
    mimetype="application/json",
    response=json.dumps(res),
    status=status_code
  )

@staticmethod
def get_all_students():
    return StudentModel.query.all()
