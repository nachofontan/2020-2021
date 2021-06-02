from client0 import Client
from pathlib import Path
from Seq02 import Seq



PRACTICE = 2
EXERCISE = 6

print(f"-----| Practice {PRACTICE}, Exercise {EXERCISE} |------")

# -- Parameters of the server to talk to
IP = "192.168.1.12"
PORT = 12000

# -- Create a client object
c = Client(IP, PORT)
s = Seq()
s.read_fasta("FRAT1.txt")
count = 0
for i in range (0, len(s.strbases), 10 ):
    fragment = s.strbases[i:i + 10]
    print(fragment)
    count = count + 1
    if count == 5:
        break
    print("Fragment", count, ":", fragment)
    print(c.talk(fragment))
