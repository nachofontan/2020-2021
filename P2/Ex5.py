

from client0 import Client
from pathlib import Path


PRACTICE = 2
EXERCISE = 5

print(f"-----| Practice {PRACTICE}, Exercise {EXERCISE} |------")

# -- Parameters of the server to talk to
IP = "192.168.1.12"
PORT = 12000

# -- Create a client object
c = Client(IP, PORT)
print(c.talk("Sending the U5 Gene to the server..."))
print(c.talk(Path("U5.txt").read_text()))