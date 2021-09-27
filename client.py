import socket
import threading
class Client:
       def  __init__(self):
	self.socket=socket.socket()
	self.socket.connect(('localhost',1200))
	self.l={"client":socket}
	name=input("Enter Name : ")
	socket.send(name.encode())
	password=input("Enter Password : ")
	socket.send(password.encode())
	print("Server Listning")
       def Send(self):
    	while True:
        	  msg = input()
        	  self.l['client'].send(msg.encode())
        	  if(msg==""):
            		self.socket.send("504exit".encode())
            		self.socket.close()
            		break
        	  print(f"\t\tYou : {msg}")
       def Recieve(self):
    	while True:
        		try:
            			msg = self.l['client'].recv(1024).decode()
            			print(f"{msg}")
        		except Exception as e:
            			print(e)
            			break
       def Start(self):
	t1=threading.Thread(target=self.Send)
	t2=threading.Thread(target=self.Recieve)
	t1.start()
	t2.start()
       def __del__(self):
	try:
		self.socket.close()
		del self.l
	except:
		pass
c1=Client()
c2=Client()
c3=Client()
