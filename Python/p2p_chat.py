#from tkinter import *
import tkinter as tk
from p2p_chat_session import p2p_chat_session

def connect():
    pass

def clicked():                                                   # clicked function defined here
    # T1 = tk.Text((root) ,height = 18, width=100)
    #T1.pack(side = tk.TOP)
    # should retrieve the text entered by user
    retrieveinput = T.get("1.0", tk.END)
    # inserts text into text chat window
    T1.insert(tk.INSERT, retrieveinput)
    # clears the text entry box after each sent message
    T.delete("1.0", tk.END)
    # print(T.get("1.0",'end-1c'))


root = tk.Tk()
root.geometry("600x600")  # SIZE OF APP WINDOW
root.title("CHAT APP")    # TITLE OF APP WINDOW
root.configure(bg="white")  # changes the background color


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



frame1 = tk.Frame(root)
frame1.pack(side=tk.RIGHT, anchor=tk.S)

frame = tk.Frame(root)
frame.pack(side=tk.LEFT, anchor=tk.NE)

# BUTTON DEFINITIONS BELOW

btn = tk.Button(root, text=" Send ", fg="green", bg="black", command=clicked)
btn.pack(side=tk.RIGHT, anchor=tk.SW)
#btn.pack(side = tk.RIGHT, fill = tk.Y)
#btn.bind("<Return>", clicked)

session = p2p_chat_session(4000)

disconnectbtn = tk.Button(frame, text="Disconnect",
                          fg="red", bg="black", command=connect)
disconnectbtn.pack(side=tk.BOTTOM)
#disconnectbtn.pack(side = tk.TOP, fill = tk.Y)

connectbtn = tk.Button(frame, text="  Connect  ",
                       fg="blue", bg="black", command=connect)
connectbtn.pack(side=tk.TOP)
#connectbtn.pack(side = tk.TOP, fill = tk.Y)


# This defines the box where text is displayed
T1 = tk.Text((root), height=15, width=100)
T1.pack(side=tk.TOP)

# This defines the box where the users type
T = tk.Text((root), height=4, width=100)
T.pack(side=tk.BOTTOM)


root.mainloop()
