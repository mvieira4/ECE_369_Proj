import socket
import ssl

# SET VARIABLES
packet, reply = "<packet>SOME_DATA</packet>", ""
HOST, PORT = 'XX.XX.XX.XX', 4434

# CREATE SOCKET
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.settimeout(10)

# WRAP SOCKET
wrappedSocket = ssl.wrap_socket(sock, ssl_version=ssl.PROTOCOL_TLSv1, ciphers="ADH-AES256-SHA")

# CONNECT AND PRINT REPLY
wrappedSocket.connect((HOST, PORT))
wrappedSocket.send(packet)
print(wrappedSocket.recv(1280))

# CLOSE SOCKET CONNECTION
wrappedSocket.close()