import socket
server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server.bind(('127.0.0.1', 12346))
print("UDP Server started...")
while True:
    data, addr = server.recvfrom(1024)
    print("UDP:", data.decode())
    server.sendto(data, addr)
