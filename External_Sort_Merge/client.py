import socket

def client_program():
    host = socket.gethostname()  # as both code is running on same pc
    print(host)
    port = 5000  # socket server port number

    client_socket = socket.socket()  # instantiate
    client_socket.connect((host, port))  # connect to the server

    message = "hi"  # take input

    while message.lower().strip() != 'bye':
        # client_socket.send(message.encode())  # send message
        data = client_socket.recv(1024).decode() # receive response

        print('Received from server: \n' + data)  # show in terminal
        msg = input()
        # client_socket.send(msg.encode())

        data = eval(data)
        print(data)
        data.sort()
        data = str(data)
        print(data)
        client_socket.send(data.encode())
        msg = input()
        client_socket.send(data.encode())

    client_socket.close()  # close the connection

if __name__ == '__main__':
    client_program()
