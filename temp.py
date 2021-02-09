from flask import Flask,render_template,request,Response
from socket import *
import time

HOST = '0.0.0.0'
PORT =  7777
BUF_SIZE = 128

s_Sock = None
#s_Sock = socket(AF_INET,SOCK_STREAM)
#s_Sock.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
#print("bind")
#s_Sock.bind((HOST,PORT))
#s_Sock.listen()
#connectionSock, addr = s_Sock.accept()
#print(str(addr),'Success Connection\n') #Adress Family = addr


#c_sock = socket(AF_INET, SOCK_STREAM)
#c_sock.connect((HOST,PORT))
#me=c_sock.send("me?".encode('utf-8'))

app = Flask(__name__)
app.debug = True


'''
def send(sendData):
	#sendData = input('>>>') #임시로 테스트를 위해 서버측에서 데이터를 콘솔로 입력하는 부분
	print("sibal")
	c_sock.send(sendData.encode('utf-8')) #모델에게 data를 보냄

def receive():
	recvData = c_sock.recv(BUF_SIZE) #모델한테 data 받음
	return recvData
	#print('Model: ',recvData.decode('utf-8')) #임시로 서버측 콘솔에 대답을 띄움


while True: #서버측 반복부분
	send(connectionSock)
	receive(connectionSock)
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


@app.route("/chatbot",methods=['POST'])
def req1():
  data = request.json
  send_sentence = data['sentence']
  print (send_sentence)
  c_sock = socket(AF_INET, SOCK_STREAM)
  c_sock.connect((HOST,PORT))
  c_sock.send(send_sentence.encode('utf-8'))
  sentence = c_sock.recv(BUF_SIZE)
  time.sleep(3)
  print (sentence)
  return sentence



@app.route("/example")
def example():
  return render_template("example.html")

if __name__ == '__main__':
  app.run(host='0.0.0.0')
