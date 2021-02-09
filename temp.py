from flask import Flask,render_template,request,Response
#from socket import *
from flask_socketio import SocketIO
from flask_socketio import send, emit

HOST = '0.0.0.0'
PORT =  7777
BUF_SIZE = 128


app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)


'''
@app.route("/test",methods=['POST'])
def test():
  record = json.loads(request.data)
  new_records =[]
  with open('/tmp/data.txt','r') as f:
     data = f.read()
     records = json.loads(data)
  for r in records:
     if r['name'] == record['name']:
         r['email'] = record['email']
     new_records.append(r)
  with open('/tmp/data.txt','w') as f:
     f.write(json.dumps(new_records,indent=2))
  return jsonify(record)
'''

@app.route("/chatbot",methods=['POST']) 
def req1():
  data = request.json
  sentence = data['sentence']
  #print (sentence)
  return sentence

def messageReceived(methods=['POST']):
    print('message was received!!!')

@socketio.on('my event') #모델에게 메세지 보내기
def handle_my_custom_event(json, methods=['POST']):
    print('received my event: ' + str(json))
    socketio.emit(req1(), json, callback=messageReceived)


@app.route("/example")
def example():
  return render_template("example.html")


if __name__ == '__main__':
  socketio.run(app,debug=True)
