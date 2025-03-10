import socket

def start_client(host='127.0.0.1', port=12345):
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((host, port))  # Connect to the server

    while True:
        message = input("Enter a string (or 'exit' to quit): ")
        if message.lower() == 'exit':
            break  # Exit the loop

        client_socket.send(message.encode())  # Send message
        reversed_message = client_socket.recv(1024).decode()  # Receive reversed string
        print(f"Reversed String: {reversed_message}")

    client_socket.close()

if __name__ == "__main__":
    start_client()
