from http import client
from re import X
import socket
from _thread import *
import mysql.connector
import time

host = '127.0.0.1'
port = 1233
cnt=0

conn=mysql.connector.connect(host='localhost',username='root',password='Vaishu@14',database='sort')
my_curr=conn.cursor()
def databaseupdate():
    try:
        my_curr.execute("select * from cust")
        '''result=my_curr.fetchall()
        for i in range(len(result)):
            result[i][2]+=500'''
        conn.commit()
        sql="update cust set amount = `amount+500`  where c_id=1 "
        my_curr.execute(sql)
        conn.commit()
    except:
        conn.rollback()

buffer=[]
buffer2=[]
def call():
    if(len(buffer)==len(buffer2)):
        if(all(buffer2)):
            for j in range(len(buffer)):
                databaseupdate()
                buffer[j].send(str.encode("commit"))
        else:
            for j in range(len(buffer)):
                buffer[j].send(str.encode("Abort"))
    

def client_handler(connection):
    '''connection.send(str.encode('You are now connected to the replay server... Type BYE to stop'))
    str1=''
    global j
    global m
    for k in range(j,j+m):
        for i in result[k]:
            str1+=str(i)+' '
        str1+='\n'
    j=m

    while True:
        data = connection.recv(2048)
        message = data.decode('utf-8')
        if message == 'BYE':
            break
        reply = f'Server: {message}'
        connection.send(str.encode(str1))
    connection.close()'''
    while True:
        reply=connection.recv(2048)
        reply=reply.decode('utf-8')
        if(reply=='Ready'):
            buffer2.append(1)
        else:
            buffer2.append(0)
        time.sleep(5)
        call()
        
    connection.close()

def accept_connections(ServerSocket):
    Client, address = ServerSocket.accept()
    print('Connected to: ' + address[0] + ':' + str(address[1]))
    buffer.append(Client)
    Client.send(str.encode("Prepare"))
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
