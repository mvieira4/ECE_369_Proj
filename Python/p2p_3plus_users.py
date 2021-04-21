from os import truncate
from p2p_chat_session import p2p_chat_session
from p2p import p2p_connection
import threading

def get_str_thread(kill,send_queue):
    while(kill == False):
        msg = input()
        send_queue.append(msg)
        if(msg.lower() == True):
            break

command = input("\n[?] Would you like to connect?\n[<] ")

if(command.lower() == "1"):
    session = p2p_chat_session(4000)
    session.send_connection(4500)
elif(command.lower() == "2"):
    session = p2p_chat_session(5000)
    session.send_connection(4500)
    
else:
    session = p2p_chat_session(4500)
get_str = threading.Thread(target=get_str_thread, args=(session.kill,session.send_queue),daemon=True)
get_str.start()
while(session.kill == False):
    pass
