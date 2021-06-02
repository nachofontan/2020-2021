import pathlib


class Seq:
    NULL='NULL'
    INVALID='ERROR'

    def __init__(self, strbases=NULL):
        if strbases == Seq.NULL:
            print("NULL Seq Created")
            self.strbases = strbases
        elif Seq.is_valid_sequence_2(strbases):
            self.strbases=strbases
            print('New sequence created')
        else:
            self.strbases=Seq.INVALID
            print('Invalid sequence')



    @staticmethod
    def is_valid_sequence_2(strbases):
        for c in strbases:
            if c!='A' and c !='C' and c!='G' and c!= 'T':
               return False
        return True

    def __str__(self):
        return self.strbases

    def len(self):
        if self.strbases == Seq.NULL or self.strbases==Seq.INVALID:
            return 0
        else:
            return len(self.strbases)


    def count_bases(self):
        a, c, g, t = 0, 0, 0, 0
        if not (self.strbases == Seq.NULL) and not (self.strbases == Seq.INVALID):
            for ch in self.strbases:
                if ch == "A":
                    a += 1
                elif ch == "T":
                    t += 1
                elif ch == "G":
                    g += 1
                elif ch == "C":
                    c += 1
        return a, c, g, t

    def count(self):
        bases = ["A", "C", "T", "G"]
        count_bases = []
        for base in bases:
            count_bases.append(self.count_base(base))
        dictionary = dict(zip(bases, count_bases))
        return dictionary

    #def percentage(self):
        #a, c, g, t = self.count()
        #total = a + c + g + t
        #return {"A": (a/total)*100, "C": (c/total)*100, "G": (g/total)*100, "T": (t/total)*100}

    def percentage(self, count_bases, seq_len):
        a = str(round(count_bases[0] / seq_len * 100, 2)) + "%"
        c = str(round(count_bases[1] / seq_len * 100, 2)) + "%"
        g = str(round(count_bases[2] / seq_len * 100, 2)) + "%"
        t = str(round(count_bases[3] / seq_len * 100, 2)) + "%"
        return a, c, g, t

    def reverse(self):
        rev_seq = ''
        if self.strbases == Seq.NULL:
            return self.strbases
        else:
            for e in self.strbases[::-1]:
                if e not in ["A", "C", "T", "G"]:
                    rev_seq = Seq.INVALID
                    return rev_seq

                else:
                    rev_seq += e
        return rev_seq


    def complement(self):
        comp_seq = ""
        if self.strbases == Seq.NULL:
            return self.strbases
        else:
            for e in self.strbases:
                if e not in ["A", "C", "T", "G"]:
                    comp_seq = Seq.INVALID
                    return comp_seq
                else:
                    if e == "A":
                        comp_seq += "T"
                    if e == "T":
                        comp_seq += "A"
                    if e == "C":
                        comp_seq += "G"
                    if e == "G":
                        comp_seq += "C"
            return comp_seq

    def read_fasta(self, filename):
        file_lines = pathlib.Path(filename).read_text().split("\n")
        body = (file_lines[1:])
        self.strbases = ''.join(body)
        return self

    def frequency(self):
        a, c, g, t = 0, 0, 0, 0
        for e in self.strbases:
            if e == "A":
                a += 1
            elif e == "C":
                c += 1
            elif e == "G":
                g += 1
            elif e == "T":
                t += 1
        new_dict = {"A": a, "C": c, "G": g, "T": t}
        number_most_frequent = max(new_dict.values())
        for k, v in new_dict.items():
            if v == number_most_frequent:
                most_frequent_base = k
        return most_frequent_base
