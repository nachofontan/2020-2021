from client0 import Client
PRACTICE = 2
EXERCISE = 1

from client0 import Client

PRACTICE = 2
EXERCISE = 1

print(f"-----| Practice {PRACTICE}, Exercise {EXERCISE} |------")

# -- Parameters of the server to talk to
IP = "192.168.1.12"
PORT = 12000

# -- Create a client object
c = Client(IP, PORT)

# -- Test the ping method
c.ping()
c.advanced_ping()


# -- Print the IP and PORTs
print(f"IP: {c.ip}, {c.port}")