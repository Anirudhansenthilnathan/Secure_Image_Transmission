import socket


# Function to send file to server
def send_file(filename, client_socket):
    with open(filename, "rb") as f:
        # Read the file in binary mode
        data = f.read()
        # Send the file data
        client_socket.sendall(data)


# Create a socket object
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Get the local machine name
host = "172.22.9.151"
port = 12345

# Connect to the server
client_socket.connect((host, port))

# Send image file to server
filename = "input.png"  # Update with your image file name
send_file(filename, client_socket)

# Close the connection
client_socket.close()
