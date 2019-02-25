from flask import Flask, request, jsonify

app = Flask(__name__, static_url_path='/static')



courses_list = [
    {"id": 1, "name": "MAT230"},
    {"id": 2, "name": "COS350"},
    {"id": 3, "name": "ENG330"}
]

# Retrieve of CRUD
def get_course(course_id):
    flag = False
    for course in courses_list:
        if course["id"] == course_id:
            flag = True
            return jsonify(course)
    if flag == False:    
        return "Could not find this ID"


def delete_course(course_id):  #delete method
    flag = False
    for i in range(len(courses_list)): 
        if courses_list[i]['id'] == course_id: 
            del courses_list[i]
            flag = True
            return "Course was deleted successfully!"

    if flag == False:
        return "ID not Found!"


def put_course(course_id, name):  #PUT method
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
           
def post_course(course_id, name): # Post method
    id_exist = False
    for i in range(len(courses_list)):
        if courses_list[i-1]['id'] == course_id:
            id_exist = True
    
    if id_exist == False:
        courses_list.append(dict({'id': course_id, 'name': name}))
        return jsonify(courses_list)
    else:
        return "ID already exist"
    
def get_courses(): #GET ALL
    return jsonify(courses_list)


# Route mapping methods.

@app.route('/')
def main():
    return "Hello World!"



@app.route('/v2/course/<int:course_id>', methods=["GET","DELETE"])
def course_crud_gd(course_id):
    if request.method == "GET":
        return get_course(course_id)
    else:
        return delete_course(course_id)
   


@app.route('/v2/course/<int:course_id>/<name>', methods=["POST","PUT"])
def course_crud_pp(course_id, name):
    if request.method == "POST":
        return post_course(course_id, name)
    else:
        return put_course(course_id, name)



@app.route('/v2/courses', methods=["GET"])
def course_retrieve():
return get_courses()