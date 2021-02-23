from flask import Flask,render_template,request,Response
import json,jsonify
import socket

HOST = '127.0.0.1'
PORT =  7777
BUF_SIZE = 128


app = Flask(__name__)


c_sock = socket(AF_INET,SOCK_STREAM)
c_sock.connect((HOST,PORT))

def send(sock):
	sendData = input('>>>') #임시로 테스트를 위해 클라이언트측에서 데이터를 콘솔로 입력하는 부분
	sock.send(sendData.encode('utf-8')) #서버에게 data를 보냄
	
def receive(sock):
	recvData = sock.recv(BUF_SIZE) #서버한테 data 받음
	print('Server: ',recvData.decode('utf-8')) #임시로 클라이언트측 콘솔에 대답을 띄움
	

while True: #클라이언트측 반복부분
  	send(connectionSock)
	  receive(connectionSock)





'''
#챗봇 서버와 통신
def get_answer(sentence):
  mySock = socket.socket()
  mySock.connect((HOST,PORT))
  mySock.send(sentence.encode())
  
  data = mySock.recv(BUF_SIZE).decode()
  ret_data = json.loads(data)
  
  mySock.close()
  
  return ret_data
  
 

#매직미러에게 메세지 받아 챗봇에게 전송하는 API
@app.route("/chatbot",methods=['POST']) 
def req1(): 
  data = request.json #받고
  sentence = data['sentence']
  ret = get_answer(sentence) #챗봇에게 전송하는 함수
  return jsonify(ret) #매직미러가 다시 받아 갈 부분
'''



if __name__ == '__main__':
  app.run(host='0.0.0.0',debug=True)
