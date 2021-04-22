#from tkinter import *
import tkinter as tk
from socket import *
from p2p_chat_session_v2 import *

cent_port = input("[?] Enter Central Port Number: ")
root = tk.Tk()
root.geometry("600x600")  # SIZE OF APP WINDOW
root.title("CHAT APP")    # TITLE OF APP WINDOW
root.configure(bg="white")  # changes the background color
session = p2p_chat_session(int(cent_port))

def disp_msg(session):
    while(session.active == True):
      while(session.message_list != []):
        disp_box.insert(tk.INSERT, session.message_list.pop())

def send():                                                   # send function defined here
    retrieveinput = send_box.get("1.0", tk.END)
    send_box.delete("1.0", tk.END)
    session.send_str(retrieveinput)


def connect():  # this is the function that will execute when the connect button is pressed
    # DELETE EVERYTHING AFTER THE PORTVALUE  AND ADD THE CODE TO CONNECT,

    # when the connect button is pressed the IP and port numbers will be stored in IPValue and PORTValue
    IPValue = ip_box.get("1.0", "end-1c")  # STORES THE IP VALUE
    port_value = port_box.get("1.0", "end-1c")  # STORES THE PORT VALUE

    ip_box.delete("1.0",tk.END)
    port_box.delete("1.0",tk.END)

    retrieve_input2 = port_box.get("1.0", tk.END)
    disp_box.insert(tk.INSERT, retrieve_input2)
    

    session.requ_p2p(gethostname(), int(port_value))

    # this is the function that will execute when the disconnect button is pressed
def disconnect():
    # DELETE EVERYTHING WITHIN THIS FUNCTION AND ADD THE CODE TO DISCONNECT
    retrieveinput = send_box.get("1.0", tk.END)
    disp_box.insert(tk.INSERT, retrieveinput)
    send_box.delete("1.0", tk.END)
    session.close_ses()


frame = tk.Frame(root, bg="white")
frame.pack(side=tk.LEFT, anchor=tk.NW)

frame1 = tk.Frame(root, bg="white")
frame1.pack(side=tk.LEFT, anchor=tk.N)


# BUTTON DEFINITIONS BELOW

btn = tk.Button(root, text=" Send ", fg="green", bg="white", command=send)
btn.pack(side=tk.RIGHT, anchor=tk.SW)
#btn.pack(side = tk.RIGHT, fill = tk.Y)
#btn.bind("<Return>", send)

ip_box = tk.Text(frame1, height=1, width=14)
ip_box.pack(side=tk.TOP, anchor=tk.N)

port_box = tk.Text(frame1, height=1, width=10)
port_box.pack(side=tk.TOP, anchor=tk.N)

discon_btn = tk.Button(frame1, text="  Disconnect    ",
                          fg="red", bg="white", command=disconnect)
discon_btn.pack(side=tk.BOTTOM)
#discon_btn.pack(side = tk.TOP, fill = tk.Y)

con_btn = tk.Button(frame1, text="     Connect     ",
                       fg="blue", bg="white", command=connect)
con_btn.pack(side=tk.BOTTOM)
#con_btn.pack(side = tk.TOP, fill = tk.Y)

ip_label = tk.Label(frame, text="IP", fg="green", bg="white")
ip_label.pack(side=tk.TOP, anchor=tk.NW)

port_label = tk.Label(frame, text="PORT", fg="green", bg="white")
port_label.pack(side=tk.BOTTOM, anchor=tk.NW)


# this defines the box where text is displayed
disp_box = tk.Text((root), height=15, width=100)
disp_box.pack(side=tk.TOP)

# this defnes the box where the users type
send_box = tk.Text((root), height=4, width=100)
send_box.pack(side=tk.BOTTOM)

disp = Thread(target=disp_msg,args=(session,),daemon=True)
disp.start()

root.mainloop()
