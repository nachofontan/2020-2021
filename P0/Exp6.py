import Seq0

gene_folder = "./SEQUENCES/"

gene_list = ["U5", "ADA", "FRAT", "FXN"]

print("-----| Exercise 6 |------")
for gene in gene_list:
    #"./SEQUENCE/"U5
    sequence = Seq0.seq_read_fasta(gene_folder + gene + ".txt")
    print("Gene", gene, ":\n", "Frag: ", sequence[0:20], "\n", "Rev: ", Seq0.seq_reverse(sequence))