from flask_restful import Resource
from flask import jsonify

courses_list = [
    {"id": 1, "name": "COS450"},
    {"id": 2, "name": "INF480"},
    {"id": 3, "name": "FAR330"}
]

class course_one(Resource):
    

    
    def put(self,course_id,name):   
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

def post(self,course_id,name):  

        id_exist = False
        for i in range(len(courses_list)):
            if courses_list[i-1]['id'] == course_id:
                id_exist = True
    
        if id_exist == False:
            courses_list.append(dict({'id': course_id, 'name': name}))
            return jsonify(courses_list)
        else:
            return "ID already exists."

    

class course_two(Resource):

    def get(self, course_id):  
        flag = False
        for course in courses_list:
            if course["id"] == course_id:
                flag = True
                return jsonify(course)
        if flag == False:    
            return "ID does not exist."
       
    def delete(self, course_id):      
        flag = False
        for i in range(len(courses_list)): 
            if courses_list[i]['id'] == course_id: 
                del courses_list[i]
                flag = True
                return "This course is deleted."

        if flag == False:
            return "ID does not exist."

class all_courses(Resource):
    def get(self):
return jsonify(courses_list)
