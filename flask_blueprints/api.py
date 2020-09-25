from flask import Flask, request, jsonify,  make_response
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate, MigrateCommand

#app intialization
app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///schoolmanagement.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']= False


#db inititalization
db = SQLAlchemy(app)
migrate = Migrate(app=app, db=db)

#Register the views in student view and teacher view as blueprints using the following prefixes.
# url_prefix for teachers: /api/teachers
# url_prefix for students: /api/students
from src.views.StudentView import student_api as student_blueprint
from src.views.TeacherView import teacher_api as teacher_blueprint

app.register_blueprint(student_blueprint, url_prefix="/api/students")
app.register_blueprint(teacher_blueprint, url_prefix="/api/teachers")



