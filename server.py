import socket
socket=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
socket.bind(('localhost',1200))
clients={}
socket.listen()
print("Server Listning")
client, address = socket.accept()
while True:
    client.send("Upload Your File ".encode())
    msg=client.recv(1024*1024*1024)
    if(msg.decode()==""):break
    elif(msg.decode()!="Error"):
        name = client.recv(1024).decode()
        with open(f"{name}","wb") as f:
            f.write(msg)
            f.close()
        client.send("File Uploaded on server".encode())
client.close()
socket.close()
