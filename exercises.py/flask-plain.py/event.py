from flask import Flask, request, jsonify

app = Flask(__name__, static_url_path='/static')


events_list = [
    {"id": 1, "event": "StartUp AUBG 2019"},
    {"id": 2, "event": "HAIR The Musical BPC"},
    {"id": 3, "event": "TEDxAUBG 2019"}
]


def get_event(event_id):
    flag = False
    for event in events_list:
        if event["id"] == event_id:
            flag = True
            return jsonify(event)
    if flag == False:    
        return "Could not find this ID."

def delete_event(event_id):  
    flag = False
    for i in range(len(events_list)): 
        if events_list[i]['id'] == event_id: 
            del events_list[i]
            flag = True
            return "You deleted this event successfully."

    if flag == False:
        return "ID does not exist."

def put_event(event_id, name):  
    id_exist = False

    for a in events_list:
        if a["id"] == event_id:
            a.update({'name': name})
            id_exist = True
            return jsonify(a)

    if id_exist == False:
        events_list.append(dict({'id': event_id, 'name': name}))
        return jsonify(events_list)

    return jsonify(events_list)
           
def post_event(event_id, name): 
    id_exist = False
    for i in range(len(events_list)):
        if events_list[i-1]['id'] == event_id:
            id_exist = True
    
    if id_exist == False:
        events_list.append(dict({'id': event_id, 'name': name}))
        return jsonify(events_list)
    else:
        return "ID already exist"
    
def get_events(): 
    return jsonify(events_list)



@app.route('/')
def main():
    return "Hello world!"


@app.route('/v2/event/<int:event_id>', methods=["GET","DELETE"])
def event_crud_gd(event_id):
    if request.method == "GET":
        return get_event(event_id)
    else:
        return delete_event(event_id)
   

@app.route('/v2/event/<int:event_id>/<name>', methods=["POST","PUT"])
def event_crud_pp(event_id, name):
    if request.method == "POST":
        return post_event(event_id, name)
    else:
        return put_event(event_id, name)


@app.route('/v2/events', methods=["GET"])
def event_retrieve():
return get_events()