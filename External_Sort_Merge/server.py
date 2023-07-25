import socket
import os
from _thread import *
ServerSideSocket = socket.socket()
host = socket.gethostname()
port = 5000
ThreadCount = 0

received_data = [[3,2,1],[5,4,6],[]]
def merge(a,b):
    x = a+b
    return x
try:
    ServerSideSocket.bind((host, port))
except socket.error as e:
    print(str(e))
print('Socket is listening..')
ServerSideSocket.listen(2)
def multi_threaded_client(connection,info):
    # connection.send(str.encode('Server is working:'))
    st = str(info)
    connection.sendall(str.encode(st))
    while True:
        data = connection.recv(2048)
        response = data.decode('utf-8')
        if not data:
            break
        print("sent data to client : ",info)
        print("client response : ",response)
        received_data.append(eval(response))
        
        
    connection.close()
received_data = []
while True:
    Client, address = ServerSideSocket.accept()
    print('Connected to: ' + address[0] + ':' + str(address[1]))
    
    test = [[3,2,1],[5,4,6],[]]
    data1 = test[ThreadCount]
    
        
    # data1 = []
    # for row in range(ThreadCount*20,ThreadCount*20+20):
    #     data1.append(table[row])
    # data1 = str(data1)
    # data1 += str(table[0]) + "\n"
    # for row in table:
    #     data1 += str(row[ThreadCount*5:ThreadCount*5+5]) + "\n"

    start_new_thread(multi_threaded_client, (Client, data1))

    ThreadCount += 1
    print('Thread Number: ' + str(ThreadCount))
    if ThreadCount == 3:
        break
# print(received_data)
print(merge(received_data[0],received_data[1]))
ServerSideSocket.close()
