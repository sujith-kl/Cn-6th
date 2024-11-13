import socket
client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
print("Connected to UDP server")
while True:
    msg = input("Enter UDP message: ")
    client.sendto(msg.encode(), ('127.0.0.1', 12346))
    print("Echo:", client.recv(1024).decode())
