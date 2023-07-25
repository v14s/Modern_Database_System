#from http import server
'''from http import server
import socket 

ip=socket.gethostbyname(socket.gethostname())
port=5566
adr=(ip,port)

def main():
    client=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    client.connect(adr)
    connected =True

    while connected:
        msg=client.recv(1024)
        if (len(msg)==0):
            break
        print()

if __name__=="__main__":
    main()'''

import socket
host = '127.0.0.1'
port = 1233

ClientSocket = socket.socket()
print('Waiting for connection')
try:
    ClientSocket.connect((host, port))
except socket.error as e:
    print(str(e))
Response = ClientSocket.recv(2048)
while True:
    Input = input('Your message: ')
    ClientSocket.send(str.encode(Input))
    Response = ClientSocket.recv(2048)
    print(Response.decode('utf-8'))
ClientSocket.close()
