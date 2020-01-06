from flask import request, jsonify
from app import app, model, socketio
from instance import config
import time
import json


@socketio.on('add_data')
def add_data(data):
    data = data.decode('utf-8')
    data = json.loads(data)
    print('received json: ' + str(json))
    model.add_data(data)

@app.route('/auth/<login>/<password>', methods=['GET'])
def auth (login, password):
    user_id = model.check_user(login)

    if user_id:
        is_valid = model.check_password(user_id, password)
        if is_valid:
            resp = jsonify(["OK"])
            resp.status_code = 200
        else:
            resp = jsonify({"Error": "Invalid password"})
            resp.status_code = 404
    else:
        resp = jsonify({"Error": "Unregistered"})
        resp.status_code = 404

    return resp

@app.route('/data/', methods=['GET'])
def send_data():
    print ("data request")
    #print ("params:", params)
    resp = jsonify({"it": "works!"})
    resp.status_code = 200
    return resp