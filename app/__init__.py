from flask import Flask, jsonify, url_for
from flask_jsonrpc import JSONRPC
from instance import config
from flask_socketio import SocketIO
#from flask_cors import CORS


app = Flask(__name__, instance_relative_config=True)

#CORS(app)
#jsonrpc = JSONRPC(app, '/')

# config
app.config.from_pyfile('config.py') # default config
app.config.from_pyfile('config.py', silent=True) # local config
socketio = SocketIO(app)


from .views import *