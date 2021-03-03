import Seq0
gene_folder = "./SEQUENCES/"

gene_list = ["U5", "ADA", "FRAT", "FXN"]

print("-----| Exercise 8 |------")
for gene in gene_list:
    sequence = Seq0.seq_read_fasta(gene_folder + gene + ".txt")
    bases_count = Seq0.seq_count((sequence))
    print("Gene", gene, ": Most frequent Base: ", Seq0.seq_procesing_genes(bases_count))
