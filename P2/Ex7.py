from client0 import Client
from pathlib import Path
from Seq02 import Seq

PRACTICE = 2
EXERCISE = 1

print(f"-----| Practice {2}, Exercise {7} |------")

IP = "192.168.1.12"
PORT = 12000
PORT_2 = 12002
c = Client(IP, PORT)
c_2 = Client(IP, PORT_2)

s = Seq()
s.read_fasta('../P0/FRAT1.txt')
i = 0
count = 0
while i < len(s.strbases) and count < 10:
    fragment = s.strbases[i:i+10]
    count += 1
    i += 10
    fragment_text = "Fragment "+ str(count) + ": " + fragment
    print(fragment_text)
    if count % 2 == 0:
        print(c_2.debug_talk(fragment_text))
    else:
        print(c.debug_talk(fragment_text))