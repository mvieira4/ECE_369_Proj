from socket import *
from threading import *
from time import sleep


class p2p_chat_session:
    # List of all sent and received messages
    display_queue = []

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
        wait = Thread(target=self.__acpt_p2p)
        wait.start()
        print("[*] Waiting For Inbound Connection...")

        # Starts waiting for string to send to all connections
        send_all = Thread(target=self.__send_all_str)
        send_all.start()
        print("[i] Session Started")

    def __send_p2p(self, target_ip, target_port):
        ip, port = self.cent_addr
        # Stops connection from connection to itself
        if(self.cent_addr == (target_ip, target_port)):
            print("[!] You Can't Connect To Yourself")
        # Stops from connecting to safe peer twice
        elif(target_port in self.connection_dict):
            print("[!] Already Connected")
        # Requests connection
        else:
            # Creates send socket
            send_pipe = socket(AF_INET, SOCK_STREAM)
            send_pipe.connect((target_ip, target_port))
            print(f"[i] Created Sending Pipeline")

            recv_pipe = socket(AF_INET, SOCK_STREAM)
            recv_pipe.connect((target_ip, target_port))
            print(f"[i] Created Receiving Pipeline")

            # Send central port info
            send_pipe.send(f"{ip} {port}".encode("utf-8"))
            print("[i] Port Info Sent")
            print(f"({target_ip},{target_port})")

            # Starts listening for incoming messages and adds them to message list
            recv = Thread(target=self.recv_str, args=(recv_pipe,))
            recv.start()
            print("[i] Listening On Receiving Pipeline")

            # Adds receiving socket and send socket as tuple to connection list
            self.connection_dict[target_port] = (recv_pipe, send_pipe)
            print(
                f"[+] {len(self.connection_dict)} Connection(s)")
                
            if(len(self.connection_dict)> 2):
                    key = list(self.connection_dict.keys())[0]
                    self.sever_con(key)




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
            # Creates send socket
            send_pipe = socket(AF_INET, SOCK_STREAM)
            send_pipe.connect((target_ip, target_port))
            print(f"[i] Created Sending Pipeline")

            recv_pipe = socket(AF_INET, SOCK_STREAM)
            recv_pipe.connect((target_ip, target_port))
            print(f"[i] Created Receiving Pipeline")

            # Send central port info
            send_pipe.send(f"{ip} {port}".encode("utf-8"))
            print("[i] Port Info Sent")
            print(f"({target_ip},{target_port})")

            # Starts listening for incoming messages and adds them to message list
            recv = Thread(target=self.recv_str, args=(recv_pipe,))
            recv.start()
            print("[i] Listening On Receiving Pipeline")

            # Adds receiving socket and send socket as tuple to connection list
            self.connection_dict[target_port] = (recv_pipe, send_pipe)
            print(
                f"[+] {len(self.connection_dict)} Connection(s)")

            # Tell peer to connect to target
            if(len(self.connection_dict)> 1):
                key = list(self.connection_dict.keys())[0]
                self.connection_dict[key][1].send("CON".encode("utf-8"))
                print(f"({target_ip},{target_port}")
                self.connection_dict[key][1].send(f"{target_ip} {target_port}".encode("utf-8"))
                ip, port_str = self.cent_addr
                port = int(port_str)
                print(f"({ip},{port}")

                # Disconnect from a peer
                if(len(self.connection_dict)> 2):
                    self.sever_con(key)
            
    # Accepts p2p connection
    def __acpt_p2p(self):
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
                                args=(recv_pipe,))
                recv.start()
                print("[i] Listening On Receiving Pipeline")

                # Adds receiving socket and send socket as tuple to connection list
                self.connection_dict[target_port] = (recv_pipe, send_pipe)
                print(
                    f"[+] {len(self.connection_dict)} Connection(s)")

                for thing in self.connection_dict.keys():
                    print(f"{thing}")
            except OSError:
                pass
            

    # Send all contents of send que to all connections
    def __send_all_str(self):
        # Sends content while session active, there are connections, and things to send
        while(self.active == True):
            while(self.send_queue != [] and self.connection_dict != {}):
                # Takes first item in list and sends it to all connections
                string = str(self.cent_addr[1]) + ": " + self.send_queue.pop()
                self.display_queue.append(string)
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
    def recv_str(self, recv_pipe):
        while(self.active == True):
            try:
                # Listens for action code
                action = recv_pipe.recv(1024).decode("utf-8")
                # Sends message
                if(action == "MES"):
                    message = recv_pipe.recv(1024).decode("utf-8")
                    self.display_queue.append(message)

                elif(action == "DIS"):
                    info = recv_pipe.recv(
                        1024).decode("utf-8").split()
                    target_ip = info[0]
                    target_port = int(info[1])
                    print(f"{target_ip},{target_port}")
                    self.sever_con(target_port)

                # Tells peer who to connect to
                elif(action == "CON"):
                    info = recv_pipe.recv(
                        1024).decode("utf-8").split()

                    target_ip = info[0]
                    target_port = int(info[1])
                    print(f"{target_ip},{target_port}")
                    self.__send_p2p(target_ip, target_port)
                    
                    print(f"[-] {len(self.connection_dict)} Connection(s)")                  

            except OSError:
                break

    # Closes all pipes and removes the connection from dictionary
    def sever_con(self, target_port):
            for pipe in self.connection_dict.pop(target_port):
                pipe.close()
                print("[i] Pipe Closed")
            print(
                        f"[-] {len(self.connection_dict)} Connection(s)")


    def discon_all(self):
        try:
            # Gets central socket ip and port
            ip, port_str = self.cent_addr
            port = int(port_str)
            print(f"({ip},{port}")
    
            # Patches connection if more than 1
            if(len(self.connection_dict)>1):
                key1 = list(self.connection_dict.keys())[0]
                key2 = list(self.connection_dict.keys())[1]
                self.connection_dict[key1][1].send("CON".encode("utf-8"))
                self.connection_dict[key1][1].send(f"{ip} {key2}".encode("utf-8"))
                self.sever_con(key1)

            # Disconnects from last peer
            key = list(self.connection_dict.keys())[0]
            self.connection_dict[key][1].send("DIS".encode("utf-8"))
            self.connection_dict[key][1].send(f"{ip} {port}".encode("utf-8"))
            self.sever_con(key)
            
        except ConnectionResetError:
            pass

        except IndexError:
            pass
        self.connection_dict = {}
        print(
            f"[-] {len(self.connection_dict)} Connection(s)")

    # Sets session to inactive and closes all sockets
    def close_ses(self):
        self.active = False
        self.discon_all()
        self.connection_dict = {}
        self.cent_sock.close()
        print("[i] Central Socket Closed")
