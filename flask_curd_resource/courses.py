from flask import Flask, request
from flask_restful import Resource, Api, abort


app = Flask(__name__)
api = Api(app)
play_courses = {}

class PlayCourses(Resource):
    
    def post(self, course_id):
      if course_id not in play_courses:
        play_courses[course_id] = request.form['course_name']
        return {course_id: play_courses[course_id]}
      abort(404, message="Course_Id {} already exists".format(course_id))


    def get(self, course_id=None):
        if course_id is None:
            return play_courses
        if course_id not in play_courses:
            abort(404, message="Course_Id {} doesn't exist".format(course_id))
        return play_courses[course_id]
    
    def put(self, course_id):
        if course_id not in play_courses:
            abort(404, message="Course_Id {} doesn't exist".format(course_id))
            
        play_courses[course_id] = request.form['course_name']
        return {course_id: play_courses[course_id]}

    def delete(self, course_id):
        if course_id in play_courses:
            response_string = '{} course is deleted'.format(play_courses[course_id])
            del play_courses[course_id]
            return response_string
        abort(404, message="Course_Id {} doesn't exist".format(course_id))


api.add_resource(PlayCourses, 
              '/Courses/',
              '/Courses/<int:course_id>')
# api.add_resource(PlayCourses, '/Courses/<int:course_id>')
if __name__ == '__main__':
    app.run()