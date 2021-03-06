import Seq0

gene_folder = "./SEQUENCES/"

gene_list = ["U5", "ADA", "FRAT", "FXN"]

print("-----| Exercise 5 |------")
for gene in gene_list:
    #"./SEQUENCE/"U5
    sequence = Seq0.seq_read_fasta(gene_folder + gene + ".txt")
    print("Gene", gene, ":", Seq0.seq_count(sequence))
