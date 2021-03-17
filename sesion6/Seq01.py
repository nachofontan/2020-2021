
class Seq:
    """A class for representing sequences"""

    def __init__(self, strbases):
        self.strbases = strbases
        if self.is_valid_sequence():
            print("New sequence created!!")
            self.strbases = strbases

        else:
            self.strbases = "error"
            print("Incorrect sequence")

        # Initialize the sequence with the value
        # passed as argument when creating the object

    def print_bases(self):
        print(self.strbases)
    def is_valid_sequence(self):
        for bases in (self.strbases):
            if bases != "A" or bases != "G" or bases != "T" or bases != "C":
                return False
        return True

    @staticmethod
    def is_valid_sequence_2(bases):
        for bases in self.strbases:
            if bases != "A" and bases != "G" and bases != "T" and bases != "C":
                return False
        return True


    def __str__(self):
        """Method called when the object is being printed"""

        # -- We just return the string with the sequence
        return self.strbases

    def len(self):
        """Calculate the length of the sequence"""
        return len(self.strbases)

#is in the module but outside the class
def generate_seqs(pattern, number):
    #A, 3
    list_seq = []
    for i in range(0, number):
            #A i = 0 -> A
            #A i = 1 -> AA
            # A i = 2 -> AAA
        list_seq.append(Seq.pattern * (i + 1))
    return list_seq




class Gene(Seq):
    """This class is derived from the Seq Class
       All the objects of class Gene will inherite
       the methods from the Seq class
    """
    pass

# --- Main program
s1 = Seq("AGT")
s2 = Seq("CGAAC")

# -- Printing the objects
print(f"Sequence 1: {s1}")
print(f"  Length: {s1.len()}")
print(f"Gene: {s2}")
print(f"  Length: {s2.len()}")
