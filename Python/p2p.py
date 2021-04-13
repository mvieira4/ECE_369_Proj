import socket


class p2p_connection():
    def __send_connection(self):
        # Establish sender connection
        print("\r[*] Connecting to peer receiver...",
              end="\n[<] ")
        self.sender = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sender.connect(
            (socket.gethostname(), self.peer_acceptor_port))
        self.peer_acceptor_ip, self.peer_acceptor_port = self.sender.getpeername()
        print(
            f"\r[+] Sending to {self.peer_acceptor_ip} at port {self.peer_acceptor_port}", end="\n[<] ")

    def __get_connection(self):
        # Establish receiver connection
        print(f"\r[*] Waiting for receiver connection...")
        self.acceptor.listen()
        self.receiver, peer_sender_addr = self.acceptor.accept()
        self.peer_sender_ip, self.peer_sender_port = peer_sender_addr
        print(
            f"\r[+] Receiving from {self.peer_sender_ip} at port {self.peer_sender_port}", end="\n[<] ")

    def __init__(self, *args):
        if(len(args) > 1):
            # Create acceptor socket
            self.acceptor = args[0]
            self.acceptor_ip, self.acceptor_port = self.acceptor.getsockname()

            # Establish sender connection
            self.peer_acceptor_port = args[1]
            self.__send_connection()

            # Send receiver information
            self.sender.send(socket.gethostname().encode("utf-8"))
            print("\r[i] Sent receiver ip")
            self.sender.send(str(self.acceptor_port).encode("utf-8"))
            print("\r[i] Sent receiver port")

            # Establish receiver connection
            self.__get_connection()
        else:
            # Create acceptor socket
            self.acceptor = args[0]
            self.acceptor_ip, self.acceptor_port = self.acceptor.getsockname()

            # Establish receiver connection
            self.__get_connection()

            # Get peer accept information
            self.peer_acceptor_ip = self.receiver.recv(1024).decode("utf-8")
            print("\r[i] Received peer receiver ip",
                  end="\n[<] ")
            self.peer_acceptor_port = int(
                self.receiver.recv(1024).decode("utf-8"))
            print("\r[i] Received peer receiver port",
                  end="\n[<] ")

            # Establish sender connection
            self.__send_connection()

    def send(self, msg):
        self.sender.send(msg.encode("utf-8"))
        print("", end="[<] ")

    def recv(self):
        receiver_str = self.receiver.recv(1024).decode("utf-8")
        print(
            f"\r[i] From {self.peer_sender_ip} at port {self.peer_sender_port}\n[>] {receiver_str}", end="\n[<] ")
        return receiver_str

    def close(self):
        self.sender.close()
        print(
            f"\r[*] Closing send socket...\n[-] Closing connection to {self.peer_acceptor_ip} at port {self.peer_acceptor_port}", end="\n[<] ")
        self.receiver.close()
        print(
            f"\r[*] Closing receive socket...\n[-] Closing connection to {self.peer_sender_ip} at port {self.peer_sender_port}", end="\n[<] ")

        self.acceptor.close()
        print("\r[*] Closing acceptor socket...", end="\n[<] ")
