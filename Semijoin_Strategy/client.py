import socket
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect((socket.gethostname(),1025))
client_msg=''
while True:
    msg=s.recv(1024)
    if(len(msg)==0):
        break
    print(msg.decode("utf-8"),end="\n")
