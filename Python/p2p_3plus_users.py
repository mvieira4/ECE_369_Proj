from os import truncate
from collections import deque
from p2p import p2p_connection
import threading
import socket

receive_queue = []
send_queue = []

kill = False


def receive_thread(connection):
    global kill
    while(kill == False):
        try:
            msg = connection.recv()
            receive_queue.append(msg)
            if (msg.lower() == "exit"):
                kill = True
                connection.close()
                print("\r[!] Press enter to close")
                break
        except ConnectionAbortedError:
            break


def send_thread(connection):
    global kill
    while(kill == False):
        while(send_queue != []):
            send_str = send_queue.pop()
            connection.send(send_str)
            if(send_str == "exit"):
                kill = True
                connection.close()
                print("\r[!] Press enter to close")
                break


def create_connection_threads(connection):
    sender = threading.Thread(target=send_thread, args=(connection,))
    sender.daemon = True
    receiver = threading.Thread(target=receive_thread, args=(connection,))
    receiver.daemon = True
    sender.start()
    receiver.start()


def connect_thread(acceptor_socket, peer_acceptor_port):
    connection = p2p_connection(acceptor_socket, peer_acceptor_port)
    create_connection_threads(connection)


def accept_thread(acceptor_socket):
    connection = p2p_connection(acceptor_socket)
    create_connection_threads(connection)


def get_str_thread():
    global kill
    while(kill == False):
        msg = input()
        send_queue.append(msg)
        if(msg.lower() == True):
            break


command = input("[$] ")
if(command.lower() == "yes"):
    acceptor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    acceptor.bind((socket.gethostname(), 4000))
    p2p_communication = threading.Thread(connect_thread(acceptor, 4500))
    p2p_communication.start()
else:
    acceptor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    acceptor.bind((socket.gethostname(), 4500))
    p2p_communication = threading.Thread(accept_thread(acceptor))
    p2p_communication.start()
get_str = threading.Thread(target=get_str_thread)
get_str.daemon
get_str.start()
