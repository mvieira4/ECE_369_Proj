from p2p_v2 import p2p_connection

receiver = int(input("Receiver: "))
connection = p2p_connection(receiver)
if(input("Connect: ").lower() == "yes"):
    peer = int(input("Peer: "))
    connection.send_con(peer)
    connection.send_str("Hello")
print("[*] Waiting...")
while(True):
    pass
    
