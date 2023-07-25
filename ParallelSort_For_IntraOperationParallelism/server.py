from http import server
from re import X
import socket
from _thread import *
import mysql.connector

host = '127.0.0.1'
port = 1233
ThreadCount = 0

conn=mysql.connector.connect(host='localhost',username='root',password='Vaishu@14',database='poe')
my_curr=conn.cursor()
try:
    my_curr.execute("select * from student1")
    result=my_curr.fetchall()
    print("Actual Table")
    for i in result:
        print(i)
    j=0;
except:
    conn.rollback()

def sort_function():
    pass
def client_handler(connection):
    connection.send(str.encode('You are now connected to the replay server... Type BYE to stop'))
    n=len(result)
    global j;
    arr1=[]
    arr2=[]
    arr3=[]
    for i in range(n):
        if(result[i][0]<6):
            arr1.append(result[i])
        elif(result[i][0]>=6 and result[i][0]<=10):
            arr2.append(result[i])
        else:
            arr3.append(result[i])
    if(j==0):
        for i in range(len(arr1)):
            str1=""
            for k in arr1[i]:
                str1+=str(k)+" "
            str1+='\n'
            connection.send(str.encode(str1))
    elif(j==1):
        for i in range(len(arr2)):
            str1=""
            for k in arr2[i]:
                str1+=str(k)+" "
            str1+='\n'
            connection.send(str.encode(str1))
    else:
        for i in range(len(arr3)):
            str1=""
            for k in arr3[i]:
                str1+=str(k)+" "
            str1+='\n'
            connection.send(str.encode(str1))
    j+=1
    while True:
        data = connection.recv(2048)
        message = data.decode('utf-8')
        if message == 'BYE':
            break
        reply = f'Server: {message}'
        connection.send(str.encode(str1))
    connection.close()

def accept_connections(ServerSocket):
    Client, address = ServerSocket.accept()
    print('Connected to: ' + address[0] + ':' + str(address[1]))
    start_new_thread(client_handler, (Client,))

def start_server(host, port):
    ServerSocket = socket.socket()
    try:
        ServerSocket.bind((host, port))
    except socket.error as e:
        print(str(e))
    print(f'Server is listing on the port {port}...')
    ServerSocket.listen()
    while True:
        accept_connections(ServerSocket)

start_server(host, port)
