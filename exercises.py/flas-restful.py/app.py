from flask import Flask, jsonify
from flask_restful import Resource, Api
from module.courses_module import course_one, all_courses, course_two
from module.students_module import student_one, all_students, student_two
from module.events_module import event_one, all_events, event_two


app = Flask(__name__)

api = Api(app)

@app.route('/')
def home():
    return 'Hello,  World!'

 
api.add_resource(course_one, '/course/<int:course_id>/<name>')
api.add_resource(course_two, '/course/<int:course_id>/')

api.add_resource(student_one, '/student/<int:student_id>/<name>')
api.add_resource(student_two, '/student/<int:student_id>/')

api.add_resource(event_one, '/event/<int:event_id>/<event>')
api.add_resource(event_two, '/event/<int:event_id>/')


api.add_resource(all_courses, '/courses/')
api.add_resource(all_students, '/students/')
api.add_resource(all_events, '/events/')