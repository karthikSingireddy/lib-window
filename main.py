from flask import Flask, render_template, request
from flask_socketio import SocketIO, send, emit

app = Flask(__name__)
socketio = SocketIO(app)

@app.route('/')
def first_page():
    socketio.emit('message', "test output")
    print('test emit')
    return "test response"

# @app.route('/response_page', methods = ['POST'])
# def response_page():
#     name = request.form['name']    
#     return render_template('response_page.html', name=name)

@app.route('/debug')
def debug():
    return render_template('log.html')

@socketio.on('message')
def socketHandleMessage(data):
    print('recieved from client' + data)
@socketio.on('connect')
def onConnect(data):
    print('client connected')
    print(data)



if __name__ == "__main__":
        port = int(os.environ.get("PORT", 5000))
        # app.run(host='0.0.0.0', port=port)
        socketio.run(app)
        #app.run()
print('LKSDJFLKSDJFLKSDJFLSKDJFLSDKJFSLDKJ')