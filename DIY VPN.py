import socket
import threading

# Define the VPN server's IP and port
SERVER_IP = '0.0.0.0'  # Listen on all available interfaces
SERVER_PORT = 8080

# Create a socket to listen for incoming connections
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((SERVER_IP, SERVER_PORT))
server_socket.listen(5)
print(f"VPN server is listening on {SERVER_IP}:{SERVER_PORT}")

# Function to handle client connections
def handle_client(client_socket):
    while True:
        data = client_socket.recv(1024)
        if not data:
            break
        # Process data here (you can forward data to the real destination)
        print(f"Received data: {data.decode()}")
    client_socket.close()

# Main loop to accept incoming connections
while True:
    client_socket, client_address = server_socket.accept()
    print(f"Accepted connection from {client_address[0]}:{client_address[1]}")
    client_thread = threading.Thread(target=handle_client, args=(client_socket,))
    client_thread.start()
