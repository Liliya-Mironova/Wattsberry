from app import app, socketio
from instance import config


if __name__ == "__main__":
	#app.run()
    socketio.run(app, debug=True, host=config.SERVER_HOST, port=config.SERVER_PORT)