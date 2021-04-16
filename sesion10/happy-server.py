import socket

# Configure the Server's IP and PORT
PORT = 8080
IP = "localhost"  #only connections from the local ip/host

# -- Step 1: create the socket
ls = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# -- Step 2: Bind the socket to server's IP and PORT
ls.bind((IP, PORT))

# -- Step 3: Configure the socket for listening
ls.listen()

print("The server is configured!")

# -- Close the socket
ls.close()