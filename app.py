from flask import Flask, render_template
from flask_socketio import SocketIO
import random

app = Flask(__name__)
socketio = SocketIO(app, cors_allowed_origins='*')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/create')
def create():
    return render_template('create.html')

@app.route('/join')
def join():
    return render_template('join.html')    

@socketio.on('create_code')
def create_code():
    code = generate_random_code()
    socketio.emit('code_created', {'code': code})

def generate_random_code():
    return random.randint(10000, 99999)

@app.route('/meet')
def meet():
    return render_template('meet.html')

@socketio.on('message')
def handle_message(data):
    socketio.emit('message', data)

if __name__ == '__main__':
    socketio.run(app, host='0.0.0.0', port=5000, use_reloader=True, debug=True)
