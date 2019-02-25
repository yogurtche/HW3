from flask_restful import Resource
from flask import jsonify

students_list = [
    {"id": 1, "student": "Jorgo Qirjaj"},
    {"id": 2, "student": "Anxhela Beluli"},
    {"id": 3, "student": "Flavia Hajna"}
]

class student_one(Resource):
    

    
    def put(self,student_id,name):   
        id_exist = False

        for a in students_list:
            if a["id"] == student_id:
                a.update({'name': name})
                id_exist = True
                return jsonify(a)

        if id_exist == False:
            students_list.append(dict({'id': student_id, 'name': name}))
            return jsonify(students_list)

        return jsonify(students_list)

def post(self,student_id,name):  

        id_exist = False
        for i in range(len(students_list)):
            if students_list[i-1]['id'] == student_id:
                id_exist = True
    
        if id_exist == False:
            students_list.append(dict({'id': student_id, 'name': name}))
            return jsonify(students_list)
        else:
            return "ID already exists."

    

class student_two(Resource):

    def get(self, student_id):  
        flag = False
        for student in students_list:
            if student["id"] == student_id:
                flag = True
                return jsonify(student)
        if flag == False:    
            return "ID does not exist."
       
    def delete(self, student_id):      
        flag = False
        for i in range(len(students_list)): 
            if students_list[i]['id'] == student_id: 
                del students_list[i]
                flag = True
                return "This student is  deleted."

        if flag == False:
            return "ID does not exist."

class all_students(Resource):
    def get(self):
        return jsonify(students_list)
