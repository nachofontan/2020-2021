import socket

# SERVER IP, PORT
PORT = 8080
IP = "192.168.1.12"

# First, create the socket
# We will always use this parameters: AF_INET y SOCK_STREAM
hello_server = "Hi!"
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# establish the connection to the Server (IP, PORT)
s.connect((IP, PORT))

# Send data. No strings can be send, only bytes
# It necesary to encode the string into bytes
s.send(hello_server.encode())

# Receive data from the server
msg = s.recv(2048).decode()
print(msg)
s.close()