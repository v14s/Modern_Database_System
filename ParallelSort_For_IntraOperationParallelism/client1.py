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
arr1=[]
while True:
    Input = input('Your message: ')
    ClientSocket.send(str.encode(Input))
    Response = ClientSocket.recv(2048)
    arr1.append(Response.decode('utf-8'))
    sol=arr1[0].split('\n')
    s=[]
    for i in range(len(sol)-1):
        val=sol[i].split(' ')
        s.append(float(val[3]))
    s.sort(reverse=True)
    sorted_arr=[]
    for j in range(len(s)):
        for i in range(len(sol)-1):
            val=sol[i].split(' ')
            if(s[j]==float(val[3])):
                sorted_arr.append(sol[i])
    for i in sorted_arr:
        print(i)
ClientSocket.close()
