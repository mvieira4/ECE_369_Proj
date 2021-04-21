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


# lbl = Label(root, text="Hello")

# lbl.pack(side = LEFT)
# w = Label(root, text ='GeeksForGeeks',
# font = "50")

# w.pack()


# mylist = Listbox(root,
# yscrollcommand = scroll_bar.set )

# for line in range(1, 26):
#mylist.insert(END, "Geeks " + str(line))

#mylist.pack( side = LEFT, fill = BOTH )

#scroll_bar.config( command = mylist.yview )
# T = StringVar()


#T1 = Text((root) ,height = 18, width=100)
#T1.pack(side = TOP)

def disp_msg(session):
    while(session.active == True):
      while(session.message_list != []):
        T1.insert(tk.INSERT, session.message_list.pop())

def clicked():                                                   # clicked function defined here
  # T1 = tk.Text((root) ,height = 18, width=100)
    #T1.pack(side = tk.TOP)
    # should retrieve the text entered by user
    retrieveinput = T.get("1.0", tk.END)
    T1.insert(tk.INSERT, retrieveinput)

    # clears the text entry box after each sent message
  # print(T.get("1.0",'end-1c'))
    session.send_str(retrieveinput)


def connect():  # this is the function that will execute when the connect button is pressed
    # DELETE EVERYTHING AFTER THE PORTVALUE  AND ADD THE CODE TO CONNECT,

    # when the connect button is pressed the IP and port numbers will be stored in IPValue and PORTValue
    IPValue = IPBox.get("1.0", "end-1c")  # STORES THE IP VALUE
    PORTValue = PortBox.get("1.0", "end-1c")  # STORES THE PORT VALUE

    retrieveinput2 = PortBox.get("1.0", tk.END)
    T1.insert(tk.INSERT, retrieveinput2)
    T.delete("1.0", tk.END)

    session.requ_p2p(gethostname(), int(PORTValue))

    # this is the function that will execute when the disconnect button is pressed
def disconnect():
    # DELETE EVERYTHING WITHIN THIS FUNCTION AND ADD THE CODE TO DISCONNECT
    retrieveinput = T.get("1.0", tk.END)
    T1.insert(tk.INSERT, retrieveinput)
    T.delete("1.0", tk.END)
    session.close_ses()


frame = tk.Frame(root, bg="white")
frame.pack(side=tk.LEFT, anchor=tk.NW)

frame1 = tk.Frame(root, bg="white")
frame1.pack(side=tk.LEFT, anchor=tk.N)


# BUTTON DEFINITIONS BELOW

btn = tk.Button(root, text=" Send ", fg="green", bg="white", command=clicked)
btn.pack(side=tk.RIGHT, anchor=tk.SW)
#btn.pack(side = tk.RIGHT, fill = tk.Y)
#btn.bind("<Return>", clicked)

IPBox = tk.Text(frame1, height=1, width=14)
IPBox.pack(side=tk.TOP, anchor=tk.N)

PortBox = tk.Text(frame1, height=1, width=10)
PortBox.pack(side=tk.TOP, anchor=tk.N)

disconnectbtn = tk.Button(frame1, text="  Disconnect    ",
                          fg="red", bg="white", command=disconnect)
disconnectbtn.pack(side=tk.BOTTOM)
#disconnectbtn.pack(side = tk.TOP, fill = tk.Y)

connectbtn = tk.Button(frame1, text="     Connect     ",
                       fg="blue", bg="white", command=connect)
connectbtn.pack(side=tk.BOTTOM)
#connectbtn.pack(side = tk.TOP, fill = tk.Y)

IPlabel = tk.Label(frame, text="IP", fg="green", bg="white")
IPlabel.pack(side=tk.TOP, anchor=tk.NW)

portlabel = tk.Label(frame, text="PORT", fg="green", bg="white")
portlabel.pack(side=tk.BOTTOM, anchor=tk.NW)


# this defines the box where text is displayed
T1 = tk.Text((root), height=15, width=100)
T1.pack(side=tk.TOP)

# this defnes the box where the users type
T = tk.Text((root), height=4, width=100)
T.pack(side=tk.BOTTOM)

disp = Thread(target=disp_msg,args=(session,),daemon=True)
disp.start()

root.mainloop()
