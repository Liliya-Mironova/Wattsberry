from flask import Flask, render_template
from flask_socketio import SocketIO
import json
import flask
import psycopg2
import psycopg2.extras


app = Flask(__name__)
socketio = SocketIO(app)
connection = psycopg2.connect(
            database="solar", host="localhost",
            user="lmironov", password="1")
cursor = connection.cursor(cursor_factory=psycopg2.extras.DictCursor)

@socketio.on('add_data')
def handle_my_custom_event(data):
    data = data.decode('utf-8')
    data = json.loads(data)
    print('received json: ' + str(json))
    cursor.execute("INSERT INTO anna (val) VALUES(%s)", (str(data),))
    connection.commit()

@app.route('/auth/', methods=['POST'])
def auth (login, password):
    pw = {"log": "passw"}
    if login in pw:
        if pw["log"] == "passw":
            resp.status_code = 200
        else:
            resp = jsonify({"Error": "Invalid values"})
            resp.status_code = 404
    else:
        resp = jsonify({"Error": "Unregistered user"})
        resp.status_code = 404


if __name__ == '__main__':
   socketio.run(app, debug=True, host='127.0.0.1')