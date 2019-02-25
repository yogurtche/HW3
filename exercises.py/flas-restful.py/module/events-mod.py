from flask_restful import Resource
from flask import jsonify

events_list = [
    {"id": 1, "event": "International Week"},
    {"id": 2, "event": "Dance Crew Performance"},
    {"id": 3, "event": "Alumni Day"}
]

class event_one(Resource):
    

    
    def put(self,event_id,name):   #Put Method
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

def post(self,event_id,name):  #Post method

        id_exist = False
        for i in range(len(events_list)):
            if events_list[i-1]['id'] == event_id:
                id_exist = True
    
        if id_exist == False:
            events_list.append(dict({'id': event_id, 'name': name}))
            return jsonify(events_list)
        else:
            return "ID already exist"

    

class event_two(Resource):

    def get(self, event_id):  #Get Method
        flag = False
        for event in events_list:
            if event["id"] == event_id:
                flag = True
                return jsonify(event)
        if flag == False:    
            return "ID not Found!"
       
    def delete(self, event_id):      #Delete method
        flag = False
        for i in range(len(events_list)): 
            if events_list[i]['id'] == event_id: 
                del events_list[i]
                flag = True
                return "The event is  deleted!"

        if flag == False:
            return "ID was not found!"

class all_events(Resource):
    def get(self):
        return jsonify(events_list)
