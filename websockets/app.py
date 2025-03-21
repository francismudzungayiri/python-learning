from flask import Flask
from flask_socketio import SocketIO, emit
import time
import threading


app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'  # Required for session management


#initialize socketio 
socketio = SocketIO(app)


@app.route('/')
def index():
    return ' Hello World'


#websocket event handler for client connection 
@socketio.on('connect')
def handle_connection():
    print('Client connected')
    #send a welcome message to the client
    emit('update', {'data':'Client connected'})
    

#function to trugger ui update
def update_ui():
    with app.app_context():
        #emit an update event to all connected clients
        socketio.emit('update',{'data':'UI updated automatically'})
        

# Background task to simulate real-time updates
def background_Task():
    while True:
        time.sleep(2) #wait for 2 seconds
        update_ui() # trigger th update function after 2 seconds
        print('ui updated')
    
    
# RUN THE BACKGROUND TASK  USING THREADS
thread = threading.Thread(target= background_Task)
thread.daemon = True  #daemonising the process makes the process when the main process stops
thread.start()
    




if __name__ == '__main__':
    socketio.run(app, debug=True)