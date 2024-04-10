import collections
dnaNucleotides = ["A", "T", "C", "G"]
rnaNucleotides = ["U", "A", "C", "G"]
RNA_Codons = {
    # M = START ; * =  STOP
    "GCU": "A", "GCC": "A", "GCA": "A", "GCG": "A",
    "UGU": "C", "UGC": "C",
    "GAU": "D", "GAC": "D",
    "GAA": "E", "GAG": "E",
    "UUU": "F", "UUC": "F",
    "GGU": "G", "GGC": "G", "GGA": "G", "GGG": "G",
    "CAU": "H", "CAC": "H",
    "AUA": "I", "AUU": "I", "AUC": "I",
    "AAA": "K", "AAG": "K",
    "UUA": "L", "UUG": "L", "CUU": "L", "CUC": "L", "CUA": "L", "CUG": "L",
    "AUG": "M",
    "AAU": "N", "AAC": "N",
    "CCU": "P", "CCC": "P", "CCA": "P", "CCG": "P",
    "CAA": "Q", "CAG": "Q",
    "CGU": "R", "CGC": "R", "CGA": "R", "CGG": "R", "AGA": "R", "AGG": "R",
    "UCU": "S", "UCC": "S", "UCA": "S", "UCG": "S", "AGU": "S", "AGC": "S",
    "ACU": "T", "ACC": "T", "ACA": "T", "ACG": "T",
    "GUU": "V", "GUC": "V", "GUA": "V", "GUG": "V",
    "UGG": "W",
    "UAU": "Y", "UAC": "Y",
    "UAA": "*", "UAG": "*", "UGA": "*"
}

# Verifying sequence

def validateSeq(dna_seq):
    tmpseq = dna_seq.upper()
    for nuc in tmpseq:
        if nuc not in dnaNucleotides:
            return "\n You have not entered a valid DNA sequence.\n\n Check your sequence and try again.\n"
    return tmpseq

# Counting DNA nucleotide frequency

def countNucFreq(seq):
    return dict(collections.Counter(seq))

# Mapping DNA to RNA

def rnaMap(seq):
    tmpseq = seq.maketrans("ATGC", "UACG")
    mRNA = seq.translate(tmpseq)
    return mRNA

# Mapping DNA to Protien

def proMAP(seq):
    tmpseq = seq.maketrans("ATGC", "UACG")
    mRNA = seq.translate(tmpseq)

    pro = ""

    for i in range(0, len(mRNA), 3):
    
        codon = mRNA[i:i+3]
    
        pro += RNA_Codons.get(codon, '')

    return pro

