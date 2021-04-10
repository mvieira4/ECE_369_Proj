import socket
import threading 

def conn(send_sock,recv_sock,target_ip,target_port):
    try:
        send_sock.connect((target_ip,target_port))
        recv_addr, recv_port = recv_sock.getsockname()
        send_sock.send(recv_addr.encode("utf-8"))
        send_sock.send(recv_port.encode("utf-8"))
        recv_sock.accept()

    except ConnectionRefusedError:
        print("[!] Target Computer Unavailable")

def accecpt_conn(send_sock,recv_sock):
    try:
        target_sock,target_addr = recv_sock.accept()
        target_ip = target_sock.recv(1024).decode("utf-8")
        target_port = int(target_sock.recv(1024).decode("utf-8"))
        send_sock.connect((target_ip,target_port))

    except ValueError:
        print("[!] Invalid Value Received")
    
    

def receive_thread(target_sock,target_addr):
    print(f"[+] Connected to {target_addr}")
    while(True):
        target_msg = target_sock.recv().decode("utf-8")
        print(f"{target_addr} : {target_msg}")
        if(target_msg.lower() == "exit"):
            print(f"[-] Disconnected {target_addr}")
            target_sock.close()
            break
    
def send_thread(target_ip,target_port):
    my_socket.connect((target_ip,target_port))
    my_msg = input("[*] Enter Message: ")
    my_socket.send(my_msg.encode("utf-8"))

my_port = int(input("[*] Enter Your Port: "))
my_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
my_socket.bind((socket.gethostname(),my_port))

threads = []

accept_port = input("[*] Enter Receiving Port: ")
accept_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
accept_socket.bind((socket.gethostname(),accept_port))


command = input("[*] Enter + to Connect: ")

if(command == "+"):
    target_port = input("[*] Enter Target Port:")



