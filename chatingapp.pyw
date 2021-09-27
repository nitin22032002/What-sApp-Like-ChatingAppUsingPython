from tkinter import *
from PIL import Image,ImageTk
import socket
import time
import threading
root1=Tk()
root1.title("Chating App")
root1.geometry("600x300")
root1.maxsize(600,300)
root1.minsize(600,300)
frame=Image.open("chatingapp.png")
frame=ImageTk.PhotoImage(frame)
root1.wm_iconphoto(False,frame)
username=""
userpassword=""
def start():
    global username,userpassword
    username=name.get()
    userpassword=password.get()
    if(username!="" and userpassword!=""):
        root1.destroy()
    else:
       a=Label(text="Please Fill Name and Password")
       a.place(x=10,y=150)
name=StringVar()
lable1=Label(root1,text="Enter Name ",font=("algerian",15,"bold"))
lable1.place(x=10,y=10)
entry1=Entry(root1,textvariable=name,font=("algerian",20,"bold"))
entry1.place(x=200,y=10)
password=StringVar()
lable2=Label(root1,text="Enter Password ",font=("algerian",15,"bold"))
lable2.place(x=10,y=100)
entry2=Entry(root1,textvariable=password,show="*",font=("algerian",20,"bold"))
entry2.place(x=200,y=100)
button=Button(root1,text="Start Chating",command=start,borderwidth=10,font="algerian 13 bold")
button.place(x=20,y=200)
root1.mainloop()
if(username!="" and userpassword!=""):
    dis=100
    disx=10
    def Send(socket):
            global l,dis,disx
            msg=msgsend.get()
            if (msg == "end"):
                socket.send("504exit".encode())
                socket.close()
            else:
                l['client'].send(msg.encode())
                Label(text=f"You : {msg}",font="algerian 13 bold").place(x=disx+190,y=dis)
                dis+=30
                if(dis>650):
                    dis=dis%650
                    disx=disx+220
    def Recieve(socket):
        global dis,disx
        while True:
            try:
                msg = l['client'].recv(1024).decode()
                Label(text=f"{msg}",font="algerian 13 bold").place(x=disx,y=dis)
                dis+=30
                if (dis > 650):
                    dis = dis % 650
                    disx=disx+220
            except Exception as e:
                print(e)
                break
    # socket.close()
    root = Tk()
    frame=Image.open("chatingapp.png")
    frame=ImageTk.PhotoImage(frame)
    root.wm_iconphoto(False,frame)
    root.title(f"{username} Chating App")
    root.geometry("600x500")
    msgsend=StringVar()
    def main():
        def sendnow():
            global socket
            Send(socket)
            msgsend.set("")
        field=Entry(root,textvariable=msgsend,font=("algerian",30,"bold"))
        field.place(x=10,y=10)
        button=Button(root,text="Send",command=sendnow,borderwidth=10,font="algerian 13 bold")
        button.place(x=520,y=10)
    try:
        socket = socket.socket()
        socket.connect(('localhost', 1200))
        l = {"client": socket}
        socket.send(username.encode())
        time.sleep(1)
        socket.send(userpassword.encode())
        print("Server Listning")
        t1 = threading.Thread(target=main)
        t2 = threading.Thread(target=Recieve, args=(socket,))
        t2.start()
        t1.start()
        root.mainloop()
        try:
            socket.send("504exit".encode())
            socket.close()
        except Exception as e:
            print(e)
    except Exception as e:
        root.destroy()
        print(e)

