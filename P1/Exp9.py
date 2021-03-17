from Seq02 import Seq
print('-----| Practice 1, Exercise 9 |------')
FOLDER = "../SEQUENCES/"
file_name = FOLDER + "U5.txt"
s0 = Seq('')
s0 = s0.read_fasta(file_name)

print(f"Sequence : (Length: {s0.len()}) {s0}")
print(f"Bases: {s0.count()}")
print(f"Rev: {s0.reverse(s0)}")
print(f"Comp: {s0.complement(s0)}")