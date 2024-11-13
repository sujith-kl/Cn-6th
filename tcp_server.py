import socket, threading
def handle_client(conn):
    while True:
        data = conn.recv(1024)
        if not data: break
        print("TCP:", data.decode())
        conn.sendall(data)
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('127.0.0.1', 12345))
server.listen()
print("TCP Server started...")
while True:
    conn, _ = server.accept()
    threading.Thread(target=handle_client, args=(conn,)).start()
