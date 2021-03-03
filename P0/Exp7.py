import Seq0

gene_folder = "./SEQUENCES/"

gene_list = ["U5", "ADA", "FRAT", "FXN"]

print("-----| Exercise 7 |------")
for gene in gene_list:
    sequence = Seq0.seq_read_fasta(gene_folder + gene + ".txt")
    print("Gene", gene, ":\n", "Frag: ", sequence[0:20], "\n", "Compl: ", Seq0.seq_complement(sequence[0:20]))
