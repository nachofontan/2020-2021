import Seq0

gene_folder = "./SEQUENCES/"

gene_list = ["U5", "ADA", "FRAT", "FXN"]
base_list = ["A","C","T","G"]
print("-----| Exercise 4 |------")
for gene in gene_list:
    #"./SEQUENCE/"U5
    sequence = Seq0.seq_read_fasta(gene_folder + gene + ".txt")
    print("gene", gene)
    for base in base_list:
        print(base + ":", Seq0.seq_count_base(sequence, base))
    print("\n")