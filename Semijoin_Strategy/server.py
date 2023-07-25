import mysql.connector
import socket
conn=mysql.connector.connect(host='localhost',username='root',password='Vaishu@14',database='poe')
my_curr=conn.cursor()
#create sockets using socket method
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.bind((socket.gethostname(),1025))
s.listen(1024)
while True:
    try:
        my_curr.execute("select * from department")
        result1=my_curr.fetchall()
        my_curr.execute("select * from customer")
        result2=my_curr.fetchall()
        sol=[]
        for x in result2:
            if(x[3] is not None):
                for v in result1:
                    if(x[3]==v[0]):
                        str1=str(v[0])+" "+str(v[1])
                        sol.append(str1)
                        break
    except:
        conn.rollback()
    clt,adr=s.accept()
    print(f"connection to {adr} established ")
    for x in sol:
        '''str1=''
        for i in x:
            str1+=str(i)+" "
        clt.send(bytes(str1,"utf-8"))'''
        clt.send(bytes(x,"utf-8"));
        print(x)
    clt.close()
