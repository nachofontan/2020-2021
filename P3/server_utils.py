from Seq02 import Seq

def print_colored(message, color):
    import termcolor
    import colorama
    colorama.init(strip="False")
    print("To server: ", end="")
    print(termcolor.colored(message, color))

def format_command(command):
    return command.replace("\n", "").replace("\r", "")

def ping():
    print_colored("PING, command!", "green")

def get(cs, list_sequences, argument):
    print_colored("GET", "green")
    response = list_sequences[int(argument)]
    print("GET " + str(argument) + ": " + response)
    cs.send(response.encode())

def info(cs, list_sequences, argument):
    print_colored("INFO", "green")
    seq = Seq(list_sequences[int(argument)])
    print(seq)
    number_dict = seq.count()
    len1 = len(str(seq))
    percentage_dict = seq.percentage(seq.count_bases() , len1)
    response = "Sequence: " + list_sequences[int(argument)] + "\nTotal length: " + str(len1) + "\n"
    for key in number_dict:
        response += (str(key) + ": " + str(number_dict[key]) + " (" + str(percentage_dict[key], ) + "%)\n")
    print(response)
    cs.send(response.encode())

def comp(cs, list_sequences, argument):
    print_colored("COMP", "green")
    seq = Seq(list_sequences[int(argument)])
    response = seq.complement()
    response = "COMP " + str(seq) + "\n" + response
    print(response)
    cs.send(response.encode())

def rev(cs, list_sequences, argument):
    print_colored("REV", "green")
    seq = Seq(list_sequences[int(argument)])
    response = seq.reverse()
    response = "REV " + str(seq) + "\n" + response
    print(response)
    cs.send(response.encode())

def gene(cs, argument):
    GENE_FOLDER = "./SEQUENCES/"
    print_colored("GENE", "green")
    seq = Seq()
    response = seq.read_fasta(GENE_FOLDER + argument + ".txt")
    print(response)
    cs.send(str(response).encode())

