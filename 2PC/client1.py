import socket
import time
host = '127.0.0.1'
port = 1233

ClientSocket = socket.socket()
print('Waiting for connection')
try:
    ClientSocket.connect((host, port))
except socket.error as e:
    print(str(e))

while True:
    Response = ClientSocket.recv(2048)
    print(Response.decode('utf-8'))
    Input = input('Your message: ')
    ClientSocket.send(str.encode(Input))
    time.sleep(10)
ClientSocket.close()
