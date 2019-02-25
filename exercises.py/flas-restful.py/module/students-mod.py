from flask_restful import Resource
from flask import jsonify

students_list = [
    {"id": 1, "student": "Iris Dyrmishi"},
    {"id": 2, "student": "Ilda Duka"},
    {"id": 3, "student": "Fatme Tsiko"}
]

class student_one(Resource):
    

    
    def put(self,student_id,name):   #Put Method
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

def post(self,student_id,name):  #Post method

        id_exist = False
        for i in range(len(students_list)):
            if students_list[i-1]['id'] == student_id:
                id_exist = True
    
        if id_exist == False:
            students_list.append(dict({'id': student_id, 'name': name}))
            return jsonify(students_list)
        else:
            return "ID already exist"

    

class student_two(Resource):

    def get(self, student_id):  #Get Method
        flag = False
        for student in students_list:
            if student["id"] == student_id:
                flag = True
                return jsonify(student)
        if flag == False:    
            return "ID not Found!"
       
    def delete(self, student_id):      #Delete method
        flag = False
        for i in range(len(students_list)): 
            if students_list[i]['id'] == student_id: 
                del students_list[i]
                flag = True
                return "The student is  deleted!"

        if flag == False:
            return "ID was not found!"

class all_students(Resource):
    def get(self):
        return jsonify(students_list)
