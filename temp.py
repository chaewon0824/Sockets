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
def req1(): #매직미러에게 메세지 받기
  data = request.json
  sentence = data['sentence']
  #print (sentence)
  return sentence

def messageSend(methods=['POST']):
    print('message is send!!!')

@socketio.on('my event') #모델에게 메세지 보내기
def handle_my_custom_event_send(req1(), methods=['POST']):
    socketio.emit("my response", req1(), callback=messageSend) 

@socketio.on('my event') #모델에게 메세지 받기
def handle_my_custom_event_receive(json, methods=['POST']):
    print('Model: ' + str(json))
    return json #여기서 매직미러가 답을 받아가길 원함...


    
@app.route("/example")
def example():
  return render_template("example.html")


if __name__ == '__main__':
  socketio.run(app,debug=True)
