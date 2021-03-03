from pathlib import Path

def seq_ping():
    print("OK")


def  take_out_first_line(sequence):
    return sequence[sequence.find("\n") + 1:].replace("\n", "")

def seq_read_fasta(filename):
    sequence = take_out_first_line(Path(filename).read_text())
    return sequence
def seq_len(seq):
     return len(seq)

def seq_count_base(seq, base):
    return seq.count(base)

def seq_count(seq):
    gene_dict = {"A": 0, "C": 0, "G": 0, "T": 0}
    for d in seq:
        gene_dict[d] += 1

    return gene_dict
def seq_reverse(seq):
    reverse = seq[19::-1]
    return reverse
def seq_complement(seq):
    gene_dict = {"A": "T", "C":"G", "G": "C", "T": "A"}
    new_string = ""
    for d in seq:
        new_string += gene_dict[d]
    return new_string
import math
def seq_procesing_genes(seq_count):
    return max(seq_count, key=seq_count.get)