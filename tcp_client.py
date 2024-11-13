import socket
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('127.0.0.1', 12345))
print("Connected to TCP server")
while True:
    msg = input("Enter TCP message: ")
    client.sendall(msg.encode())
    print("Echo:", client.recv(1024).decode())
