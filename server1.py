import threading
import socket
import time
socket=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
socket.bind(('localhost',1200))
socket.listen()
print("Server Listning")
clients={}
def ProcessClose():
    global socket,clients
    while True:
        a=input("Enter server exit : ")
        print(a)
        if(a.lower()=="exit"):
            for item in clients.values():
                item[0].close()
            socket.close()
            break
def mysend(socket,msg,password):
    global clients
    if(len(clients)!=0):
        a=""
        for item in clients:
            if(password==clients[item][2]):
                a+=(f" {item} ,")
        if(a!=""):
            a=a[:-1]
            a+=f" {msg}"
            socket.send(a.encode())
def send(socket,id,msg):
    global clients
    for item in clients:
        if(item==id):
            continue
        elif(clients[id][2]==clients[item][2]):
            clients[item][0].send(msg)
def Receive(socket):
    global clients
    while True:
        try:
            msg=clients[threading.currentThread().getName()][0].recv(1024)
            if(msg.decode()=="504exit"):
                send(socket,threading.currentThread().getName(),f"{threading.currentThread().getName()} is left chat at {time.asctime(time.localtime(time.time()))}".encode())
                clients.pop(threading.currentThread().getName())
                break
            msg=f"{threading.currentThread().getName()} : {msg.decode()}".encode()
            send(socket,threading.currentThread().getName(),msg)
        except Exception as e:
            print(e)
            break
def Connection():
    global clients,Receive,socket
    while True:
        try:
            client,address=socket.accept()
            id=client.recv(1024).decode()
            password=client.recv(1024).decode()
            mysend(client,"In Meeting",password)
            clients[str(id)]=[client,threading.Thread(target=Receive,name=str(id),args=(socket,)),password]
            clients[str(id)][1].start()
            send(socket,id,f"{id} is join chat at {time.asctime(time.localtime(time.time()))}".encode())
        except Exception as e:
            print(e)
            break
t1=threading.Thread(target=Connection)
t2=threading.Thread(target=ProcessClose)
t1.start()
t2.start()
