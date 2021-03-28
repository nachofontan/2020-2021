from client0 import Client
from pathlib import Path
from P1.Seq02 import Seq



PRACTICE = 2
EXERCISE = 6

print(f"-----| Practice {PRACTICE}, Exercise {EXERCISE} |------")

# -- Parameters of the server to talk to
IP = "192.168.1.12"
PORT = 12000

# -- Create a client object
c = Client(IP, PORT)
s = Seq
s.read_fasta('.../SEQUENCES/FRAT.txt')
print(s.strbases)
