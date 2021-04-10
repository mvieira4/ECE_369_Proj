import socket

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.bind((socket.gethostname(), 4000))
client.connect((socket.gethostname(), 4200))

msg = client.recv(1024).decode("utf-8")
print(f"Message: {msg}")

while(True):
    rsp = input("Send Something: ")
    client.send(rsp.encode("utf-8"))
    msg = client.recv(1024).decode("utf-8")
    print(f"Message: {msg}")
    if(rsp.lower() == "exit"):
        break
client.close()