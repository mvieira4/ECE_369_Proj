import socket
import sys


try:
    port = int(sys.argv[1])

    print(port)
    host = socket.gethostname()

    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind((host, port))

    while(True):
        command = input("- ")
        if(command.lower() == "connect"):
            target_port = int(input("Enter Target Port: "))
            sock.connect((socket.gethostname(), target_port))
            sock.send("Hello".encode("utf-8"))
            msg = sock.recv(1024).decode("utf-8")
            print(f"Message: {msg}")
            while(True):
                rsp = input("Send Something: ")
                sock.send(rsp.encode("utf-8"))
                msg = sock.recv(1024).decode("utf-8")
                print(f"Message: {msg}")

                if(rsp.lower() == "exit"):
                    break
            sock.close()
        else:
            sock.listen(5)
            print("Waiting for connection...")
            peer_sock, peer_addr = sock.accept()
            print(f"Connected to {peer_addr}")
            msg = peer_sock.recv(1024).decode("utf-8")
            print(f"Message: {msg}")
            peer_sock.send("Hello".encode("utf-8"))
            while(True):
                msg = peer_sock.recv(1024).decode("utf-8")
                print(f"Message: {msg}")
                rsp = input("Send Something: ")
                peer_sock.send(rsp.encode("utf-8"))
                
                if(rsp.lower() == "exit"):
                    break
            sock.close()
            peer_sock.close()
        exit()

except ValueError:
    print("Invalid Value")

except ConnectionRefusedError:
    print("Peer not active")


#sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
