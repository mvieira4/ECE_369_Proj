from p2p import p2p_connection
from collections import OrderedDict
import threading


class p2p_chat_session:
    # List of all sent and received messages
    message_list = []

    # Queue of messages waiting to be sent
    send_queue = []

    # Dict of all established connections
    connection_dict = {}

    # List of all receiver ports
    receivers_ports = []

    # List of all sender ports
    sender_ports = []


    # Value that tells methods stop all processes
    kill = False

    # Receives messages from peer sender socket
    def __receive_thread(self, connection):
        # Checks if it should shut down
        self.kill
        while(self.kill == False):
            # Attempts to receive message if it can't break loop
            try:
                # Gets message and adds it to message list
                msg = connection.recv()
                self.message_list.append(msg)

                # If exit received close connection, set kill true, and break loop
                if (msg.lower() == "exit"):
                    self.kill = True
                    connection.close()
                    break
            except ConnectionAbortedError:
                break

    # Sends messages in send queue
    def __send_thread(self):
        # Checks if it should shut down
        self.kill
        while(self.kill == False):
            # Checks if there is anything to send
            while(self.send_queue != []):
                for connection in self.connection_dict.values():
                    # Removes item from queue and sends it
                    send_str = self.send_queue.pop()
                    connection.send(send_str)

                    # Adds sent message to message list
                    self.message_list.append(send_str)

                    # If exit sent close connection, set kill true, and break loop
                    if(send_str == "exit"):
                        self.kill = True
                        connection.close()
                        break

    # Makes the threads for keeping track of messages
    def __create_connection_threads(self, connection):
        # Creates and starts threads that manages messages received and sent
        sender = threading.Thread(
            target=self.__send_thread)
        sender.daemon = True
        sender.start()

        receiver = threading.Thread(
            target=self.__receive_thread, args=(connection,))
        receiver.daemon = True
        receiver.start()
        print("[+] Created Connection Threads")

    # Accepts incoming connections
    def __accept_thread(self, receiver_port):
        # Checks if it should shut down
        while(self.kill == False):
            try:
                # Accepts connection
                connection = p2p_connection(receiver_port)
                self.__create_connection_threads(connection)

                # Adds connection to connection dictionary
                self.connection_dict[connection.peer_receiver_port] = connection
                print("[+] New Connection")
            except OSError:
                pass

    # Starts accept thread on initialization
    def __init__(self, receiver_port):
        self.receivers_ports.append(receiver_port)
        p2p_accept = threading.Thread(
            target=self.__accept_thread, args=(receiver_port,))
        p2p_accept.daemon = True
        p2p_accept.start()
        print("[+] Created Accept Thread")

    # Sends connection to another user
    def send_connection(self, peer_receiver_port):
        # Sends connection
        connection = p2p_connection(
            self.receivers_ports[-1] + 4, peer_receiver_port)
        self.__create_connection_threads(connection)

        # Adds connection to connection dictionary
        self.connection_dict[connection.peer_receiver_port] = connection
        print("[i] Connection Sent")

    # Closes connetion to specified peer
    def close_connection(self, connection_name):
        try:
            self.connection_dict[connection_name].close()
        except KeyError:
            print("[!] Not connected")
