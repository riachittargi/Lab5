import socket

def start_server(host='127.0.0.1', port=12345):
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen(1)  # Listen for a client connection

    print(f"Server listening on {host}:{port}...")

    conn, addr = server_socket.accept()  # Accept a client connection
    print(f"Connected by {addr}")

    while True:
        data = conn.recv(1024).decode()  # Receive data from client
        if not data:
            break  # Stop if no data is received

        print(f"Received: {data}")
        reversed_data = data[::-1]  # Reverse the string
        conn.send(reversed_data.encode())  # Send reversed string back
        print(f"Sent: {reversed_data}")

    conn.close()
    server_socket.close()

if __name__ == "__main__":
    start_server()
