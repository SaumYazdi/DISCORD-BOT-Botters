import socket
import threading

# Define the proxy server's IP and port
PROXY_IP = '0.0.0.0'  # Listen on all available interfaces
PROXY_PORT = 8080

# Create a socket to listen for incoming connections
proxy_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
proxy_socket.bind((PROXY_IP, PROXY_PORT))
proxy_socket.listen(5)
print(f"Proxy server is listening on {PROXY_IP}:{PROXY_PORT}")

# Function to handle client connections
def handle_client(client_socket):
    request = client_socket.recv(4096)
    destination = ("discord.com/login", 80)  # Correct the destination server details
    
    # Create a socket to connect to the destination server
    destination_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    destination_socket.connect(destination)
    
    destination_socket.send(request)
    
    response = destination_socket.recv(4096)
    client_socket.send(response)
    
    destination_socket.close()
    client_socket.close()

# Main loop to accept incoming connections
while True:
    client_socket, client_address = proxy_socket.accept()
    print(f"Accepted connection from {client_address[0]}:{client_address[1]}")
    client_thread = threading.Thread(target=handle_client, args=(client_socket,))
    client_thread.start()
