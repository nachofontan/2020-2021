from Seq02 import Seq

print("-----| Practice 1, Exercise 8 |------")
s1 = Seq('NULL')

s2 = Seq("ACTGA")

s3 = Seq("Invalid sequence")

print("Sequence", 1, ": (Length:",  s1.len(), ")",  s1)
print(f"Bases: {s1.count()}")
print(f"Rev: {s1.reverse(s1)}")
print(f"Comp: {s1.complement(s1)}")
print("Sequence", 2, ": (Length:",  s2.len(), ")",  s2)
print(f"Bases: {s2.count()}")
print(f"Rev: {s2.reverse(s2)}")
print(f"Comp: {s2.complement(s2)}")
print("Sequence", 3, ": (Length:",  s3.len(), ")",  s3)
print(f"Bases: {s3.count()}")
print(f"Rev: {s3.reverse(s3)}")
print(f"Comp: {s3.complement(s3)}")