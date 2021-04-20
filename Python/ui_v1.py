#from tkinter import *
import tkinter as tk 

root = tk.Tk() 
root.geometry("500x500") 
root.title("CHAT APP")



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
T1 = tk.Text((root) ,height = 18, width=100)
T1.pack(side = tk.TOP)
T = tk.Text ((root) ,height=4, width=100)
T.pack(side = tk.BOTTOM)

#T1 = Text((root) ,height = 18, width=100)
#T1.pack(side = TOP)

def clicked():
  # T1 = tk.Text((root) ,height = 18, width=100)
   #T1.pack(side = tk.TOP)
   retrieveinput  =  T.get("1.0",tk.END)       # should retrieve the text entered by user
   T1.insert(tk.INSERT, retrieveinput)         # inserts text into text chat window
   T.delete("1.0",tk.END)                      # clears the text entry box after each sent message
  # print(T.get("1.0",'end-1c'))
	

	

btn = tk.Button(root, text="Send",command = clicked)
btn.pack(side = tk.RIGHT, fill = tk.Y)
#btn.bind("<Return>", clicked)



root.mainloop() 
