from socket import *
from p2p_v2 import p2p_connection
from threading import *


class p2p_chat_session:
    # List of all sent and received messages
    message_list = []

    # Queue of messages waiting to be sent
    send_queue = []

    # List of all established connections
    connection_list = []

    # Indicate if session active
    active = True

    # Starts session
    def __init__(self, cent_port):
        # Creates central socket
        self.cent_addr = (gethostname(),cent_port)
        self.cent_sock = socket(AF_INET, SOCK_STREAM)
        self.cent_sock.bind(self.cent_addr)
        self.cent_sock.listen(2)

        # Starts waiting for inbound connections
        wait = Thread(target = self.acpt_p2p)
        wait.start()

        # Starts waiting for string to send to all connections
        send_all = Thread(target = self.send_all_str)
        send_all.start()

    # Requests p2p connection
    def requ_p2p(self, target_ip, target_port):
        # Creates send socket
        send_pipe = socket(AF_INET, SOCK_STREAM)
        send_pipe.connect((target_ip,target_port))

        # Gets central socket info, sends it, and accepts connection
        info = " ".join(self.cent_addr)
        send_pipe.send(info.encode("utf-8"))
        recv_pipe, _ = self.cent_sock.accept()

        # Starts listening for incoming messages and adds them to message list
        recv = Thread(target = self.recv_str, args = (recv_pipe,))
        recv.start()

        # Adds receiving socket and send socket as tuple to connection list
        self.connection_list.append((recv_pipe, send_pipe))
    
    # Accepts p2p connection
    def acpt_p2p(self):
        # Accepts connections as long as session active
        while(self.acpt_p2p == True):
            recv_pipe, _ = self.cent_sock.accept()
            
            # Receives peer central socket and connects
            target_ip, target_port = recv_pipe.recv(1024)
            send_pipe = socket(AF_INET, SOCK_STREAM)
            send_pipe.connect((target_ip,target_port))

            # Starts listening for incoming messages and adds them to message list
            recv = Thread(target = self.recv_str, args = (recv_pipe,))
            recv.start()

            # Adds receiving socket and send socket as tuple to connection list
            self.connection_list.append((recv_pipe, send_pipe))

    # Print all messages
    def recv_prt_all(self):
        while(self.active == True):
            while(self.message_list != [] and self.connection_list != []):
                string = self.message_list.pop()
                print(f"{string}")

    # Send all contents of send que to all connections
    def send_all_str(self):
        # Sends content while session active, there are connections, and things to send
        while(self.active == True):
            while(self.send_queue != [] and self.connection_list != []):
                # Takes first item in list and sends it to all connections
                string = self.send_queue.pop()
                self.message_list.append(string)
                for _, send_pipe in self.connection_list:
                    send_pipe.send(string.encode("utf-8"))

    # Puts string in send queue
    def send_str(self,string):
        self.send_queue.append(string)

    # Recives string from peer and ads it to message list
    def recv_str(self, recv_pipe) -> str:
        while(self.active == True):    
            self.message_list.append(recv_pipe.recv(1024).decode("utf-8"))

    # Sets session to inactive and closes all sockets
    def close_ses(self):
        self.active = False

        for connection in self.connection_list:
            for pipe in connection:
                pipe.close()
        self.cent_sock.close()