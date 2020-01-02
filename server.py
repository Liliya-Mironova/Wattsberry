from flask import Flask, render_template, jsonify
from flask_socketio import SocketIO
import json
import flask
import psycopg2
import psycopg2.extras


app = Flask(__name__)
socketio = SocketIO(app)
connection = psycopg2.connect(
            database="solar", host="localhost",
            user="liliya", password=" ")
cursor = connection.cursor(cursor_factory=psycopg2.extras.DictCursor)

@socketio.on('add_data')
def add_data(data):
    data = data.decode('utf-8')
    data = json.loads(data)
    print('received json: ' + str(json))
    cursor.execute("INSERT INTO tmp_table (val) VALUES(%s)", (str(data),))
    connection.commit()

@app.route('/auth/<login>/<password>', methods=['GET'])
def auth (login, password):
    pw = {"log": "passw"}
    resp = None

    if login in pw:
        if pw["log"] == password:
            resp = jsonify(["OK"])
            resp.status_code = 200
        else:
            resp = jsonify({"Error": "Invalid password"})
            resp.status_code = 404
    else:
        resp = jsonify({"Error": "Unregistered user"})
        resp.status_code = 404

    return resp

@app.route('/data/', methods=['GET'])
def send_data():
    print ("data request")
    #print ("params:", params)
    resp = jsonify({"it": "works!"})
    resp.status_code = 200
    return resp


if __name__ == '__main__':
   socketio.run(app, debug=True, host='127.0.0.1')