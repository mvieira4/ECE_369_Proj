from socket import *
from threading import *


class p2p_connection():

    # Local port and ip values
    #recv_addr = None
    #send_addr = None
    #send_sock = socket()
    #recv_sock = socket()

    # Peer port and ip values
    #peer_send_addr = None
    #peer_recv_addr = None

    # Create connection
    def __init__(self, recv_port):
        # Assign local Ports
        recv_port = recv_port
        send_port = recv_port + 100
        self.recv_addr = (gethostname(), recv_port)
        self.send_addr = (gethostname(), send_port)

        # Create Local Sockets
        self.recv_sock = socket(AF_INET, SOCK_STREAM)
        self.recv_sock.bind(self.recv_addr)
        self.send_sock = socket(AF_INET, SOCK_STREAM)
        self.send_sock.bind(self.send_addr)
        print("[+] Sockets created")

        # Wait for connections
        wait_conn = Thread(target=self.recv_conn, daemon=True)
        wait_conn.start()
        print("[*] Waiting for connection...")

    # Send out connection to peer
    def send_con(self, peer_recv_port):
        self.peer_recv_addr = (gethostname(), peer_recv_port)
        self.send_sock.connect((self.peer_recv_addr))
        print("[+] Sender connection")

        recv_ip, recv_port = self.recv_addr
        self.send_sock.send(
            " ".join((recv_ip, str(recv_port))).encode("utf-8"))
        print("[i] Info sent")

        self.recv_sock, self.peer_send_addr = self.recv_sock.accept()
        print("[+] Receiver connection")

    # Receive connection from peer
    def recv_conn(self):
        self.recv_sock.listen(5)
        self.__recv_pipe, self.peer_send_addr = self.recv_sock.accept()
        print("[+] Receiver connection")

        peer_recv_ip, peer_recv_port = self.__recv_pipe.recv(1024).decode("utf-8").split()
        self.peer_recv_addr = (peer_recv_ip, int(peer_recv_port))
        print("[i] Info received")

        self.send_sock.connect(self.peer_recv_addr)
        print("[+] Sender connection")

    # Send message
    def send_str(self, string):
        self.send_sock.send(string.encode("utf-8"))

    # Receive message
    def recv_str(self):
        return self.__recv_pipe.recv(1024).decode("utf-8")

    # Close connection
    def clear_conn(self):
        # Close connection
        self.__recv_pipe.close()
        self.send_sock.close()
    
        # Wait for new connection
        wait_con = Thread(target=self.recv_conn, daemon=True)
        wait_con.start()
        print("[*] Waiting for connection...")
    
    def kill_conn(self):
        self.recv_sock.close()
        self.send_sock.close()
        self.__recv_pipe.close()