from Seq02 import Seq

print("-----| Practice 1, Exercise 6 |------")

s1 = Seq()
s2 = Seq("ACTGA")
s3 = Seq("Invalid sequence")


print("Sequence 1: (Length : ", s1.len(), ")", s1)
print("Bases:", s1.count())

print("Sequence 2: (Length : ", s2.len(), ")", s2)
print("Bases:", s2.count())

print("Sequence 3: (Length : ", s3.len(), ")", s3)
print("Bases:", s3.count())