import os,sys
from tabnanny import check
import tkinter as ui
from tkinter import messagebox as mb
import subprocess as sp
import http.server
import socketserver
import socket
from turtle import color


alive="Server is running..."
dead="Server is stopped..."
server=dead
checkstatus="Waiting..."
runOnce=False
CREATE_NO_WINDOW = 0x08000000
handler = http.server.SimpleHTTPRequestHandler
hostname = socket.gethostname()
local_ip = socket.gethostbyname(hostname)


def start():
    global server,poll,runOnce
    if runOnce==False:
        try:
            PORT= int(giris_port.get())
            if PORT <= 0 or PORT > 65535:
                    mb.showerror(title="ERROR", message="Port must be between 1-65535")
                    return
            server=sp.Popen(args=[f"python","-m","http.server",f"{PORT}"],creationflags=CREATE_NO_WINDOW, stdout=sp.PIPE,stderr=sp.STDOUT)
            poll=server.poll()
            runOnce=True
        except:
            mb.showerror(title="ERROR", message="Port must be between 1-65535")


def terminate():
    global runOnce
    if runOnce==True:
        runOnce=False
        server.terminate()
        stat.configure(text=dead,bg="black",fg="red")


def status():
    global runOnce
    if runOnce==True:
        if poll is None:    #process still alive
            stat.configure(text=alive,bg="black",fg="green")
    window.after(3000,status)


def guide():
    GuideWindow = ui.Toplevel(window)
    GuideWindow.geometry("500x150")
    GuideWindow.resizable(0,0)
    GuideExample = ui.Label(GuideWindow, text = "This is a beginner's guide", font = ("Arial", 14), fg = "purple")
    GuideExample.pack()
    guid = ui.Text(GuideWindow)
    GuideExample.pack()
    guid.pack()
    guid.insert(ui.END,"1. Move this program to folder where you want to start server\n")
    guid.insert(ui.END,"2. To start type server's port number and click Start\n")
    guid.insert(ui.END,"3. If you want to stop the server, click Stop\n")
    guid.insert(ui.END,"4. If you want to donate, click Donate\n\n")
    guid.insert(ui.END,"     @@@ Thanks for reading, hope it helpful with you @@@")
    guid.configure(state='disabled')
  
    
def donate():
    newWindow = ui.Toplevel(window)
    newWindow.geometry("410x150")
    newWindow.resizable(0,0)
    labelExample = ui.Label(newWindow, text = "Thank you so much, @Dr1801", font = ("Arial", 14), fg = "red")
    labelExample.pack()
    donatee = ui.Text(newWindow)
    labelExample.pack()
    donatee.pack()
    donatee.insert(ui.END,"Support me at: https://www.buymeacoffee.com/Dr1801")
    donatee.insert(ui.END,"\n\n        Feedback at: mq18011210@gmail.com")
    donatee.insert(ui.END,"\n       Hope you enjoy this simply software!")
    donatee.configure(state='disabled')

    
if __name__ == '__main__':
    window=ui.Tk()
    window.title("Simple HTTP Server")
    window.geometry("420x150")
    window.resizable(0,0)
    window.configure(bg="black")
    
    ui.Label(window,text="             Your server IP : ",bg="black",fg="red").grid(row=0,column=4)
    ui.Label(window,text=str(local_ip),bg="black",fg="white").grid(row=0,column=5)
    
    ui.Label(window,text="                Your server Port : ",bg="black",fg="cyan").grid(row=1,column=4)
    giris_port = ui.Entry(window)
    giris_port.grid(row=1, column=5)
    
    button1=ui.Button(text="Start",width=20,height=1,bg="green",fg="white",command=start)
    button1.grid(row=3,column=4)
    button1.place(x=320,y=70,anchor="center")
    
    button2=ui.Button(text="Stop",width=20,height=1,bg="red",fg="white",command=terminate)
    button2.grid(row=3,column=2)
    button2.place(x=100,y=70,anchor="center")
    
    button3=ui.Button(text="Donate",width=7,height=1,bg="orange",fg="white",command=donate)
    button3.grid(row=5,column=3)
    button3.place(x=210,y=70,anchor="center")
    
    button4=ui.Button(text="Guide",width=7,height=1,bg="gray",fg="white",command=guide)
    button4.grid(row=5,column=3)
    button4.place(x=210,y=105,anchor="center")
    
    stat=ui.Label(window,text=checkstatus,bg="black",fg="yellow")
    stat.grid(row=2,column=0)
    stat.place(x=210,y=130,anchor="center")
    
    window.after(3000,status)
    window.mainloop()
    
    
