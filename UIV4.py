#from tkinter import *
import tkinter as tk
from p2p_chat_session_v2 import p2p_chat_session
#from tkinter import scrolledtext

root = tk.Tk() 
root.geometry("600x600")  # SIZE OF APP WINDOW
root.title("CHAT APP")    # TITLE OF APP WINDOW
root.configure(bg = "black") # changes the background color 


# lbl = Label(root, text="Hello")

# lbl.pack(side = LEFT)
#w = Label(root, text ='GeeksForGeeks', 
		#font = "50") 

#w.pack() 


#mylist = Listbox(root, 
				#yscrollcommand = scroll_bar.set ) 

#for line in range(1, 26): 
	#mylist.insert(END, "Geeks " + str(line)) 

#mylist.pack( side = LEFT, fill = BOTH ) 

#scroll_bar.config( command = mylist.yview ) 
# T = StringVar()


#message_display_box = Text((root) ,height = 18, width=100)
#message_display_box.pack(side = TOP)


def clicked():                                                   # clicked function defined here 
  # message_display_box = tk.Text((root) ,height = 18, width=100)
   #message_display_box.pack(side = tk.TOP)
 
   retrievename = nameBox.get("1.0",tk.END)
   message_display_box.insert(tk.INSERT, retrievename)

   retrieveinput  =  text_input_box.get("1.0",tk.END)       # should retrieve the text entered by user
   #p2p_chat_session.send_str(socket.gethostname(), retrieveinput)
   message_display_box.insert(tk.INSERT, retrieveinput)         # clears the text entry box after each sent message
   text_input_box.delete("1.0",tk.END)

  

   
                        
  



def connect(): # this is the function that will execute when the connect button is pressed
	# DELETE EVERYTHING AFTER THE PORTVALUE  AND ADD THE CODE TO CONNECT, 

	# when the connect button is pressed the IP and port numbers will be stored in IPValue and PORTValue 
   IPValue=IPBox.get("1.0","end-1c") # STORES THE IP VALUE
   PORTValue=PortBox.get("1.0","end-1c") # STORES THE PORT VALUE
   
   
   retrieveinput2  =  IPBox.get("1.0",tk.END)       
   message_display_box.insert(tk.INSERT, retrieveinput2)         
   text_input_box.delete("1.0",tk.END)


   # this is the function that will execute when the disconnect button is pressed
def disconnect():
	# DELETE EVERYTHING WITHIN THIS FUNCTION AND ADD THE CODE TO DISCONNECT
 
  retrieveinput2  = IPBox.get("1.0",tk.END)       
  message_display_box.insert(tk.INSERT, retrieveinput2)         
  text_input_box.delete("1.0",tk.END)
 
frame = tk.Frame(root,bg = "black")
frame.pack(side = tk.LEFT,anchor=tk.NW)

frame1 = tk.Frame(root,bg = "black")
frame1.pack(side = tk.LEFT,anchor=tk.N)



#frame2 = tk.Frame(root,bg = "black")
#frame2.pack(side = tk.TOP,anchor=tk.N)


nameBox=tk.Text(frame1, height=1, width=14)
nameBox.pack(side = tk.TOP,anchor = tk.N)

# BUTTON DEFINITIONS BELOW

btn = tk.Button(root, text=" Send ",fg = "green",bg = "black",command = clicked)
btn.pack(side = tk.RIGHT, anchor = tk.SW)
#btn.pack(side = tk.RIGHT, fill = tk.Y)
#btn.bind("<Return>", clicked)

IPBox=tk.Text(frame1, height=1, width=14)
IPBox.pack(side = tk.TOP,anchor = tk.N)

PortBox=tk.Text(frame1, height=1, width=10)
PortBox.pack(side = tk.TOP,anchor = tk.N)

disconnectbtn = tk.Button(frame1, text="  Disconnect    ",fg = "red",bg = "black",command = disconnect)
disconnectbtn.pack(side=tk.BOTTOM)
#disconnectbtn.pack(side = tk.TOP, fill = tk.Y)

connectbtn = tk.Button(frame1, text="     Connect     ",fg = "blue",bg = "black",command = connect)
connectbtn.pack(side=tk.BOTTOM)
#connectbtn.pack(side = tk.TOP, fill = tk.Y)

IPlabel = tk.Label(frame, text="IP",fg = "green",bg = "black")
IPlabel.pack(side=tk.BOTTOM, anchor = tk.NW)

portlabel= tk.Label(frame, text="PORT",fg = "green",bg = "black")
portlabel.pack(side=tk.BOTTOM, anchor = tk.NW)

namelabel = tk.Label(frame, text="USER",fg = "green",bg = "black")
namelabel.pack(side=tk.TOP, anchor = tk.NW)

#sbVerticalScrollBar.pack(fill=tk.Y, side=tk.RIGHT, expand=tk.FALSE)

message_display_box = tk.Text((root) ,height = 15, width=100,wrap=tk.WORD) # this defines the box where text is displayed 
message_display_box.pack(side = tk.TOP)
#message_display_box.grid(column=0, columnspan=3)


#scroll_y = tk.Scrollbar(root, orient="vertical", command=message_display_box.yview)
#scroll_y.pack(side=tk.RIGHT, expand=True, fill="y")

text_input_box = tk.Text ((root) ,height=4, width=100)  # this defnes the box where the users type
text_input_box.pack(side = tk.BOTTOM)


#message_display_box.configure(yscrollcommand=scroll_y.set)

root.mainloop() 
