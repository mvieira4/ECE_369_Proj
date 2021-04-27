from time import sleep
import tkinter as tk
from socket import *
from threading import *
from p2p_chat_session_v2 import p2p_chat_session

# Gets message list from 
def disp_msg(session):
    while(session.active == True):
        while(session.message_list != []):
            disp_box.insert(tk.INSERT, session.message_list.pop())
        sleep(0.5)

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

    session.requ_p2p(gethostname(), int(port_value))

    # this is the function that will execute when the disconnect button is pressed
def disconnect():
    ip_box.delete("1.0",tk.END)
    port_box.delete("1.0",tk.END)

    session.discon_all()

cent_port = input("[?] Enter Central Port Number: ")
root = tk.Tk()
root.geometry("600x600")  # SIZE OF APP WINDOW
root.title("CHAT APP")    # TITLE OF APP WINDOW
root.configure(bg="white")  # changes the background color
session = p2p_chat_session(int(cent_port))

frame = tk.Frame(root, bg="white")
frame.pack(side=tk.LEFT, anchor=tk.NW)

frame1 = tk.Frame(root, bg="white")
frame1.pack(side=tk.LEFT, anchor=tk.N)

# Defines ip label
ip_label = tk.Label(frame, text="IP", fg="green", bg="white")
ip_label.pack(side=tk.TOP, anchor=tk.NW)

# Defines port label
port_label = tk.Label(frame, text="PORT", fg="green", bg="white")
port_label.pack(side=tk.BOTTOM, anchor=tk.NW)

# Defines send button
send_btn = tk.Button(root, text=" Send ", fg="green", bg="white", command=send)
send_btn.pack(side=tk.RIGHT, anchor=tk.SW)

#  Defines disconnect button
discon_btn = tk.Button(frame1, text="  Disconnect    ", fg="red", bg="white", command=disconnect)
discon_btn.pack(side=tk.BOTTOM)

# Defines connection button
con_btn = tk.Button(frame1, text="     Connect     ", fg="blue", bg="white", command=connect)
con_btn.pack(side=tk.BOTTOM)

# Defines the box where the users type ip
ip_box = tk.Text(frame1, height=1, width=14)
ip_box.pack(side=tk.TOP, anchor=tk.N)

# Defines the box where the users type port
port_box = tk.Text(frame1, height=1, width=10)
port_box.pack(side=tk.TOP, anchor=tk.N)

# Defines the box where text is displayed
disp_box = tk.Text((root), height=15, width=100)
disp_box.pack(side=tk.TOP)

# Defines the box where the users type messages
send_box = tk.Text((root), height=4, width=100)
send_box.pack(side=tk.BOTTOM)

# Starts displaying messages
disp = Thread(target=disp_msg,args=(session,),daemon=True)
disp.start()

root.mainloop()

session.close_ses()
