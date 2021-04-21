import socket

# Peer to peer connection class


class p2p_connection():

    # Establish sender connection
    def __send_connection(self):

        # Defines sender IP and sender port
        self.sender_ip = self.receiver_ip
        self.sender_port = self.receiver_port - 1

        # Creates sender socket
        self.sender = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sender.bind((self.sender_ip, self.sender_port))
        print(f"[+] Created Sender")

        # Connects to peer receiver port
        self.sender.connect((socket.gethostname(), self.peer_receiver_port))

    # Establishes receiver connection
    def __get_connection(self):
        # Accepts connection to receiver
        self.receiver.listen()
        self.receiver, peer_sender_addr = self.receiver.accept()
        print(f"[i] Connection Accepted")

        # Gets peer infomation from socket
        self.peer_sender_ip, self.peer_sender_port = peer_sender_addr

    # Creates receiver socket
    def __create_receiver(self, port):
        # Stores receiver information
        self.receiver_ip = socket.gethostname()
        self.receiver_port = port

        # Creates receiver socket
        self.receiver = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.receiver.bind((self.receiver_ip, self.receiver_port))
        print("[+] Created Receiver")

    # Creates connection which connects to peer
    def __init__(self, *args):
        if(len(args) > 1):
            # Create receiver socket
            self.__create_receiver(args[0])

            # Establish sender connection
            self.peer_receiver_ip = socket.gethostname()
            self.peer_receiver_port = args[1]
            self.__send_connection()

            # Send receiver information\
            information = socket.gethostname() + " " + str(self.receiver_port)
            self.sender.send(information.encode("utf-8"))
            print("[i] Receiver Info Sent")

            # Establish receiver connection
            self.__get_connection()
        else:
            # Create receiver socket
            self.__create_receiver(args[0])

            # Establish receiver connection
            self.__get_connection()

            # Get peer receiver information
            peer_receiver_ip, receiver_port = self.receiver.recv(1024).decode("utf-8").split(" ")
            self.peer_receiver_ip = peer_receiver_ip
            self.peer_receiver_port = int(receiver_port)
            print("[i] Receiver Info Received")

            # Establish sender connection
            self.__send_connection()

    # Sends strings to peer
    def send(self, msg):
        self.sender.send(msg.encode("utf-8"))
        print("[i] Sent")

    # Receives information from peer
    def recv(self):
        receiver_str = self.receiver.recv(1024).decode("utf-8")
        print("[i] Received")
        return receiver_str

    # Attempt to close all connection sockets
    def close(self):
        try:
            self.sender.close()
            print("[-] Closed Sender")
        except OSError:
            pass

        try:
            self.receiver.close()
            print("[-] Closed Receiver")
        except OSError:
            pass
