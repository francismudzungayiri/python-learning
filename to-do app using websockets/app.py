from flask import Flask,render_template, redirect,url_for
from pymongo import MongoClient
from forms import ToDoForm
from flask_socketio import SocketIO, emit


app = Flask(__name__)#initialize flask app
app.config['SECRET_KEY'] = 'dklzknvnzdjklvnjsnkjlnsd'
socket = SocketIO(app) #initialize fsocket app


#set up the mongodb conection
client = MongoClient('localhost', 27017) 
db = client['To-Do-App'] 
tasks = db['tasks'] 




@app.route('/', methods = ['POST', 'GET'])
def index():
    form = ToDoForm()
    all_tasks = list(tasks.find())        
    return render_template('index.html', form = form, all_todos=all_tasks)



# WebSocket event handler for adding a task






# @app.route('/add', methods=['POST'])
# def addTask():
#     form = ToDoForm()
#     if form.validate_on_submit():
#         task = form.todo.data
        
#         data={'task':task}
#         tasks.insert_one(data)
#         print('Data posted')
#         return redirect(url_for('index'))




## WebSocket event handler for client connection
@socket.on('conect')
def handleConnection():
    print('CONNECTION ESTABLISHED')
    # Fetch all tasks from MongoDB and send them to the client
    todos = list(tasks.find())
    emit('tasksy', todos)




if __name__ == '__main__':
    socket.run(app,debug=True)