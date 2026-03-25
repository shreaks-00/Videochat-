from flask import Flask, render_template
from flask_socketio import SocketIO, emit, join_room

app = Flask(__name__)
socketio = SocketIO(app, cors_allowed_origins="*")

@app.route('/')
def index():
    return render_template('index.html')

@socketio.on('join')
def on_join(data):
    room = data['room']
    join_room(room)
    emit('ready', room=room, skip_sid=True)

@socketio.on('data')
def transfer_data(data):
    # This passes video 'handshake' data between users
    room = data['room']
    emit('data', data, room=room, skip_sid=True)

if __name__ == '__main__':
    socketio.run(app, debug=True)
