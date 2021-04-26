from socket import *
from threading import *
from time import sleep


class p2p_chat_session:
    # List of all sent and received messages
    message_list = []

    # Queue of messages waiting to be sent
    send_queue = []

    # Dictionary of all established connections
    connection_dict = {}

    # Indicate if session active
    active = True

    # Starts session
    def __init__(self, cent_port):
        # Creates central socket
        self.cent_addr = (gethostname(), cent_port)
        self.cent_sock = socket(AF_INET, SOCK_STREAM)
        self.cent_sock.bind(self.cent_addr)
        self.cent_sock.listen()
        print(f"[i] Created Central Socket At {gethostname()}:{cent_port}")

        # Starts waiting for inbound connections
        wait = Thread(target=self.acpt_p2p, daemon=True)
        wait.start()
        print("[*] Waiting For Inbound Connection...")

        # Starts waiting for string to send to all connections
        send_all = Thread(target=self.send_all_str, daemon=True)
        send_all.start()
        print("[i] Session Started")

    # Requests p2p connection
    def requ_p2p(self, target_ip, target_port):
        ip, port = self.cent_addr
        # Stops connection from connection to itself
        if(self.cent_addr == (target_ip, target_port)):
            print("[!] You Can't Connect To Yourself")
        # Stops from connecting to safe peer twice
        elif(target_port in self.connection_dict):
            print("[!] Already Connected")
        # Requests connection
        else:
            # Passes connection when more than one connection
            if(len(self.connection_dict) > 1):
                key = list(self.connection_dict.keys())[0]
                self.connection_dict[key][1].send("CON".encode("utf-8"))
                self.connection_dict[key][1].send(f"{target_ip} {target_port}".encode("utf-8"))
                sleep(0.3)
                self.sever_con(key)
                print(f"connecting to {key}")

            # Creates closed system
            elif(len(self.connection_dict) == 1):
                key = list(self.connection_dict.keys())[0]
                self.connection_dict[key][1].send("CON".encode("utf-8"))
                self.connection_dict[key][1].send(f"{target_ip} {target_port}".encode("utf-8"))
            
            # Creates send socket
            send_pipe = socket(AF_INET, SOCK_STREAM)
            send_pipe.connect((target_ip, target_port))
            print(f"[i] Created Sending Pipeline")

            recv_pipe = socket(AF_INET, SOCK_STREAM)
            recv_pipe.connect((target_ip, target_port))
            print(f"[i] Created Receiving Pipeline")

            send_pipe.send(f"{ip} {port}".encode("utf-8"))

            # Starts listening for incoming messages and adds them to message list
            recv = Thread(target=self.recv_str, args=(recv_pipe,))
            recv.start()
            print("[i] Listening On Receiving Pipeline")

            # Adds receiving socket and send socket as tuple to connection list
            self.connection_dict[target_port] = (recv_pipe, send_pipe)
            print(
                f"[+] {len(self.connection_dict)} Connection(s)")

    # Accepts p2p connection
    def acpt_p2p(self):
        # Accepts connections as long as session active
        while(self.active == True):
            try:
                recv_pipe, _ = self.cent_sock.accept()
                print("[i] Created Receiving Pipeline")

                send_pipe, _ = self.cent_sock.accept()
                print(f"[i] Created Sending Pipeline")

                target_ip, target_port_str = recv_pipe.recv(
                    1024).decode("utf-8").split()
                target_port = int(target_port_str)

                # Starts listening for incoming messages and adds them to message list
                recv = Thread(target=self.recv_str,
                              args=(recv_pipe,), daemon=True)
                recv.start()
                print("[i] Listening On Receiving Pipeline")

                # Adds receiving socket and send socket as tuple to connection list
                self.connection_dict[target_port] = (recv_pipe, send_pipe)
                print(
                    f"[+] {len(self.connection_dict)} Connection(s)")

                for thing in self.connection_dict.keys():
                    print(f"{thing}")
            except:
                pass

    # Print all messages
    def recv_prt_all(self):
        while(self.active == True):
            while(self.message_list != [] and self.connection_dict != {}):
                string = self.message_list.pop()
                print(f"{string}")
            sleep(0.3)

    # Send all contents of send que to all connections
    def send_all_str(self):
        # Sends content while session active, there are connections, and things to send
        while(self.active == True):
            while(self.send_queue != [] and self.connection_dict != {}):
                # Takes first item in list and sends it to all connections
                string = str(self.cent_addr[1]) + ": " + self.send_queue.pop()
                self.message_list.append(string)
                for _, send_pipe in self.connection_dict.values():
                    try:
                        send_pipe.send("MES".encode("utf-8"))
                        send_pipe.send(string.encode("utf-8"))
                    except ConnectionResetError:
                        pass

            sleep(0.3)

    # Puts string in send queue
    def send_str(self, string):
        self.send_queue.append(string)

    # Recives string from peer and ads it to message list
    def recv_str(self, recv_pipe) -> str:
        while(self.active == True):
            try:
                action = recv_pipe.recv(1024).decode("utf-8")
                if(action == "MES"):
                    message = recv_pipe.recv(1024).decode("utf-8")
                    self.message_list.append(message)
                elif(action == "CON"):
                    sleep(0.2)
                    target_ip, target_port = recv_pipe.recv(
                        1024).decode("utf-8").split()
                    self.requ_p2p(target_ip, int(target_port))
                elif(action == "DIS"):
                    target_ip, target_port_str = recv_pipe.recv(
                        1024).decode("utf-8").split()
                    target_port = int(target_port_str)
                    self.sever_con(target_port)
                    for pipe in self.connection_dict.pop(target_port):
                        pipe.close()
                    print(
                        f"[-] {len(self.connection_dict)} Connection(s)")

            except OSError:
                break

    def sever_con(self, target_port):
            self.connection_dict[target_port][1].send("DIS".encode("utf-8"))
            ip, port = self.cent_addr
            self.connection_dict[target_port][1].send(
                f"{ip} {port}".encode("utf-8"))
            for pipe in self.connection_dict.pop(target_port):
                pipe.close()
                print("[i] Pipe Closed")

    def discon_ses(self):
        for connection in self.connection_dict.values():
            try:
                connection[1].send("DIS".encode("utf-8"))
                ip, port = self.cent_addr
                connection[1].send(f"{ip} {port}".encode("utf-8"))
                for pipe in connection:
                    pipe.close()
                    print("[i] Pipe Closed")

            except ConnectionResetError:
                pass
        self.connection_dict = {}
        print(
            f"[-] {len(self.connection_dict)} Connection(s)")

    # Sets session to inactive and closes all sockets
    def close_ses(self):
        self.active = False
        self.discon_ses()
        self.connection_dict = {}
        self.cent_sock.close()
        print("[i] Central Socket Closed")
