import Seq0
gene_folder = "./SEQUENCES/"

gene_list = ["U5", "ADA", "FRAT", "FXN"]

print("-----| Exercise 7 |------")
for gene in gene_list:
    sequence = Seq0.seq_read_fasta(gene_folder + gene + ".txt")
    x = max(Seq0.seq_count(sequence)).keys().get