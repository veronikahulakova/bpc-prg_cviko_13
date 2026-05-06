import matplotlib.pyplot as plt
class Sequence:
    def __init__(self, name, sequence):
        self.name = name
        self.sequence = sequence.upper()   # vždy uložíme velkými písmeny

    def length(self):
        return len(self.sequence)

    def __str__(self):
        return f"[{self.name}] délka={self.length()} nt, začátek: {self.sequence[:8]}..."

class DNASequence(Sequence):
    def gc_content(self):
        gc = self.sequence.count("G") + self.sequence.count("C")
        return gc / len(self.sequence)

    def base_counts(self):
        bases = {'A': 0, 'C': 0, 'G': 0, 'T': 0}
        for base in self.sequence:
            if base == 'A':
                bases['A'] += 1
            elif base == 'C':
                bases['C'] += 1
            elif base == 'G':
                bases['G'] += 1
            elif base == 'T':
                bases['T'] += 1
        return bases

    def plot_composition(self):
        counts = self.base_counts()
        bases = ["A", "C", "G", "T"]
        values = [counts[b] for b in bases]
        colors = ["tab:green", "tab:blue", "tab:orange", "tab:red"]

        plt.figure(figsize=(5, 3))
        plt.bar(bases, values, color=colors, edgecolor="black")
        plt.title(f"Složení bází: {self.name}")
        plt.ylabel("Počet")
        plt.tight_layout()
        plt.show()

    def is_valid(self):
        return set(self.sequence) <= {"A", "C", "G", "T"}

    def to_rna(self):
        return RNASequence(self.name, self.sequence.replace("T", "U"))


class RNASequence(Sequence):
    def is_valid(self):
        return set(self.sequence) <= {"A", "C", "G", "U"}

    def codons(self):
        codons = []
        for i in range(0, len(self.sequence) - 2, 3):
            codons.append(self.sequence[i:i + 3])
        return codons

    def find_start_codon(self):
        return self.sequence.find('AUG')



seq = Sequence("testovací", "acgtagctagc")
print(seq)            # [testovací] délka=11 nt, začátek: ACGTAGCT...
print(seq.length())   # 11
print(seq.sequence)   # ACGTAGCTAGC – automaticky převedeno na velká písmena

dna_seq_1 = DNASequence("DNA 1", "ACGT")
dna_seq_2 = DNASequence("DNA 2", "AAAA")
dna_seq_3 = DNASequence("DNA 3", "GCGC")
print(dna_seq_1.gc_content())
dna = DNASequence("mini", "ACCGGGTT")
print(dna.base_counts())   # {"A": 1, "C": 2, "G": 3, "T": 2}
dna_seq_4 = DNASequence('DNA 4', 'ACTAACTAATTAATTAATGCGAT')
print(dna_seq_4)
print(dna_seq_4.length())
print(dna_seq_4.gc_content())
# print(dna_seq_4.plot_composition())
print(dna_seq_4.is_valid())
dna_seq_5 = DNASequence('DNA 5', 'LGCTAGTAATCCTGACTAGCATG')
print(dna_seq_5)
print(dna_seq_5.length())
print(dna_seq_5.gc_content())
print(dna_seq_5.is_valid())
dna_seq_6 = DNASequence('DNA 6', 'GTCATGACTAGGACCGCCTACGG')
print(dna_seq_6)
print(dna_seq_6.length())
print(dna_seq_6.gc_content())
# print(dna_seq_6.plot_composition())
print(dna_seq_6.is_valid())

print(RNASequence("správná",   "ACGUACGU").is_valid())   # True
print(RNASequence("s thyminem","ACGTACGU").is_valid())   # False — T v RNA být nemá
rna = RNASequence("mini", "AUGGCUUAA")
print(rna.codons())   # ["AUG", "GCU", "UAA"]

rna2 = RNASequence("zbytek", "AUGGCUUA")
print(rna2.codons())  # ["AUG", "GCU"]   — poslední dvě písmena netvoří celý kodon

rna = RNASequence("gen", "CCAUGGCUUAA")
print(rna.find_start_codon())   # 2   — AUG začíná na indexu 2

dna = DNASequence("gen_01", "CCATGGCTTAA")

rna = dna.to_rna()
print(rna)                          # __str__ zděděné ze Sequence
print(rna.is_valid())               # True
print(rna.find_start_codon())       # pozice prvního AUG
print(rna.codons())                 # seznam kodonů