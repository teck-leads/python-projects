from flask import request, json, Response, Blueprint
from flask import render_template
from flask_cors import CORS, cross_origin
from ..models.TeacherModel import TeacherModel, TeacherSchema

#Add your code here
teacher_api = Blueprint('teacher', __name__)
teacher_schema = TeacherSchema()

# Create routes to add a teacher to the database.
@teacher_api.route('/add', methods=['POST'])
def create():
  req_data = request.get_json()
  data = teacher_schema.load(req_data)

  teacher = TeacherModel(data)
  teacher.save()

  resp_data = teacher_schema.dumps(teacher)
  message = {'message': 'Added teacher to the list'}
  return custom_response(message ,201)



# Create routes to list all the added teachers.
@teacher_api.route('/', methods=['GET'])
def get_all():
  teachers = TeacherModel.get_all_teachers()
  resp = teacher_schema.dump(teachers, many=True)
  return custom_response(resp, 200)


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
def get_all_teachers():
    return TeacherModel.query.all()
