from socket import *


HOST = '127.0.0.1'
PORT = 7777
BUF_SIZE = 1024

c_sock = socket(AF_INET,SOCK_STREAM)
c_sock.connect()

