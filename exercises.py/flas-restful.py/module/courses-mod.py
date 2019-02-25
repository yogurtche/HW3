from flask_restful import Resource
from flask import jsonify

courses_list = [
    {"id": 1, "name": "MAT230"},
    {"id": 2, "name": "COS350"},
    {"id": 3, "name": "ENG330"}
]

class course_one(Resource):
    

    
    def put(self,course_id,name):   #Put Method
        id_exist = False

        for a in courses_list:
            if a["id"] == course_id:
                a.update({'name': name})
                id_exist = True
                return jsonify(a)

        if id_exist == False:
            courses_list.append(dict({'id': course_id, 'name': name}))
            return jsonify(courses_list)

        return jsonify(courses_list)

def post(self,course_id,name):  #Post method

        id_exist = False
        for i in range(len(courses_list)):
            if courses_list[i-1]['id'] == course_id:
                id_exist = True
    
        if id_exist == False:
            courses_list.append(dict({'id': course_id, 'name': name}))
            return jsonify(courses_list)
        else:
            return "ID already exist"

    

class course_two(Resource):

    def get(self, course_id):  #Get Method
        flag = False
        for course in courses_list:
            if course["id"] == course_id:
                flag = True
                return jsonify(course)
        if flag == False:    
            return "ID not Found!"
       
    def delete(self, course_id):      #Delete method
        flag = False
        for i in range(len(courses_list)): 
            if courses_list[i]['id'] == course_id: 
                del courses_list[i]
                flag = True
                return "The course is  deleted!"

        if flag == False:
            return "ID was not found!"

class all_courses(Resource):
    def get(self):
return jsonify(courses_list)