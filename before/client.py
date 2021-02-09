from socket import *


HOST = '127.0.0.1'
PORT = 7777
BUF_SIZE = 1024

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
