from flask import Flask,render_template,request,Response
import json,jsonify
import socket

HOST = '127.0.0.1'
PORT =  7777
BUF_SIZE = 128


app = Flask(__name__)

#챗봇 서버와 통신
def get_answer(sentence):
  mySock = socket.socket()
  mySock.connect((HOST,PORT))
  mySock.send(sentence.encode())
  
  data = mySock.recv(BUF_SIZE).decode()
  ret_data = json.loads(data)
  
  mySock.close()
  
  return ret_data
  
  
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

#매직미러에게 메세지 받아 챗봇에게 전송하는 API
@app.route("/chatbot",methods=['POST']) 
def req1(): 
  data = request.json #받고
  sentence = data['sentence']
  ret = get_answer(sentence) #챗봇에게 전송하는 함수
  return jsonify(ret) #매직미러가 다시 받아 갈 부분

   
@app.route("/example")
def example():
  return render_template("example.html")


if __name__ == '__main__':
  app.run(host='0.0.0.0',debug=True)
