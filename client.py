import json
import socketio
from urllib.request import urlopen
from time import sleep


sio = socketio.Client()

def send_ping():
    while True:
      data = urlopen('http://192.168.0.30:8081/api/state')
      data = json.dumps(data).encode('utf-8')
      sio.emit('add_data', data)
      sleep(3)

@sio.event

def connect():
    print('connected to server')
    send_ping()

if __name__ == '__main__':
  flag = 0
  while True:
    try:
      if flag==0:
        sio.connect('http://localhost:5000')
        flag=1

      else:
        send_ping()
    except socketio.Client-ConnectionError:
      print('Connection failed, try again.')
      sleep(3)