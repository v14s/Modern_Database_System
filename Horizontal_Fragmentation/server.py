#from http import server
'''import socket 
import threading

ip=socket.gethostbyname(socket.gethostname())
port=5566
adr=(ip,port)

def handle_client(clt,addr):
    print(f"connection to {adr} established and id is {clt}")
    connected=True
    while connected:
        clt.send("executed or connected sucessfully ","utf-8")
        clt.close()

def main():
    print("server is starting ")
    server=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    server.bind(adr)
    server.listen()
    print("server is listening on "+str(ip)+str(port))
    while True:
        clt,addr=server.accept()
        thread=threading.start_new_thread(target=handle_client,args=(clt,addr))
        #thread.start()
        #print("active connections"+threading.activeCount()-1)

if __name__=="__main__":
    main()'''

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
    my_curr.execute("select * from student")
    result=my_curr.fetchall()
    m=len(result)//2
    j=0
except:
    conn.rollback()

def client_handler(connection):
    connection.send(str.encode('You are now connected to the replay server... Type BYE to stop'))
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
