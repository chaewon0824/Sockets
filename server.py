from socket import *


HOST = '127.0.0.1'
PORT =  7777
BUF_SIZE = 1024



serverSock = socket(AF_INET,SOCK_STREAM)
serverSock.bind((HOST,PORT))
serverSock.listen()

connectionSock, addr = serverSock.accept() #addr = Address Family
print(str(addr),'Success Connection\n')


def send(sock):
	sendData = input('>>>') #임시로 테스트를 위해 서버측에서 데이터를 콘솔로 입력하는 부분
	sock.send(sendData.encode()) #클라이언트에게 data를 보냄
	
def receive(sock):
	recvData = sock.recv(BUF_SIZE) #클라이언트한테 data 받음
	print('Client: ',recvData.decode('utf-8')) #임시로 서버측 콘솔에 대답을 띄움
	

while True: #서버측 반복부분
	receive(connectionSock)
	send(connectionSock)
	
	
