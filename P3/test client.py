import client0

print("-----| Practice 3, Exercise 7 |-----")

IP = "127.0.0.1"
PORT = 8080
gene_list = ["ADA", "FRAT1", "FXN", "RNU6_269P", "U5"]
function_list = ["PING", "GET ", "INFO 0", "COMP 0", "REV 0", "GENE "]

c = client0.Client(IP, PORT)
print(c)

print(c.talk("PING"))
for i in range(5):
    print(c.talk("GET "+ str(i)))
print(c.talk("INFO 0"))
print(c.talk("COMP 0"))
print(c.talk("REV 0"))
for gene in gene_list:
    print("GENE", gene)
    print(c.talk("GENE " + gene))