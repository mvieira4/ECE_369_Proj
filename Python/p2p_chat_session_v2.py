from socket import *
from p2p_v2 import p2p_connection
from threading import *


class p2p_chat_session:
    # List of all sent and received messages
    message_list = []

    # Queue of messages waiting to be sent
    send_queue = []

    # Dict of all established connections
    connection_list = []

    active = True

    # Creates central socket
    def __init__(self, cent_port):
        self.cent_addr = (gethostname(),cent_port)
        self.cent_sock = socket(AF_INET, SOCK_STREAM)
        self.cent_sock.bind(self.cent_addr)
        self.cent_sock.listen(2)

        wait = Thread(target = self.acpt_p2p)
        wait.start()

        send_all = Thread(target = self.send_all_str)
        send_all.start()

    # Requests p2p connection
    def requ_p2p(self, target_ip, target_port):
        send_pipe = socket(AF_INET, SOCK_STREAM)
        send_pipe.connect((target_ip,target_port))

        info = " ".join(self.cent_addr)
        send_pipe.send(info.encode("utf-8"))
        recv_pipe, _ = self.cent_sock.accept()

        recv = Thread(target = self.recv_str, args = (recv_pipe,))
        recv.start()

        self.connection_list.append((recv_pipe, send_pipe))
    
    # Accepts p2p connection
    def acpt_p2p(self):
        while(self.acpt_p2p == True):
            recv_pipe, _ = self.cent_sock.accept()
            
            target_ip, target_port = recv_pipe.recv(1024)
            send_pipe = socket(AF_INET, SOCK_STREAM)
            send_pipe.connect((target_ip,target_port))

            recv = Thread(target = self.recv_str, args = (recv_pipe,))
            recv.start()

            self.connection_list.append((recv_pipe, send_pipe))

    def recv_prt_all(self):
        while(self.active == True):
            while(self.message_list != [] and self.connection_list != []):
                string = self.message_list.pop()
                print(f"{string}")

    def send_all_str(self):
        while(self.active == True):
            while(self.send_queue != [] and self.connection_list != []):
                string = self.send_queue.pop()
                self.message_list.append(string)
                for _, send_pipe in self.connection_list:
                    send_pipe.send(string.encode("utf-8"))

    def send_str(self,string):
        self.send_queue.append(string)

    def recv_str(self, recv_pipe) -> str:
        while(self.active == True):    
            self.message_list.append(recv_pipe.recv(1024).decode("utf-8"))

    def close_ses(self):
        self.active = False

        for connection in self.connection_list:
            for pipe in connection:
                pipe.close()