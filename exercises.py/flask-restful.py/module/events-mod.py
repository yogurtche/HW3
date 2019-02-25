from flask_restful import Resource
from flask import jsonify

events_list = [
    {"id": 1, "event": "StartUp AUBG 2019"},
    {"id": 2, "event": "HAIR The Musical BPC"},
    {"id": 3, "event": "TEDxAUBG 2019"}
]

class event_one(Resource):
    

    
    def put(self,event_id,name):   
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

def post(self,event_id,name):  

        id_exist = False
        for i in range(len(events_list)):
            if events_list[i-1]['id'] == event_id:
                id_exist = True
    
        if id_exist == False:
            events_list.append(dict({'id': event_id, 'name': name}))
            return jsonify(events_list)
        else:
            return "ID already exists."

    

class event_two(Resource):

    def get(self, event_id):  
        flag = False
        for event in events_list:
            if event["id"] == event_id:
                flag = True
                return jsonify(event)
        if flag == False:    
            return "ID does not exist."
       
    def delete(self, event_id):    
        flag = False
        for i in range(len(events_list)): 
            if events_list[i]['id'] == event_id: 
                del events_list[i]
                flag = True
                return "This event is  deleted."

        if flag == False:
            return "ID does not exist."

class all_events(Resource):
    def get(self):
        return jsonify(events_list)
