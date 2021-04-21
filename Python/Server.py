import socket
import threading

# Create server socket
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((socket.gethostname(), 4200))
server.listen(5)

print("Waiting for connection...")
sock,addr = server.accept()
print(f"Connected to {addr} {sock}")
print(sock.getsockname())
sock.send("Welcome".encode("utf-8"))

while(True):
    msg = sock.recv(1024).decode("utf-8")
    print(f"Message: {msg}")
    sock.send(msg.upper().encode("utf-8"))
    
    if(msg.lower() == "exit"):
        sock.close()
        print(f"Connection to {addr} closed")
        break
server.close()



